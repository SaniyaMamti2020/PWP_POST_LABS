class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")

    def apply_discount(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        self.price -= discount_amount


# Create two books
book1 = Book("Python Programming", "John Smith", 500)
book2 = Book("Data Structures", "Alice Brown", 700)

print("Book 1 details:")
book1.display_details()

print("\nBook 2 details:")
book2.display_details()
print("\n3EK3_16_Saniya_Mamti")

# Apply 10% discount to book2
print("\nApplying 10% discount to Book 2...\n")
book2.apply_discount(10)

print("Updated Book 2 details after discount:")
book2.display_details()
print("\n3EK3_16_Saniya_Mamti")