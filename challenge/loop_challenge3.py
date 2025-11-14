outer_counter= 1
lines = 50
spaces = (lines * 2) - 1
stars = 1

while outer_counter <=  lines:
    print(" " * (spaces // 2) + "*" * stars + " " * (spaces // 2)) 
    stars += 2
    spaces -= 2
    outer_counter += 1
  