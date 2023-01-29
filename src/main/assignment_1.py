import numpy as np
from math import trunc
from decimal import Decimal
#expected output
# 3 prints 

def double_precision(floatingNumber):
  # Use double precision, calculate the resulting values (format to 5 decimal places)
  #0 10000000111 111010111001 000000000000000000000000000000
  # 0 10000000111 111010111001 
 
  s: int = int(input[0])
  exponent: str = input[1:12]
  c: int = int(exponent,2)
  
  #automate f 
  mantisa: str = input[12:]
  i = 12
  f: float = 0
  while(i < len(input)):
    if(input[i] == '1'):
      f += 1 * pow(1/2, i - 11)
    i+=1

  #f: float = (1 * pow(1/2,1)) + (1 * pow(1/2,2)) + (1 * pow(1/2,3)) + (1 * pow(1/2, 5))+ (1 * pow(1/2, 7)) + (1 * pow(1/2, 8)) + (1 * pow(1/2, 9)) +(1 * pow(1/2, 12))
  precision: float = pow(-1, s) * pow(2, c-1023) * (1 + f)
  return round(precision, 5)

#change to normalise form 
#add 5 in i+1 digit
#bring it back
def rounding_value(number: float, value: float):
  count: int = 0
  if(int(number) > 0):
    while(int(number) > 0):
      number/=10
      count +=1 
  else:
    while(int(number) <= 0):
      number *= 10
      count -= 1 
  
  add_5: float = 5 * pow(10, (value + 1) * -1)
  new_number: float = add_5 + number
  new_number = round(new_number, value) 
  return new_number * pow(10, count)

#change to normalise form 
#round
#bring it back
def chopping_value(number: float, value: float):
  count: int = 0
  if(int(number) > 0):
    while(int(number) > 0):
      number/=10
      count +=1 
  
  new_number: float = trunc(number * pow(10, value)) / pow(10, value)
  return new_number * pow(10, count)

def absolute_error(precise:float, approximate: float):
  sub_operation = precise - approximate
  return abs(sub_operation)
  
def relative_error(precise:float, approximate: float):
  if precise != 0:
    return abs(Decimal(precise) - Decimal(approximate)) / abs(Decimal(precise))

def four_rounding(floatingNumber):
  #---------- 3 digit rounding ----------
  s: int = int(input[0])
  exponent: str = input[1:12]
  c: int = int(exponent,2)
  
  mantisa: str = input[12:]
  i = 12
  f: float = 0
  while(i < len(input)):
    if(input[i] == '1'):
      f += 1 * pow(1/2, i - 11)
    i+=1

  f = rounding_value(f, 3)
  #f: float = (1 * pow(1/2,1)) + (1 * pow(1/2,2)) + (1 * pow(1/2,3)) + (1 * pow(1/2, 5))+ (1 * pow(1/2, 7)) + (1 * pow(1/2, 8)) + (1 * pow(1/2, 9)) +(1 * pow(1/2, 12))
  approximate: float = pow(-1, s) * pow(2, c-1023) * (1 + f)
  return rounding_value(approximate, 3)

def check_for_negative_1_exponent_term(function: str) -> bool:
  if "-1**k" in function:
    return True
  return False

def check_for_alternating(function_we_got: str):
  term_check = check_for_negative_1_exponent_term(function_we_got)
  return term_check

def check_for_decreasing(function_we_got: str, x: int):
  decreasing_check = True
  k = 1
  starting_val = abs(eval(function_we_got))
  for k in range(2, x):
    result = abs(eval(function_we_got))
    #print(result)
    if starting_val <= result:
      decreasing_check = False
  return decreasing_check

def minTerms(x):
  min_terms = 0
  while ((min_terms + 1) <= 10**(-1 * x / 3)):
    min_terms += 1
  
  return min_terms


#---- question 6 ---- 
FUNCTION = "x ** 3 + 4 * (x ** 2) - 10"
DERIVATIVE = "3 * (x ** 2) + 8 * x"

def calc_fx(x, f):
  return eval(f)

def bisection_method(a, b):
  iteration: int = 0
  error = 1e-4
  max_iterations = 100
  while b - a > error and iteration < max_iterations:
    iteration += 1
    mid = (b + a) / 2
    if calc_fx(mid, FUNCTION) < 0:
      b = mid
    else:
      a = mid

  return iteration

def newton_raphson_method(p0):
  error = 1e-4
  p_prev = p0
  iteration: int = 0
  max_iterations = 100
  while iteration < max_iterations:
    iteration += 1
    f_prime = calc_fx(p_prev, DERIVATIVE)

    if (f_prime != 0):
      p_next = p_prev - calc_fx(p_prev, FUNCTION) / calc_fx(p_prev, DERIVATIVE)
      if abs(p_next - p_prev) < error:
        return iteration
      p_prev = p_next
    else:
      return -1

  return iteration

if __name__ == "__main__":
  input: str = '010000000111111010111001'
  print("%.4f" % (double_precision(str)), '\n')
  print("%.1f" % (chopping_value(double_precision(str), 3)), '\n')
  print("%.1f" % (rounding_value(double_precision(str), 3)), '\n')
  
  #question 4, 2 answers, from rounding
  print(absolute_error(double_precision(str), four_rounding(str)))
  print(relative_error(double_precision(str), four_rounding(str)))

  print()

  #---------- question 5 ----------
  function_a: str = "(-1**k) * (x**k) / (k**3)"
  error = -4
  x: int = 1
  check1: bool = check_for_alternating(function_a)
  check2: bool = check_for_decreasing(function_a, x)
  if check1 and check2:
    print(minTerms(-4))
  
  print()

  #---------- question 6 ----------
  print(bisection_method(-4, 7))
  print()
  print(newton_raphson_method(7))