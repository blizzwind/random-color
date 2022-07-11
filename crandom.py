import random
import matplotlib
def get():
  r = random.random()
  g = random.random()
  b = random.random()
  hex = matplotlib.colors.to_hex([r,g,b])
  return hex
