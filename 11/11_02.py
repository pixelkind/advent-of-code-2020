from copy import deepcopy

file = open('./input.txt', 'r')
string = file.read()
seats = list(map(lambda x: list(x), string.split('\n')))

def check_ray(x, y, step_x, step_y, seats):
  running = True
  while running:
    y += step_y
    x += step_x
    if y >= len(seats) or y < 0 or x >= len(seats[y]) or x < 0:
      return 0

    v = seats[y][x]
    if v == '#':
      return 1
    elif v == 'L':
      return 0

def calculate_state(x, y, seats):
  value = seats[y][x]
  if value == '.':
    return value
  
  occupied = 0
  occupied += check_ray(x, y, 0, -1, seats)
  occupied += check_ray(x, y, 1, -1, seats)
  occupied += check_ray(x, y, 1, 0, seats)
  occupied += check_ray(x, y, 1, 1, seats)
  occupied += check_ray(x, y, 0, 1, seats)
  occupied += check_ray(x, y, -1, 1, seats)
  occupied += check_ray(x, y, -1, 0, seats)
  occupied += check_ray(x, y, -1, -1, seats)

  if occupied == 0:
    return '#'
  elif value == '#' and occupied >= 5:
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

print('->', last_occupied)