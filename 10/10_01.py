file = open('./input.txt', 'r')
string = file.read()
numbers = list(map(lambda x: int(x), string.split('\n')))

# 1-3 lower than rating
internal_rating = max(numbers) + 3

last = 0
diff = [0, 0, 0]
while len(numbers) > 0:
  smallest = min(numbers)
  diff_number = smallest - last
  diff[diff_number - 1] += 1
  last = smallest
  numbers.remove(smallest)

print(diff[0] * (diff[2] + 1)) # +1 because my computer has always +3
