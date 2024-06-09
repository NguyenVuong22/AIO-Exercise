# calculate approx. cos(x)
def factorial (n):
  giaithua = 1
  for i in range(1, n+1):
    giaithua = giaithua * i
  return(giaithua)
def approx_cos(x, n):
  total = 0
  for i in range(n+1):
    total = total + ((-1)**i )* (x**(2*i))/factorial(2*i)
  return(total)
assert round(approx_cos(x = 1, n = 10), 2) == 0.54
print(round(approx_cos(x = 3.14, n = 10), 2))

# calcute approx.sin(x)
def factorial (n):
  giaithua = 1
  for i in range(1, n+1):
    giaithua = giaithua * i
  return(giaithua)
def approx_sin(x, n):
  total = 0
  for i in range(n+1):
      total = total + ((-1)**i )* (x**(2*i + 1))/factorial(2*i +1)
  return(total)


assert round(approx_sin(x = 1, n = 10), 4) == 0.8415
print(round(approx_sin(x = 3.14, n = 10), 4))

# calcute approx. sinh(x)
def factorial (n):
  giaithua = 1
  for i in range(1, n+1):
    giaithua = giaithua * i
  return(giaithua)

def approx_sinh(x, n):
  total = 0
  for i in range(n+1):
      total = total +  (x**(2*i + 1))/factorial(2*i +1)
  return(total)

assert round(approx_sinh(x= 1, n=10), 2) == 1.18
print(round(approx_sinh(x = 3.14, n=10), 2))

# calcute approx. cosh(x)

def factorial (n):
  giaithua = 1
  for i in range(1, n+1):
    giaithua = giaithua * i
  return(giaithua)

def approx_cosh(x, n):
  total = 0
  for i in range(n+1):
      total = total +  (x**(2*i ))/factorial(2*i)
  return(total)

assert round(approx_cosh(x=1, n=10), 2)==1.54
print(round(approx_cosh(x=3.14, n=10), 2))