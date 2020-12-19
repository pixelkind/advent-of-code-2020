file = open('./input.txt', 'r')
string = file.read()
numbers = list(map(lambda x: int(x), string.split('\n')))

invalid_number = 104054607
# invalid_number = 127
final_list = []

def calculate(numbers):
  global invalid_number
  global final_list
  result = 0
  result_list = []
  for value in numbers:
    result += value
    result_list.append(value)
    if result == invalid_number:
      final_list = result_list
      return True
  return False


r = False
index = 0
while r == False:
  temp = numbers.copy()[index:]
  r = calculate(temp)
  index += 1
  if index >= len(numbers):
    break

smallest = min(final_list)
largest = max(final_list)
# print(final_list)
print(smallest + largest)
