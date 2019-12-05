import numpy as np

# Import Intcode Input
intcode_input = np.genfromtxt('input-1.csv',dtype=int,delimiter=',')
read_pos = 0
exit = 0
verbose = False

intcode_input[1] = 12
intcode_input[2] = 2

while exit == 0:
  if verbose:
    print('Current Intcode command set of numbers: ')
    if intcode_input[read_pos] == 99:
      print(str(intcode_input[read_pos]))
    else:
      for i in range(4):
        print(str(intcode_input[read_pos+i]) + ',')
  if intcode_input[read_pos] == 1:
    if verbose:
      print('Adding ' + str(intcode_input[intcode_input[read_pos+1]]))
      print('and ' + str(intcode_input[intcode_input[read_pos+2]]))
      print('Storing sum at position ' + str(intcode_input[read_pos+3]) + '\n')
    intcode_input[intcode_input[read_pos+3]] = intcode_input[intcode_input[read_pos+1]] + \
        intcode_input[intcode_input[read_pos+2]]
    read_pos += 4
  elif intcode_input[read_pos] == 2:
    if verbose:
      print('Multiplying ' + str(intcode_input[intcode_input[read_pos+1]]))
      print('and ' + str(intcode_input[intcode_input[read_pos+2]]))
      print('Storing product at position ' + str(intcode_input[read_pos+3]) + '\n')
    intcode_input[intcode_input[read_pos+3]] = intcode_input[intcode_input[read_pos+1]] * \
        intcode_input[intcode_input[read_pos+2]]
    read_pos += 4
  elif intcode_input[read_pos] == 99:
    exit = 1
    print('Program has completed successfully. Position 0 value is ' + \
        str(intcode_input[0]))
  else:
    exit = 2
    print(str(intcode_input[read_pos] + ' is not a valid Intcode command number!'))
