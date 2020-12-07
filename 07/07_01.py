file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

rules = {}

def parse_rule(s):
  rule = s.split(' contain ')
  outer_bag = rule[0].replace(' bags', '')
  contained_bags = rule[1][:-1]
  inner_bags = []
  if contained_bags != 'no other bags':
    bags = contained_bags.split(', ')
    for bag in bags:
      nr = int(bag[:1])
      bag_color = bag[2:].replace(' bags', '').replace(' bag', '')
      inner_bags.append({ bag_color: nr })
  rules[outer_bag] = inner_bags
  return { outer_bag: inner_bags }

bags = []
for line in lines:
  bags.append(parse_rule(line))

possible_bags = []

def can_contain(rule, bag):
  inner_bags = list(map(lambda x: list(x.keys())[0], rules[rule]))
  if bag in inner_bags:
    return True
  else:
    for x in inner_bags:
      if can_contain(x, bag):
        return True

for rule in rules.keys():
  if can_contain(rule, 'shiny gold'):
    possible_bags.append(rule)

print(len(possible_bags))

# shiny gold bag
