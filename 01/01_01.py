file = open('./input_01_01.txt', 'r')
string = file.read()
lines = string.split()
int_lines = list(map(lambda x: int(x), lines))

def checkNumber():
  r = 0
  first = int_lines.pop(0)
  for n in int_lines:
    if first + n == 2020:
      r = first * n
      break
  
  if r == 0:
    return checkNumber()
  else:
    return r

result = checkNumber()

print(result)