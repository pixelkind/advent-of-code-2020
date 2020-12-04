import re

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

def parse_passport(pass_string):
  pass_string = pass_string.replace('\n', ' ')
  pass_elements = pass_string.split(' ')
  passport = {}
  for element in pass_elements:
    kv = element.split(':')
    passport[kv[0]] = kv[1]
  return passport

passports = []
for line in r:
  passports.append(parse_passport(line))

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def check_height(height_string):
  if len(height_string) <= 2:
    return False
  height = int(height_string[:-2])
  if 'cm' in height_string:
    return height in range(150, 193 + 1)
  elif 'in' in height_string:
    return height in range(59, 76 + 1)
  else:
    return False

eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_eye_color(eye_color):
  return eye_color in eye_colors


hcl = re.compile('^#[0-9a-f]{6}$', re.IGNORECASE)
pid = re.compile('[0-9]{9}$')

def contains_required_valid_fields(passport):
  # print(int(passport['byr']) in range(1920, 2002 + 1),int(passport['iyr']) in range(2010, 2020 + 1),int(passport['eyr']) in range(2020, 2030 + 1),check_height(passport['hgt']),hcl.match(passport['hcl']) != None,check_eye_color(passport['ecl']),pid.match(passport['pid']) != None)
  return (
    int(passport['byr']) in range(1920, 2002 + 1) and
    int(passport['iyr']) in range(2010, 2020 + 1) and
    int(passport['eyr']) in range(2020, 2030 + 1) and
    check_height(passport['hgt']) and
    hcl.match(passport['hcl']) != None and
    check_eye_color(passport['ecl']) and
    pid.match(passport['pid']) != None
  )

r = list(filter(contains_required_valid_fields, passports))
print(len(r))

# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm