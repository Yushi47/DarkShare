import re
from flask import Blueprint, request, abort, current_app, jsonify
import urllib.parse
import os

url_ops_bp = Blueprint('url_ops', __name__)

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

@url_ops_bp.route('/delete_url/<path:url>', methods=['DELETE'])
def delete_url(url):
    try:
        decoded_url = urllib.parse.unquote(url).strip()
        current_app.logger.info(f"Received request to delete URL: {url}")
        current_app.logger.info(f"Decoded URL: {decoded_url}")

        if os.path.exists(current_app.config['URLS_FILE']):
            with open(current_app.config['URLS_FILE'], 'r', encoding='utf-8') as f:
                urls = f.readlines()
            urls = [u.strip() for u in urls if u.strip() != decoded_url]

            with open(current_app.config['URLS_FILE'], 'w', encoding='utf-8') as f:
                for u in urls:
                    f.write(u + '\n')

        current_app.logger.info(f"URL deleted successfully: {decoded_url}")
        return jsonify({"message": "URL deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting URL {url}: {e}")
        abort(500, description="Internal Server Error: Unable to delete URL.")

@url_ops_bp.route('/delete_all_urls', methods=['DELETE'])
def delete_all_urls():
    try:
        if os.path.exists(current_app.config['URLS_FILE']):
            open(current_app.config['URLS_FILE'], 'w', encoding='utf-8').close()
        current_app.logger.info("All URLs deleted successfully")
        return jsonify({"message": "All URLs deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting all URLs: {e}")
        abort(500, description="Internal Server Error: Unable to delete all URLs.")

@url_ops_bp.route('/add_url', methods=['POST'])
def add_url():
    data = request.json
    if not data or 'url' not in data:
        abort(400, description="Invalid request: 'url' field is required.")
    
    try:
        new_url = data['url'].strip()
        if not is_valid_url(new_url):
            abort(400, description="Invalid URL format.")
        with open(current_app.config['URLS_FILE'], 'a', encoding='utf-8') as f:
            f.write(new_url + '\n')
        
        current_app.logger.info(f"URL added successfully: {new_url}")
        return jsonify({"message": "URL added successfully"}), 201
    except Exception as e:
        current_app.logger.error(f"Error adding URL {new_url}: {e}")
        abort(500, description="Internal Server Error: Unable to add URL.")

@url_ops_bp.route('/get_urls', methods=['GET'])
def get_urls():
    try:
        if os.path.exists(current_app.config['URLS_FILE']):
            with open(current_app.config['URLS_FILE'], 'r', encoding='utf-8') as f:
                urls = [u.strip() for u in f.readlines()]
        else:
            urls = []
        return jsonify(urls)
    except Exception as e:
        current_app.logger.error(f"Error getting URLs: {e}")
        abort(500, description="Internal Server Error: Unable to get URLs.")
