class ShoppingCart:
    def __init__(self):
        self.item = []

    def add_items(self, name: str, price: float, quantity:int):
        for item in self.item:
            if item['name'] == name:
                item['quantity'] += quantity
                item['price'] = price
                return

        self.item.append({
            'name' : name,
            'quantity' : quantity,
            'price' : price

        })

    def remove_items(self, name:str):
        for item in self.item:
            if item['name'] == name:
                self.item.remove(item)

