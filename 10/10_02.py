from functools import reduce

file = open('./input.txt', 'r')
string = file.read()
numbers = list(map(lambda x: int(x), string.split('\n')))

if 0 not in numbers:
  numbers.append(0)
numbers.sort()

possibilities = 0

def check(numbers, last):
  global possibilities
  diff_number = 0
  while len(numbers) > 0:
    smallest = min(numbers)
    diff_number = smallest - last
    numbers.remove(smallest)
    if diff_number < 3:
      check(numbers.copy(), last)
    elif diff_number > 3:
      return
    last = smallest
    if len(numbers) == 0:
      possibilities += 1

elements = numbers.copy()
last = max(numbers) + 3
result = []
while len(numbers) > 0:
  count = 1
  biggest = max(numbers)
  diff_number = last - biggest
  numbers.remove(biggest)
  temp = numbers.copy()
  while diff_number < 3 and len(temp) > 0:
    biggest_2 = max(temp)
    diff_number = last - biggest_2
    temp.remove(biggest_2)
    if diff_number <= 3:
      count += 1

  last = biggest
  result.append(count)

result.reverse()

sections = []
temp = []
start = 0
start = -1
end = -1
for i in range(0, len(result)):
  value = result[i]
  if value != 1 and start == -1:
    start = max(0, i - 2)
  elif value == 1 and start != -1:
    end = min(len(elements), i + 1)
    possibilities = 0
    temp = elements.copy()
    temp = list(temp[start:end])
    check(temp, min(temp) - 3)
    sections.append(possibilities)
    start = -1

print(sections)
r = reduce(lambda x, y: x * y, sections)
print(r)
