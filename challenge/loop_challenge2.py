outer_count = 5

while outer_count > 0:
  # Outer loop controls the number of times the inner loop runs
  inner_count = 1
  while inner_count <= outer_count:
    # Inner loop repeats for each outer loop iteration
    print(inner_count, end=" ")
    inner_count += 1
  print()  # Move to a new line after each outer loop iteration
  outer_count -= 1




outer_count = 1

while outer_count < 6:
  # Outer loop controls the number of times the inner loop runs
  inner_count = 1
  while inner_count <= outer_count:
    # Inner loop repeats for each outer loop iteration
    print(inner_count, end=" ")
    inner_count += 1
  print()  # Move to a new line after each outer loop iteration
  outer_count += 1



outer_count = 5

while outer_count > 0:
    inner_count = 1
    
    # Print left side numbers
    while inner_count <= outer_count:
        print(inner_count, end=" ")
        inner_count += 1

    # Print right side numbers (reverse)
    right_count = outer_count
    while right_count >= 1:
        print(right_count, end=" ")
        right_count -= 1

    print()  # Move to next line
    outer_count -= 1
