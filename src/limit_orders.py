import sys
import os
from binance.client import Client
from dotenv import load_dotenv
from logger import setup_logger
from validate import validate_order_input

logger = setup_logger()
load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET_KEY")
client = Client(api_key, api_secret)

def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
        logger.info(f"Limit Order Executed: {order}")
    except Exception as e:
        logger.error(f"Limit Order Failed: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python limit_orders.py SYMBOL SIDE QUANTITY PRICE")
        sys.exit(1)
    symbol, side, quantity, price = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
    validate_order_input(symbol, side, quantity, price)
    place_limit_order(symbol, side, quantity, price)
