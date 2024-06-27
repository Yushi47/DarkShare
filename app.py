from flask import Flask, send_from_directory, render_template
from flask_talisman import Talisman
import os
from config import config
import logging

# Import Blueprints
from blueprints.main import main_bp
from blueprints.file_ops import file_ops_bp
from blueprints.url_ops import url_ops_bp
from blueprints.text_ops import text_ops_bp

app = Flask(__name__)

# Disable strict CSP policy for local use
csp = {
    'default-src': ['\'self\''],
    'script-src': ['\'self\'', '\'unsafe-inline\''],
    'style-src': ['\'self\'', '\'unsafe-inline\'', 'https://fonts.googleapis.com'],
    'font-src': ['\'self\'', 'https://fonts.gstatic.com']
}

Talisman(app, content_security_policy=csp)  # Enforce HTTPS and security headers

config_name = os.getenv('FLASK_CONFIG') or 'default'
app.config.from_object(config[config_name])
config[config_name].init_app(app)

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize text.json and urls.txt if they don't exist
def initialize_file(file_path):
    if not os.path.exists(file_path):
        open(file_path, 'w').close()

initialize_file(app.config['TEXT_FILE'])
initialize_file(app.config['URLS_FILE'])

# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(file_ops_bp)
app.register_blueprint(url_ops_bp)
app.register_blueprint(text_ops_bp)

# Route to serve favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'icons'), 'favicon.ico')

# Example route to demonstrate nonce usage
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure SSL certificate and key file paths are correct
    ssl_cert = app.config['SSL_CERT']
    ssl_key = app.config['SSL_KEY']
    if not os.path.isfile(ssl_cert) or not os.path.isfile(ssl_key):
        raise FileNotFoundError(f"SSL certificate or key file not found. Ensure the paths are correct:\nSSL_CERT={ssl_cert}\nSSL_KEY={ssl_key}")
    
    ssl_context = (ssl_cert, ssl_key)
    
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)
    
    try:
        app.run(host=app.config['IP_ADDRESS'], port=app.config['PORT'], debug=app.config['DEBUG'], ssl_context=ssl_context)
    except Exception as e:
        logging.exception("An error occurred while running the Flask application.")
