import collections

Action = collections.namedtuple('Action', 'action value')

file = open('./input.txt', 'r')
string = file.read()
actions = list(map(lambda x: Action(x[:1], int(x[1:])), string.split('\n')))

# The ship starts by facing east.

x = 0
y = 0
direction = 0 # east

def move(action):
  global x
  global y
  global direction

  if action.action == 'N':
    y -= action.value
  elif action.action == 'S':
    y += action.value
  elif action.action == 'E':
    x += action.value
  elif action.action == 'W':
    x -= action.value
  elif action.action == 'L':
    direction -= action.value / 90
  elif action.action == 'R':
    direction += action.value / 90
  elif action.action == 'F':
    if direction == 0:
      x += action.value
    elif direction == 1:
      y += action.value
    elif direction == 2:
      x -= action.value
    elif direction == 3:
      y -= action.value
  direction = direction % 4

for action in actions:
  move(action)
  # print(x, y, direction)

print(abs(x) + abs(y))