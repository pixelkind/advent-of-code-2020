import collections

Instruction = collections.namedtuple('Instruction', 'name argument')

file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

def parse_lines(line):
  i = line.split(' ')
  return Instruction(i[0], int(i[1]))

instructions = []
for line in lines:
  instructions.append(parse_lines(line))

accumulator = 0
visited = []

# Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. 
# The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file.

def run(index, instructions):
  global accumulator
  if index in visited:
    return False
  if index >= len(instructions):
    return True
  instruction = instructions[index]
  visited.append(index)
  if instruction.name == 'jmp':
    index += instruction.argument
    return run(index, instructions)
  elif instruction.name == 'acc':
    accumulator += instruction.argument
    index += 1
    return run(index, instructions)
  elif instruction.name == 'nop':
    index += 1
    return run(index, instructions)

tempInstructions = instructions
startIndex = 0
running = True
change = 'nop'

while running:
  accumulator = 0
  visited = []
  oldIndex = startIndex
  startIndex = -1
  for index, item in enumerate(instructions):
    if index < oldIndex:
      continue
    if item.name == change:
      startIndex = index
      break
  if startIndex == -1 and change == 'jmp':
    running = False
  elif startIndex == -1:
    change = 'jmp'

  tempInstructions = instructions.copy()
  element = tempInstructions[startIndex]
  if element.name == 'nop':
    tempInstructions[startIndex] = Instruction('jmp', element.argument)
  elif element.name == 'jmp':
    tempInstructions[startIndex] = Instruction('nop', element.argument)

  result = run(0, tempInstructions)
  startIndex += 1

  if result:
    running = False

print(accumulator)