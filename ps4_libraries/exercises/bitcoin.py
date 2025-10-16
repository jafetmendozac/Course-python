# import sys
# import requests
# import json
# import locale

# locale.setlocale(locale.LC_ALL, 'C')


# def main():
#   try:
#     if sys.argv[1]:
#       if type(float(sys.argv[1])) == float:
#           try:
#             priceBitcoin = get_price_bitcoin()
#             formatted = formatted_currency(float(priceBitcoin)*float(sys.argv[1]))
#             return print(formatted)
#           except (requests.RequestException, KeyError):
#             print("Server error")  
#   except IndexError:
#     print("Missing command-line argument")
#     sys.exit
#   except ValueError:
#     print("Command-line argument is not a number")
#     sys.exit

# def get_price_bitcoin():
#   response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=62d22d769a86ecf004bc259e46c8ed57db52154264c8b626bdd6601e14ec15da")
#   data = response.json()
#   dataBitcoin = data["data"]
#   return dataBitcoin["priceUsd"]


# def formatted_currency(priceBitcoin):
#   return '${:,.4f}'.format(priceBitcoin)


# main()




# OPTIMIZATED

import sys
import requests


def main():
    # Validate command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Get Bitcoin price
    try:
        price_bitcoin = get_price_bitcoin()
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

    # Calculate and format total
    total_value = amount * price_bitcoin
    print(f"${total_value:,.4f}")


def get_price_bitcoin():
    """Fetch the current Bitcoin price in USD from CoinCap API."""
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=62d22d769a86ecf004bc259e46c8ed57db52154264c8b626bdd6601e14ec15da"
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # raise error if request fails
    data = response.json()
    return float(data["data"]["priceUsd"])


if __name__ == "__main__":
    main()
