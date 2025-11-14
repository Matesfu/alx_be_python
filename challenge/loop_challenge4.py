# outer_counter = 15
# line = (outer_counter * 2) - 1
# while outer_counter >=1:
#     space= outer_counter -1
#     astrics = line - (2*space)
#     print(" " * (space) + "*"* astrics + " " * (space))
    
#     outer_counter -=1



rows = 20
current_rows = 1

while current_rows <= rows:
    spaces = 1
    while spaces <= rows - current_rows:
        print(" ", end="")
        spaces+=1
    astrics = 1
    while astrics <= (2*current_rows)-1:
        print("*",end="")
        astrics+=1
    print()
    current_rows+=1

current_rows2 = rows - 1
while current_rows2 >= 1:
    spaces = 1
    while spaces <= (rows - current_rows2):
        print(" ",end="")
        spaces +=1
    astrics = 1
    while astrics <= (current_rows2*2)-1:
        print("*",end="")
        astrics +=1
    print()
    current_rows2 -=1