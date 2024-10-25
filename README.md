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
