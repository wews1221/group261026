def calculate_discounds(price:str, discount:str) -> str:
    final_price = float(price) * (1 - float(discount) / 100)
    return str(final_price)