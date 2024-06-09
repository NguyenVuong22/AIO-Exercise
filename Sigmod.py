import math
def calc_sig(x):
  fx = 1 / (1 + math.exp(-x))
  return fx
assert round(calc_sig(3), 2) == 0.95
print(round(calc_sig(2), 2))