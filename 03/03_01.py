file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

# right 3, down 1
# . = open, # = tree

x = 0
trees = 0
for y in range(1, len(lines)):
  x += 3
  line = lines[y]
  char = line[x % len(line)]
  if char == '#':
    trees += 1

print(trees)