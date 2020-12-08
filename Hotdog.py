# ------------
# Hotdog.py
# ------------
from Sandwich import Sandwich

# Class Hotdog
class Hotdog(Sandwich):
  hotdog_length = 6
  is_spicy = True
  def __init__(self, name, price):
    super().__init__(name, price)
    self.ingredients = list()
  
  @classmethod
  def increase_length(cls, amount):
    cls.hotdog_length += amount

  @classmethod
  def decrease_length(cls, amount):
    cls.hotdog_length -= amount

if __name__ == "__main__":
  hotdog1 = Hotdog("Frank", 2.99)
  hotdog2 = Hotdog("Furter", 3.99)
  Hotdog.increase_length(4)
  print(hotdog1.hotdog_length)
  print(hotdog2.hotdog_length)
