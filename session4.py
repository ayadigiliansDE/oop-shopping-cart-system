from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name: str, price: float, description: str):
        if price < 0:
            raise ValueError("Price cannot be negative")

        self._name = name
        self._price = price
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @abstractmethod
    def get_description(self):
        pass


class Electronics(Product):
    def get_description(self):
        return f"Electronics: {self._description}"


class Clothing(Product):
    def get_description(self):
        return f"Clothing: {self._description}"


class Book(Product):
    def get_description(self):
        return f"Book: {self._description}"


class ShoppingCart:
    def __init__(self):
        self._products = []

    def add_product(self, product: Product):
        self._products.append(product)

    def remove_product(self, product: Product):
        if product in self._products:
            self._products.remove(product)

    def calculate_total(self):
        return sum(product.price for product in self._products)

    def save_to_file(self, filename="cart.txt"):
        with open(filename, "w", encoding="utf-8") as file:
            for product in self._products:
                file.write(f"{product.name}: {product.price}\n")

    def __len__(self):
        return len(self._products)

    def __str__(self):
        return "\n".join(
            f"{product.name}: {product.price}"
            for product in self._products
        )


if __name__ == "__main__" :
    card =  ShoppingCart()
    keyboard = Electronics("keyboard", 500, "acsessories")
    dress = Clothing("dress", 1400, "hegab clothing")
    atomic_habits = Book("atomic_habits", 100, "(inspiring- motivation) book ")
    card.add_product(keyboard)
    card.add_product(dress)
    card.add_product(atomic_habits)
    print("card items :")
    print(card)
    print(card.calculate_total())
    print("number of items :" , len(card))
    card.save_to_file("card.txt")
    
    
