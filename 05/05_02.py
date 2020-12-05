file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

def calculacte(start, row_string):
  result = 0
  row = start
  for char in row_string:
    row /= 2
    if char == 'B' or char == 'R':
      result += row
  return result

seat_ids = []

for l in lines:
  row = calculacte(128, l[:-3])
  seat = calculacte(8, l[7:])
  seat_id = row * 8 + seat
  seat_ids.append(seat_id)

# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

seat_ids.sort()

current_id = -1
for i in seat_ids:
  if current_id == -1:
    current_id = i
    continue
  if i == current_id + 1:
    current_id = i
  else:
    print(current_id + 1)
    break