import math
def calc_activation_func(x, act_name):
  if act_name == 'sigmoid':
    fx = 1 / (1 + math.exp(-x))
    return fx
  if act_name == 'relu' and x <= 0:
    fx = 0
    return fx
  if act_name == 'relu' and x > 0:
    fx = x
    return fx
  if act_name == 'elu' and x <= 0:
    fx = 0.01 * (math.exp(x)-1)
    return fx
  if act_name == 'elu' and x > 0:
    fx = x
    return fx
assert calc_activation_func(x = 1, act_name = 'relu') == 1
print(round(calc_activation_func(x = 3, act_name = 'sigmoid'), 2))