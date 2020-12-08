# ------------
# Menu.py
# ------------
from Sandwich import Sandwich

# Class Menu
class Menu:
  def __init__(self):
    self.menu_type = "Food"
    self.menu_list = []
    self.build_menu()

  def build_menu(self):
    menu_dict = { "Club Sandwich" : 4.99, "Italian" : 10.99, "Cheese Steak" : 5.99, "Chilli Dog" : 2.99}
    print(f"---------------\n")
    for key, value in menu_dict.items():
      new_sandwich = Sandwich(key, value)
      self.menu_list.append(new_sandwich)
      print(f"{key} - ${value}")
    print(f"---------------\n")

  def remove_sandwich(self, name):
    self.menu_list.remove(name)

  def add_sandwich(self, name, price):
    new_sandwich = Sandwich(name, price)
    self.menu_list.append(new_sandwich)

if __name__ == "__main__":
  menu = Menu()
    