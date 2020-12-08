# ------------
# SandwichShop.py
# ------------
from Sandwich import Sandwich
from Hotdog import Hotdog
from Order import Order
from Menu import Menu

# Class SandwichShop
class SandwichShop:
  def __init__(self):
    self.orders = None

  def create_sandwich(self):
    name = input("What is the name of the sandwich? ")
    price = input("How much does the sandwich cost? ")
    return Sandwich(name, price)

  def create_hotdog(self):
    name = input("What is the name of the hotdog? ")
    price = input("How much does the sandwich cost? ")
    return Hotdog(name, price)

  def create_custom_sandwich(self):
    name = input("What is the name of your custom sandwich? ")
    price = input("How much does the sandwich cost? ")
    bread = input("What kind of bread does it have? ")
    sauce = input("What kind of sauce does it have? ")
    filling = input("what kind of filling does it have? ")
    new_custom_sandwich = Sandwich(name, price)
    new_custom_sandwich.add_ingredients(bread, sauce, filling)
    return new_custom_sandwich

  def create_menu(self):
    menu = Menu()
    return

  def create_order(self):
    order_name = input("What is your name? ")
    order = Order(order_name)
    add_item = None
    while add_item != "5":
      add_item = input("[1] Add Sandwich\n[2] Add Hotdog\n[3] Add Custom Sandwich\n[4] Open Menu\n[5] Done adding items\n\nYour choice: ")
      if add_item == "1":
        new_sandwich = self.create_sandwich()
        order.add_sandwich(new_sandwich.name, new_sandwich.price)
      if add_item == "2":
        new_hotdog = self.create_hotdog()
        order.add_sandwich(new_hotdog.name, new_hotdog.price)
      if add_item == "3":
        new_custom_sandwich = self.create_custom_sandwich()
        order.add_sandwich(new_custom_sandwich.name, new_custom_sandwich.price)
      if add_item == "4":
        self.create_menu()
      if add_item == "5":
        print(f"Finished creating Order")
        order.view_order()
    return order

  def build_orders(self):
    numOfOrders = int(input("How many orders would you like today?\n"))
    
    for order in range(numOfOrders):
      order = self.create_order()

if __name__ == "__main__":
  shop_is_running = True

  sandwichshop = SandwichShop()

  sandwichshop.build_orders()
