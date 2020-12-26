import collections

Action = collections.namedtuple('Action', 'action value')

file = open('./input.txt', 'r')
string = file.read()
actions = list(map(lambda x: Action(x[:1], int(x[1:])), string.split('\n')))

wx = 10
wy = -1
x = 0
y = 0

def move(action):
  global wx
  global wy
  global x
  global y

  if action.action == 'N':
    wy -= action.value
  elif action.action == 'S':
    wy += action.value
  elif action.action == 'E':
    wx += action.value
  elif action.action == 'W':
    wx -= action.value
  elif action.action == 'L':
    direction = int(action.value / 90)
    for _ in range(direction):
      tx = wx
      ty = wy
      wx = ty
      wy = -1 * tx

  elif action.action == 'R':
    direction = int(action.value / 90)
    for _ in range(direction):
      tx = wx
      ty = wy
      wx = -1 * ty
      wy = tx
  
  elif action.action == 'F':
    x += wx * action.value
    y += wy * action.value

for action in actions:
  move(action)
  # print(x, y, wx, wy)

print(abs(x) + abs(y))