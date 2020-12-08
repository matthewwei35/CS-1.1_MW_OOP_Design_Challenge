# ------------
# Sandwich.py
# ------------

# Class Sandwich
class Sandwich:
  served_hot = True
  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.ingredients = list()

  def add_ingredients(self, bread, sauce, filling):
    self.ingredients.extend([bread, sauce, filling])

  def remove_ingredient(self, name):
    self.ingredients.remove(name)

  @classmethod
  def serve_cold(cls):
    if cls.served_hot == True:
      cls.served_hot = False
      print("Sandwiches are on their way cold!")
    else:
      print("Sandwiches are already being served cold.")

  @classmethod
  def serve_hot(cls):
    if cls.served_hot == False:
      cls.served_hot = True
      print("Sandwiches are on their way hot!")
    else:
      print("Sandwiches are already being served hot.")

if __name__ == "__main__":
  sandwich1 = Sandwich("Meatball", 6.99)
  sandwich2 = Sandwich("Roastbeef", 7.99)
  sandwich1.add_ingredients("French", "Marinara", "Meatballs")
  sandwich2.add_ingredients("French", "Cheese", "Roast Beef")
  print(sandwich1.ingredients)
  sandwich1.remove_ingredient("Meatballs")
  print(sandwich1.ingredients)

  Sandwich.serve_cold()
  Sandwich.serve_cold()
  Sandwich.serve_hot()
  Sandwich.serve_hot()
  