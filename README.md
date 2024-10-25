# Crypto Stock CLI Application

A command-line application to fetch and display stock and cryptocurrency data using the Finnhub and CryptoCompare APIs. This tool provides live updates for selected stocks and cryptocurrencies, with a simple and interactive interface.

## Features
- Fetch current stock data, including prices, highs, lows, and volume.
- Get live cryptocurrency prices in USD.
- Interactive menu for easy navigation.
- Support for Linux, Windows, and macOS binaries.

## Installation

### Prerequisites
- Python 3.x
- API keys for [Finnhub](https://finnhub.io/) and [CryptoCompare](https://min-api.cryptocompare.com/)

### Downloading the Application
Binaries are available for each operating system:
1. Go to the [Releases](https://github.com/King-kin5/Stock/releases) section of this repository.
2. Download the appropriate binary for your OS:
   - `crypto-linux` for Linux
   - `crypto-macos` for macOS
   - `crypto-windows.exe` for Windows

### Setting Up the API Key
Replace the `FINNHUB_API_TOKEN` variable in the script with your actual API token.

### Running the Application
Once downloaded, you can run the application directly from the terminal:

#### Linux/macOS:
```bash
./crypto-linux   # For Linux
./crypto-macos   # For macOS
crypto-windows.exe # For windows





                                                        ## Building from Source



If you want to build the Crypto and Stock Data Fetcher application from source, follow these steps: Ensure you have the following installed on your system: **Python 3.x**: Download and install from [python.org](https://www.python.org/downloads/). **pip**: Python's package installer (usually comes with Python). **PyInstaller**: For creating standalone executables. Open your terminal or command prompt and run: 


git clone https://github.com/King-kin5/Stock.git
cd Stock
Create a virtual environment (optional but recommended) and install the necessary Python packages:

python -m venv venv          # Create a virtual environment
source venv/bin/activate     # Activate on Linux or macOS
# venv\Scripts\activate       # Activate on Windows
pip install -r requirements.txt
If you haven’t installed PyInstaller yet, run:

pip install pyinstaller
Create the executable binary by running:


pyinstaller --onefile crypto.py
This will generate a standalone executable, which can be found in the dist directory after the build process is complete. Navigate to the dist directory and run the binary:


cd dist
# For Linux
./crypto-linux
# For macOS
./crypto-macos
# For Windows
crypto-windows.exe



