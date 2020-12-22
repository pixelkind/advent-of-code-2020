from copy import deepcopy

file = open('./input.txt', 'r')
string = file.read()
seats = list(map(lambda x: list(x), string.split('\n')))

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

def calculate_state(x, y, seats):
  value = seats[y][x]
  if value == '.':
    return value
  
  start_x = max(0, x - 1)
  start_y = max(0, y - 1)
  end_x = min(len(seats[y]), x + 2)
  end_y = min(len(seats), y + 2)

  values = []
  for i in range(start_y, end_y):
    cells = seats[i][start_x:end_x]
    values.extend(cells)
  
  values.remove(value)
  occupied = values.count('#')
  if occupied == 0:
    return '#'
  elif value == '#' and occupied >= 4:
    return 'L'
  else:
    return value

def simulate_round(seats):
  temp_seats = deepcopy(seats)
  for y in range(len(temp_seats)):
    for x in range(len(temp_seats[y])):
      temp_seats[y][x] = calculate_state(x, y, seats)
  return temp_seats

last_occupied = 0
running = True
while running:
  seats = simulate_round(seats)
  # print('\n'.join(map(str, seats)))
  currently_occupied = ''.join(map(str, seats)).count('#')
  if currently_occupied == last_occupied:
    running = False
  else:
    last_occupied = currently_occupied

print(last_occupied)