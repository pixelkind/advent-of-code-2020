file = open('./input_01_01.txt', 'r')
string = file.read()
lines = string.split()
input_numbers = list(map(lambda x: int(x), lines))

def checkNumber():
  r = 0
  first = input_numbers.pop(0)
  for second in input_numbers:
    temp_input_numbers = input_numbers.copy()
    temp_input_numbers.remove(second)
    for third in temp_input_numbers:
      if first + second + third == 2020:
        r = first * second * third
        break
  
  if r == 0:
    return checkNumber()
  else:
    return r

result = checkNumber()

print(result)