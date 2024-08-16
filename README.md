# DarkShare

DarkShare is a Flask-based web application for efficient file sharing and management. This README provides instructions for setting up and running the application.

## Features
- File Upload and Download Easily manage file uploads and downloads.
- Clipboard Functionality Copy and paste text using clipboard functionalities.
- Persistent Text Box Quicly share text between different devices.
- File Deletion Remove files with a single confirmation.
- Dynamic Script Loading Efficiently load and manage scripts.
- Secure HTTPS Supports self-signed SSL certificates for secure communication.

## Installation

Follow these steps to set up DarkShare on your local machine for development and testing

### Prerequisites

Make sure you have the following installed
- Python (= 3.6)
- pip (Python package installer)
- Flask and other dependencies listed in `requirements.txt`

### Clone the Repository

```bash
git clone httpsgithub.comyourusernamedarkshare.git
cd darkshare
```

### Create and Activate a Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venvbinactivate   # On Windows use `venvScriptsactivate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```
## Setting the IP Address

### Configuring the IP Address
1. Find an IP outside the DHCP range of your router
   - Access your router's configuration page (usually `192.168.1.1` or `192.168.0.1`) through a web browser.
   - Log in with your admin credentials.
   - Locate the DHCP settings section. Identify the DHCP range.
   - Choose an IP address outside this range (e.g., if the DHCP range is `192.168.1.100 - 192.168.1.200`, you can choose `192.168.1.201`).

2. Assign IP to your PCHost
   - On Windows
     - Go to `Control Panel  Network and Sharing Center  Change adapter settings`.
     - Right-click on the network adapter connected to your router and select `Properties`.
     - Select `Internet Protocol Version 4 (TCPIPv4)` and click `Properties`.
     - Select `Use the following IP address` and enter your chosen IP (e.g., `192.168.1.201`). Set the Subnet mask, usually `255.255.255.0`, and Default gateway (your router’s IP, e.g., `192.168.1.1`).

   - On MacLinux
     - Open `System Preferences  Network`.
     - Select your active network connection and click `Advanced`.
     - Go to the `TCPIP` tab. Set `Configure IPv4` to `Manually`.
     - Enter your chosen IP (e.g., `192.168.1.201`), Subnet mask (`255.255.255.0`), and Router (default gateway, e.g., `192.168.1.1`).

## Configuration

### Environment Variables

Update the `.env` file in the root of your project directory with the following content. Note Update the `SHARED_FOLDER` path to match your local directory before usage.

```env
# Path to the shared folder (update this path according to your setup)
SHARED_FOLDER=CUsers(User)DesktopSharedFolder

# Server IP address
IP_ADDRESS=0.0.0.0

# Server port
PORT=8000

# Enable or disable debug mode
DEBUG=True

# Path to the SSL certificate
SSL_CERT=certsselfsigned.crt

# Path to the SSL key
SSL_KEY=certsselfsigned.key
```
### Config.py

Update the `confi.py` file in the root of your project directory with the following content. Note Update the `SHARED_FOLDER` path to match your local directory before usage.

```config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config
    SHARED_FOLDER = os.getenv('SHARED_FOLDER', 'CUsers(User)DesktopSharedFolder') # Path to the shared folder (update this path according to your setup)
    UPLOAD_FOLDER = os.path.join(SHARED_FOLDER, 'uploads')
    TEXT_FILE = os.path.join(SHARED_FOLDER, 'text.json')
    URLS_FILE = os.path.join(SHARED_FOLDER, 'urls.txt')
    IP_ADDRESS = os.getenv('IP_ADDRESS', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8000))
    DEBUG = os.getenv('DEBUG', 'True').lower() in ['true', '1', 't']
    SSL_CERT = os.getenv('SSL_CERT', os.path.join('certs', 'selfsigned.crt'))
    SSL_KEY = os.getenv('SSL_KEY', os.path.join('certs', 'selfsigned.key'))

    @staticmethod
    def init_app(app)
        pass

class DevelopmentConfig(Config)
    DEBUG = True

class TestingConfig(Config)
    TESTING = True
    DEBUG = True

class ProductionConfig(Config)
    DEBUG = False

config = {
    'development' DevelopmentConfig,
    'testing' TestingConfig,
    'production' ProductionConfig,
    'default' ProductionConfig
}
```

### SSL Certificates

You can use the self-signed SSL certificates provided in the `certs` directory. Ensure these files are correctly placed and referenced in your `.env` file.

## Usage

1. Run the Application

   Start the Flask application with

   ```bash
   flask run --host=your-ip-address --port=8000
   ```

   Replace `your-ip-address` with the IP address you configured in the `.env` file.

2. Access the Application

   Open a web browser and navigate to `httpyour-ip-address8000` to use the application.

## Known Issues

- Upload Speeds The current implementation may have limitations with upload speeds and handling of large files.
- File Sizes There may be issues with very large files. Improvements are planned to address these areas.

## Screenshots for the UI

<p align="center">
<a href="#">
<img src="https://i.gyazo.com/bdd44540b5f22bc08c202b2d88f6ad02.png" width="500" alt="logo"/>
</a>
</p>
