import re
from flask import Blueprint, request, redirect, url_for, send_from_directory, abort, send_file, current_app, jsonify
import os
import urllib.parse
import io
import zipfile
from werkzeug.utils import secure_filename

file_ops_bp = Blueprint('file_ops', __name__)

# Regular expression pattern to match valid URLs
URL_PATTERN = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def is_valid_url(url):
    return re.match(URL_PATTERN, url) is not None

@file_ops_bp.route('/', methods=['POST'])
def upload_file():
    try:
        if 'files[]' in request.files:
            files = request.files.getlist('files[]')
            for file in files:
                if file.filename == '':
                    continue
                filename = secure_filename(file.filename)
                file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        
        urls = request.form.get('url')
        if urls:
            url_list = urls.split()
            url_list = [url.strip() for url in url_list if url.strip()]
            valid_urls = [url for url in url_list if is_valid_url(url)]
            current_app.logger.debug(f"Valid URLs received: {valid_urls}")
            
            if os.path.exists(current_app.config['URLS_FILE']):
                with open(current_app.config['URLS_FILE'], 'r', encoding='utf-8') as f:
                    existing_urls = f.read().splitlines()
            else:
                existing_urls = []

            updated_urls = list(set(existing_urls + valid_urls))  # Remove duplicates
            current_app.logger.debug(f"Updated URLs before saving: {updated_urls}")

            with open(current_app.config['URLS_FILE'], 'w', encoding='utf-8') as f:
                for url in updated_urls:
                    f.write(f"{url}\n")

        return redirect(url_for('main.index'))
    except Exception as e:
        current_app.logger.error(f"Error uploading files or URLs: {e}")
        abort(500, description="Internal Server Error: Unable to upload files or URLs.")

@file_ops_bp.route('/uploaded_file/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

@file_ops_bp.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    try:
        decoded_filename = urllib.parse.unquote(filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], decoded_filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            current_app.logger.info(f"File deleted successfully: {decoded_filename}")
            return jsonify({"message": "File deleted successfully"}), 200
        else:
            current_app.logger.warning(f"File not found: {decoded_filename}")
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        current_app.logger.error(f"Error deleting file {filename}: {e}")
        abort(500, description="Internal Server Error: Unable to delete file.")

@file_ops_bp.route('/delete_all_files', methods=['DELETE'])
def delete_all_files():
    try:
        files = os.listdir(current_app.config['UPLOAD_FOLDER'])
        for file in files:
            os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], file))
        return jsonify({"message": "All files deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting all files: {e}")
        abort(500, description="Internal Server Error: Unable to delete all files.")

@file_ops_bp.route('/download_all_files')
def download_all_files():
    try:
        files = os.listdir(current_app.config['UPLOAD_FOLDER'])
        if not files:
            return redirect(url_for('main.index'))
        
        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w') as zf:
            for file in files:
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file)
                zf.write(file_path, file)
        memory_file.seek(0)
        return send_file(memory_file, download_name='all_files.zip', as_attachment=True)
    except Exception as e:
        current_app.logger.error(f"Error downloading all files: {e}")
        abort(500, description="Internal Server Error: Unable to download all files.")
