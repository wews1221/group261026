class ShoppingCart:
    def __init__(self):
        self.item = []

    def add_item(self, name: str, price: float, quantity:int):
        for item in self.item:
            if item['name'] == name:
                item['quantity'] += quantity
                item['price'] = price

        self.item.append({
            'name' : name,
            'quantity' : quantity,
            'price' : price

        })

    def remove_item(self, name:str):
        for item in self.item:
            if item['name'] == name:
                self.item.remove(item)

