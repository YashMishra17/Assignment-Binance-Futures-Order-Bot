from binance.client import Client
import os
from dotenv import load_dotenv
from logger import setup_logger

logger = setup_logger()
load_dotenv()

client = Client(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET_KEY"))

def place_stop_limit(symbol, side, quantity, stop_price, limit_price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="STOP_MARKET",
            stopPrice=stop_price,
            quantity=quantity,
            timeInForce="GTC"
        )
        logger.info(f"Stop-Limit Order Placed: {order}")
    except Exception as e:
        logger.error(f"Stop-Limit Order Failed: {e}")
