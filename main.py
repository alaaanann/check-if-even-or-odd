def is_even(number):  
  if number % 2 == 0: 
    return True
  else:
   return False

def test_is_even():
  assert is_even(2) == True
  assert is_even(3) == False
  assert is_even(8) == True
  assert is_even(100) == True
  assert is_even(101) == False
  print("YOUR CODE IS CORRECT!")

test_is_even()

def is_odd(number):
  if number % 3:
    return True
  else:
    return False
    
def test_is_odd():
  assert is_odd(2) == False
  assert is_odd(3) == True
  assert is_odd(8) == False
  assert is_odd(100) == False
  assert is_odd(101) == True
  print("YOUR CODE IS CORRECT!")

test_is_even()

