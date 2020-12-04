# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

# sequence of key:value pairs separated by spaces or newlines

# Passports are separated by blank lines

file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n\n')

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def contains_required_fields(s):
  contains = True
  for r in required:
    if r not in s:
      contains = False
      break
  return contains

r = list(filter(contains_required_fields, lines))
print(len(r))
