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
      inner_bags.append({ 'name': bag_color, 'amount': nr })
  rules[outer_bag] = inner_bags

for line in lines:
  parse_rule(line)

def contains(bag):
  nr = 0
  for x in rules[bag]:
    nr += x['amount']
    nr += x['amount'] * contains(x['name'])
  return nr


print(contains('shiny gold'))

# shiny gold bag
