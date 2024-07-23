num1: int = int (input("Please enter your first number"));
num2: int = int (input("Please enter your second number"));
ans = num1
for i in range (1, num2):
    num1 = num1 * ans
print(num1)


