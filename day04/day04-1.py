def adjacent_equal_pairs_check(seq):
  it = iter(seq)
  prev = next(it)
  for item in it:


# Input Data Range
data_range = [234208,765869]

# Loop over numbers in range
for n in range(data_range[0],data_range[1]+1):
  double_digits = False
  incr_digits = False
  digits = [int(d) for d in str(num)]
  # Check conditions
  ## At least two adjacent digits must be the same
  
