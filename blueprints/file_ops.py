from flask import Blueprint, request, redirect, url_for, send_from_directory, abort, send_file, current_app, jsonify
import os
import urllib.parse
import io
import zipfile
from werkzeug.utils import secure_filename

file_ops_bp = Blueprint('file_ops', __name__)

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
        
        return redirect(url_for('main.index'))
    except Exception as e:
        current_app.logger.error(f"Error uploading files: {e}")
        abort(500, description="Internal Server Error: Unable to upload files.")

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
