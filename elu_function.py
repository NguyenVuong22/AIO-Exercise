import math
def calc_elu(x):
  if x <= 0:
    y = 0.01 * (math.exp(x)-1)
    return (y)
  else:
    y = x
    return(y)
assert round(calc_elu(1)) == 1
print (round(calc_elu(-1), 2))