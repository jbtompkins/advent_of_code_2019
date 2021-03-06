# Read wire directions
with open('input-1.csv') as f:
  read_data = f.read()

# Parse Wire Location Input
wire0 = read_data.splitlines()[0].split(',')
wire1 = read_data.splitlines()[1].split(',')

wire0_pos = []
wire0_curpos = [0,0]
wire1_curpos = [0,0]

# Generate list of positions for wire0
for m in range(len(wire0)):
  for l in range(int(wire0[m][1:])):
    if wire0[m][0] == 'R':
      wire0_curpos[0] += 1
    elif wire0[m][0] == 'L':
      wire0_curpos[0] -= 1
    elif wire0[m][0] == 'U':
      wire0_curpos[1] += 1
    elif wire0[m][0] == 'D':
      wire0_curpos[1] -= 1
    else:
      print('ERROR: Invalid movement instructions encountered at ' + str(m))
    wire0_pos.append(wire0_curpos[:])

# Loop through list of wire1 positions comparing to wire0 positions and save
# matches
dups = []
dists = []

for m in range(len(wire1)):
  for l in range(int(wire1[m][1:])):
    if wire1[m][0] == 'R':
      wire1_curpos[0] += 1
    elif wire1[m][0] == 'L':
      wire1_curpos[0] -= 1
    elif wire1[m][0] == 'U':
      wire1_curpos[1] += 1
    elif wire1[m][0] == 'D':
      wire1_curpos[1] -= 1
    else:
      print('ERROR: Invalid movement instructions encountered at ' + str(m))
    if wire1_curpos in wire0_pos:
      dists.append(abs(wire1_curpos[0]) + abs(wire1_curpos[1]))
      dups.append(wire1_curpos[:])
      print('match at '+str(wire1_curpos)+' Manhattan distance is '+str(dists[-1]))

# Loop through crossing list to find closest
short_length = 1e6
short_idx = 1e6

for m in range(len(dups)):
  length = abs(dups[m][0]) + abs(dups[m][1])
  if length < short_length:
    short_length = length
    short_idx = m

print short_length
