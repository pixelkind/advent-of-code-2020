file = open('./input.txt', 'r')
string = file.read()
groups = string.split('\n\n')

def count_chars(s):
  s = s.replace('\n', '')
  chars = []
  for char in s:
    if char not in chars:
      chars.append(char)
  return len(chars)

r = 0
for group in groups:
  r += count_chars(group)

print(r)