import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SHARED_FOLDER = os.getenv('SHARED_FOLDER', 'C:\\Users\\(User)\\Desktop\\SharedFolder')
    UPLOAD_FOLDER = os.path.join(SHARED_FOLDER, 'uploads')
    TEXT_FILE = os.path.join(SHARED_FOLDER, 'text.json')
    URLS_FILE = os.path.join(SHARED_FOLDER, 'urls.txt')
    IP_ADDRESS = os.getenv('IP_ADDRESS', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8000))
    DEBUG = os.getenv('DEBUG', 'True').lower() in ['true', '1', 't']
    SSL_CERT = os.getenv('SSL_CERT', os.path.join('certs', 'selfsigned.crt'))
    SSL_KEY = os.getenv('SSL_KEY', os.path.join('certs', 'selfsigned.key'))

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
