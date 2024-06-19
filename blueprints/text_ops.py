from flask import Blueprint, request, jsonify, current_app, abort
import json
import os

text_ops_bp = Blueprint('text_ops', __name__)

@text_ops_bp.route('/save_text', methods=['POST'])
def save_text():
    data = request.json
    if not data or 'text' not in data:
        abort(400, description="Invalid request: 'text' field is required.")
    
    try:
        with open(current_app.config['TEXT_FILE'], 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return '', 204
    except Exception as e:
        current_app.logger.error(f"Error saving text: {e}")
        abort(500, description="Internal Server Error: Unable to save text.")

@text_ops_bp.route('/load_text', methods=['GET'])
def load_text():
    try:
        if os.path.exists(current_app.config['TEXT_FILE']):
            with open(current_app.config['TEXT_FILE'], 'r', encoding='utf-8') as f:
                text_data = json.load(f)
            return jsonify(text_data)
        else:
            return jsonify({'text': ''})
    except Exception as e:
        current_app.logger.error(f"Error loading text: {e}")
        abort(500, description="Internal Server Error: Unable to load text.")
