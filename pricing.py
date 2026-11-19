def total_price(unit_price, quantity):
    """Return the price of exactly quantity items."""
    return unit_price * max(quantity, 1)
