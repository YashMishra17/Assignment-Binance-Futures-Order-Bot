from binance.client import Client
import os
from dotenv import load_dotenv
from logger import setup_logger

logger = setup_logger()
load_dotenv()

client = Client(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET_KEY"))

def place_oco_order(symbol, quantity, take_profit_price, stop_price, stop_limit_price):
    try:
        order = client.create_oco_order(
            symbol=symbol,
            side="SELL",
            quantity=quantity,
            price=take_profit_price,
            stopPrice=stop_price,
            stopLimitPrice=stop_limit_price,
            stopLimitTimeInForce="GTC"
        )
        logger.info(f"OCO Order Placed: {order}")
    except Exception as e:
        logger.error(f"OCO Order Failed: {e}")
