import collections

Password = collections.namedtuple('Password', 'value letter range_min range_max')

file = open('./input_02.txt', 'r')
string = file.read()
lines = string.split('\n')

def split_rules(s):
  # 1-3 a: abcde
  a = s.split(': ')
  rule = a[0].split(' ')
  password = a[1]
  letter = rule[1]
  range_values = rule[0].split('-')
  range_min = int(range_values[0])
  range_max = int(range_values[1])
  return Password(password, letter, range_min, range_max)


passwords = list(map(split_rules, lines))

def filter_passwords(password):
  c = password.value.count(password.letter)
  r = range(password.range_min, password.range_max + 1)
  return c in r

filtered_passwords = list(filter(filter_passwords, passwords))

print(len(filtered_passwords))