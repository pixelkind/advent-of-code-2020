file = open('./input.txt', 'r')
string = file.read()
groups = string.split('\n\n')

def count_chars(s):
  answers = s.split('\n')
  chars = list(answers[0])
  for answer in answers:
    remove = []
    for char in chars:
      if char not in answer:
        remove.append(char)
    for char in remove:
      chars.remove(char)
  return len(chars)

r = 0
for group in groups:
  r += count_chars(group)

print(r)