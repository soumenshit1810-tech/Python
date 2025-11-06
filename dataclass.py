from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def total_price(self):
        return self.price * self.quantity

item = Product("Laptop", 65000, 2)
print(item.total_price())
