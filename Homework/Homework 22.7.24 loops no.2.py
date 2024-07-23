top: int = int (input("Please enter your first number"));
bottom: int = int (input("Please enter your second number"));
if top>bottom:
    for i in range (bottom, top+1):
        print(i, end = " ")
else:
    for i in range (top, bottom+1):
        print(i, end = " ")