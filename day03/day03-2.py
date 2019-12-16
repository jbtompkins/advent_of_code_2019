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
wire0_pos.append(wire0_curpos[:])

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
wire0_step = 0
wire1_step = 0
wire0_x_steps = []
wire1_x_steps = []

for m in range(len(wire1)):
  for l in range(int(wire1[m][1:])):
    wire1_step += 1
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
    # Check if wire1 position is in wire0 list of positions
    cross_check = [i for i, j in enumerate(wire0_pos) if j == wire1_curpos]
    if len(cross_check) > 0:
      wire0_x_steps.append(cross_check[0])
      wire1_x_steps.append(wire1_step)
      total_steps = cross_check[0] + wire1_step
      print('Match at '+str(wire1_curpos)+'. Total Steps are '+str(total_steps))
