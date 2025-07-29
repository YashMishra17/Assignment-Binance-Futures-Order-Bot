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

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )
        logger.info(f"Market Order Executed: {order}")
    except Exception as e:
        logger.error(f"Market Order Failed: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python market_orders.py SYMBOL SIDE QUANTITY")
        sys.exit(1)
    symbol, side, quantity = sys.argv[1], sys.argv[2], float(sys.argv[3])
    validate_order_input(symbol, side, quantity)
    place_market_order(symbol, side, quantity)
