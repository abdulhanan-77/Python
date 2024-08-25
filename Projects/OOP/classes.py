import csv

'''item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

print(type(item1))
print(type(item1_price))
print(type(item1_quantity))
print(type(item1_price_total))'''

class Item:

    pay_rate = 0.8 #Pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        #print(f"An instance created at: {name}")

        # Run validation to the recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        

print(Item.is_integer(7.0))
Item.instantiate_from_csv()
#item1 = Item("Phone", 100, 1) 
#print(item1.calculate_total_price(item1.price, item1.quantity))


#item2 = Item("Laptop", 1000, 3)
#print(item2.calculate_total_price(item2.price, item2.quantity))

#print(item1.name)
#print(item2.name)
#print(item1.price)
#print(item2.price)
#print(item1.quantity)
#print(item2.quantity)

#print(item1.calculate_total_price())
#print(item2.calculate_total_price())

#print(Item.__dict__) # All the aattributes for the class level
#print(item1.__dict__) # All the attributes for instance level

#item1.apply_discount()
#print(item1.price)

#item2.pay_rate = 0.7
#item2.apply_discount()
#print(item2.price)

#item3 = Item("Cable", 10, 5)
#item4 = Item("Mouse", 50, 5)
#item5 = Item("Keyboard", 75,5)

#print(Item.all)