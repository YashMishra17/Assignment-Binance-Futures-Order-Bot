def validate_order_input(symbol, side, quantity, price=None):
    assert side.upper() in ("BUY", "SELL"), "Side must be BUY or SELL"
    assert quantity > 0, "Quantity must be greater than 0"
    if price is not None:
        assert price > 0, "Price must be greater than 0"
