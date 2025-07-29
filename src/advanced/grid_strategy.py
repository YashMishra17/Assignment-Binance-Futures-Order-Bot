from market_orders import place_market_order
import time
from logger import setup_logger

logger = setup_logger()

def run_grid_strategy(symbol, side, quantity, lower_bound, upper_bound, steps, interval_sec):
    price_range = upper_bound - lower_bound
    step_size = price_range / steps
    prices = [lower_bound + i * step_size for i in range(steps + 1)]

    for price in prices:
        logger.info(f"Placing simulated order at grid price: {price}")
        place_market_order(symbol, side, quantity)
        time.sleep(interval_sec)
