import os
import requests
import logging
import time
import threading

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace with your actual Finnhub API token
FINNHUB_API_TOKEN = 'cqogti9r01qk95834dq0cqogti9r01qk95834dqg'

# Default list of stock symbols
DEFAULT_STOCK_SYMBOLS = [
    'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA', 'META', 'NVDA',
    'BRK.B', 'JNJ', 'JPM', 'V', 'PG', 'INTC', 'WMT', 'HD',
    'DIS', 'NFLX', 'UNH', 'MA', 'KO'
]

def fetch_stock_data(symbol):
    url = f'https://finnhub.io/api/v1/quote'
    params = {
        'symbol': symbol,
        'token': FINNHUB_API_TOKEN
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            logger.error(f"Error fetching data from {url} with status code {response.status_code}")
            return

        data = response.json()
        if data:
            print("\n--- Stock Data ---")
            current_price = data.get('c', 'N/A')  # Current price
            high_price = data.get('h', 'N/A')     # High price of the day
            low_price = data.get('l', 'N/A')      # Low price of the day
            open_price = data.get('o', 'N/A')     # Open price of the day
            volume = data.get('v', 'N/A')         # Volume

            print(f"Symbol: {symbol}")
            print(f"Current Price: ${current_price}")
            print(f"High Price: ${high_price}")
            print(f"Low Price: ${low_price}")
            print(f"Open Price: ${open_price}")
            print(f"Volume: {volume}")
            print("-" * 30)
        else:
            logger.error(f"No valid data found in response: {data}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")

def fetch_crypto_data(stop_event):
    url = "https://min-api.cryptocompare.com/data/pricemulti"
    params = {
        'fsyms': 'BTC,ETH,XRP,ADA,DOT,BNB,SOL,LUNA,UNI,LTC',
        'tsyms': 'USD'
    }

    while not stop_event.is_set():
        try:
            response = requests.get(url, params=params)
            if response.status_code != 200:
                logger.error(f"Error fetching data from {url} with status code {response.status_code}")
                return
            data = response.json()
            print("\n--- Crypto Data ---")
            for crypto, price_data in data.items():
                price = price_data['USD']
                print(f"{crypto}: ${price:.2f}")
            time.sleep(1)  # Fetch data every 1 second

        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")

def clear_screen():
    # Clear the terminal screen based on the OS
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n=== Financial Data Command-Line Application ===")
    print("1. Fetch Default Stock Data")
    print("2. Fetch Crypto Data")
    print("3. Exit")
    print("==============================================")

def main():
    while True:
        clear_screen()
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Automatically fetch data for the default list of stock symbols
            for symbol in DEFAULT_STOCK_SYMBOLS:
                fetch_stock_data(symbol)
                time.sleep(1)
            input("\nPress Enter to return to the main menu...")

        elif choice == '2':
            # Run the crypto fetching in a loop until Enter is pressed
            stop_event = threading.Event()
            crypto_thread = threading.Thread(target=fetch_crypto_data, args=(stop_event,))
            crypto_thread.start()

            input("\nPress Enter to stop fetching crypto data and return to the main menu...")
            stop_event.set()  # Signal the thread to stop
            crypto_thread.join()  # Wait for the thread to finish

        elif choice == '3':
            print("Exiting...")
            time.sleep(1)
            break

        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
