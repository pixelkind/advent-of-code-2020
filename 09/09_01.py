file = open('./input.txt', 'r')
string = file.read()
numbers = list(map(lambda x: int(x), string.split('\n')))

preamble = 25

def calculate(numbers, number):
  while len(numbers) > 0:
    valueA = numbers.pop(0)
    for valueB in numbers:
      r = valueA + valueB
      if r == number:
        return True
  return False

for i in range(preamble, len(numbers)):
  number = numbers[i]
  temp = numbers.copy()[i-preamble:i]
  r = calculate(temp, number)
  if r == False:
    print(number)
    break