file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# . = open, # = tree

def calculateSlope(xStep, yStep):
  x = 0
  trees = 0
  for y in range(yStep, len(lines), yStep):
    x += xStep
    line = lines[y]
    char = line[x % len(line)]
    if char == '#':
      trees += 1

  return trees

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
r = 1
for s in slopes:
  t = calculateSlope(s[0], s[1])
  r *= t

print(r)