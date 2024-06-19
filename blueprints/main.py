from flask import Blueprint, render_template, current_app, abort
import os

main_bp = Blueprint('main', __name__)

def get_file_type(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png', '.gif']:
        return 'image-icon'
    elif ext in ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm']:
        return 'video-icon'
    elif ext in ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a']:
        return 'audio-icon'
    elif ext in ['.pdf']:
        return 'pdf-icon'
    elif ext in ['.doc', '.docx']:
        return 'word-icon'
    elif ext in ['.xls', '.xlsx']:
        return 'excel-icon'
    elif ext in ['.txt']:
        return 'txt-icon'
    elif ext in ['.config', '.env']:
        return 'config-icon'
    elif ext in ['.css']:
        return 'css-icon'
    elif ext in ['.html']:
        return 'html-icon'
    elif ext in ['.js']:
        return 'js-icon'
    elif ext in ['.json']:
        return 'json-icon'
    elif ext in ['.ppt', '.pptx', '.pot']:
        return 'powerpoint-icon'
    elif ext in ['.py']:
        return 'python-icon'
    elif ext in ['.md']:
        return 'readme-icon'
    elif ext in ['.zip', '.rar', '.7z']:
        return 'zip-icon'
    else:
        return 'file-icon'

@main_bp.route('/')
def index():
    try:
        files = os.listdir(current_app.config['UPLOAD_FOLDER'])
    except Exception as e:
        current_app.logger.error(f"Error listing files in {current_app.config['UPLOAD_FOLDER']}: {e}")
        abort(500, description="Internal Server Error: Unable to list files.")
    
    try:
        with open(current_app.config['URLS_FILE'], 'a+') as f:
            f.seek(0)
            urls = f.readlines()
    except Exception as e:
        current_app.logger.error(f"Error reading URLs from {current_app.config['URLS_FILE']}: {e}")
        abort(500, description="Internal Server Error: Unable to read URLs.")

    return render_template('index.html', files=files, urls=urls, get_file_type=get_file_type)
