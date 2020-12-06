# ------------
# Order.py
# ------------
from Sandwich import Sandwich

# Class Order
class Order:
  def __init__(self, order_name = "Guest"):
    self.order_name = order_name
    self.sandwiches = list()

  def view_order(self):
    for sandwich in self.sandwiches:
      print(sandwich.name)

  def remove_sandwich(self, name):
    self.sandwiches.remove(name)

  def add_sandwich(self, sandwich):
    self.sandwiches.append(sandwich)

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  order = Order("Matthew")
  sandwich = Sandwich("Meatball", 6.99)
  sandwich.add_ingredients("French", "Marinara", "Meatballs")
  print(sandwich.ingredients)
  order.add_sandwich(sandwich)
  order.view_order()
  print(order.order_name)
  print(order.sandwiches)
  order.remove_sandwich(sandwich)
