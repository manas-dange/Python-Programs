class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name]['quantity'] <= quantity:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity

    def total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items.values())

    def __str__(self):
        cart_content = '\n'.join([f"{item}: {details['quantity']} @ {details['price']} each" for item, details in self.items.items()])
        return f"Shopping Cart:\n{cart_content}\nTotal Price: {self.total_price()}"

cart = ShoppingCart()
cart.add_item("Apple", 1.5, 3)
cart.add_item("Banana", 0.5, 6)
cart.add_item("Orange", 2.0, 4)
print(cart)
cart.remove_item("Banana", 2)
print(cart)

