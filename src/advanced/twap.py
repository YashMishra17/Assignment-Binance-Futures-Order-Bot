import time
from logger import setup_logger
from market_orders import place_market_order

logger = setup_logger()

def place_twap_order(symbol, side, total_quantity, intervals, delay_sec):
    chunk = total_quantity / intervals
    for i in range(intervals):
        logger.info(f"TWAP Order {i+1}/{intervals}: {chunk}")
        place_market_order(symbol, side, chunk)
        time.sleep(delay_sec)
