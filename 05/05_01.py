file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

# first 7 characters will either be F or B
# Each letter tells you which half of a region the given seat is in
# F = front, B = back

def calculacte(start, row_string):
  result = 0
  row = start
  for char in row_string:
    row /= 2
    if char == 'B' or char == 'R':
      result += row
    # print(char, row, result)
  return result

# last three characters will be either L or R
# L means to keep the lower half, while R means to keep the upper half

# unique seat ID: multiply the row by 8, then add the column

seat_ids = []

for l in lines:
  row = calculacte(128, l[:-3])
  seat = calculacte(8, l[7:])
  seat_id = row * 8 + seat
  seat_ids.append(seat_id)
  # print(row, seat, seat_id)

print(max(seat_ids))