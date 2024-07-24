num1: int = int (input ("Please enter your first number"));
num2: int = int (input ("Please enter your second number"));
common_div: int = 0
for i in range (1, num1+1):
    if num1 % i == 0 and num2 % i == 0:
        common_div = i
print (common_div)

