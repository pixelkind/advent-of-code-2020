import collections

Instruction = collections.namedtuple('Instruction', 'name argument')

file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

# acc increase accumulator
# jmp jumps to relative instruction
# nop No Operation

# acc -99
# nop +0
# jmp +4

def parse_lines(line):
  i = line.split(' ')
  return Instruction(i[0], int(i[1]))

instructions = []
for line in lines:
  instructions.append(parse_lines(line))

accumulator = 0
visited = []

def run(index):
  global accumulator
  if index in visited:
    return
  instruction = instructions[index]
  visited.append(index)
  if instruction.name == 'jmp':
    index += instruction.argument
    run(index)
  elif instruction.name == 'acc':
    accumulator += instruction.argument
    index += 1
    run(index)
  elif instruction.name == 'nop':
    index += 1
    run(index)

run(0)

print(accumulator)