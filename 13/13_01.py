file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

earliest = int(lines[0])

buses = []
wait = []
for v in lines[1].split(','):
  if v != 'x':
    buses.append(int(v))
    wait.append(int(v) - earliest % int(v))

wait_time = min(wait)
bus = buses[wait.index(wait_time)]
print(bus * wait_time)