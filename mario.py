from cs50 import get_int
height = get_int("Enter your pyramid height?\n")
if height >=1 and height <=8:
    for i in range(height):
        print(" "*(height -i)+("#"*(i+1)) + " " + (("#")*(i+1)) )
else:
 print("invalid #")