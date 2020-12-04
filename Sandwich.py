# ------------
# Sandwich.py
# ------------

# Class Sandwich
class Sandwich():
  def __init__(self, name):
    self.name = name
    self.price = 0.00
    self.ingredients = list()

  def add_ingredients(self, bread, sauce, filling):
    self.ingredients.extend([bread, sauce, filling])

  def remove_ingredient(self, name):
    self.ingredients.remove(name)

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  sandwich = Sandwich("Meatball")
  sandwich.add_ingredients("French", "Marinara", "Meatballs")
  print(sandwich.ingredients)
  sandwich.remove_ingredient("Meatballs")
  print(sandwich.ingredients)
  