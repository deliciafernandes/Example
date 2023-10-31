def calculate_item_price(item):
    if item.quantity <= 0:
        return 0
    if item.price > 100:
        return item.price * 0.9 * item.quantity
    return item.price * item.quantity

def calculate_total_price(items):
    return sum(calculate_item_price(item) for item in items)
