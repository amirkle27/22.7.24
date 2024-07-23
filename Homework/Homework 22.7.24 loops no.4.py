max: int = int (input("Please enter a second number"));
den: int = int (input("Please enter a number"));
for i in range (1, max+1):
    if i%den==0:
        print(i, end = " ")