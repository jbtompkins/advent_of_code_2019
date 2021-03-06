#def adjacent_equal_pairs_check(seq):
def adjacent_pairs(seq):
  it = iter(seq)
  prev = next(it)
  for item in it:
    yield (prev, item)
    prev = item

def adjacent_equal_pairs_check(seq):
  equal_pairs = False
  pairs_list = list(adjacent_pairs(seq))
  for pair in pairs_list:
    equal_pairs = equal_pairs or (pair[0] == pair[1])
  return equal_pairs

def increasing_digits(seq):
  incr_digs = True
  pairs_idx = 0
  decr_idx = 10 # An arbitrary number higher than the number of digits
  pairs_list = list(adjacent_pairs(seq))
  while pairs_idx < len(pairs_list) and incr_digs == True:
    curr_pair_incr = not(pairs_list[pairs_idx][0] > pairs_list[pairs_idx][1]) 
    if curr_pair_incr == False:
      decr_idx = pairs_idx
    incr_digs = incr_digs and curr_pair_incr
    pairs_idx += 1
  return decr_idx, incr_digs
  
verbose = True

# Input Data Range
data_range = [234208,765869]

# Initialize valid password counter
pot_passes = 0

# Loop over numbers in range
cur_num = data_range[0]

s = [1,2,2,4]

## Use a while loop to check that the current number meets requirements and
## advance to next number
while cur_num <= data_range[1]:
  # Reset values for current loop
  double_digits = False
  incr_digits = False
  if verbose:
    print cur_num
  digits = [int(d) for d in str(cur_num)]
  # Check conditions
  ## At least two adjacent digits must be the same
  double_digits = adjacent_equal_pairs_check(digits)
  ## All subsequent digits must increase
  decr_idx, incr_digits = increasing_digits(digits)
  ## Both conditions must be met to store number
  if double_digits and incr_digits:
    if verbose:
      print('Found a match!')
    pot_passes += 1
    cur_num += 1
  elif double_digits and not(incr_digits):
    cur_num += 10**(4-decr_idx)
  else:
    cur_num += 1

print(pot_passes)
