num1: int = int (input("Please enter your first number"));
num2: int = int (input("Please enter your second number"));
while num1 != num2:
    if num1 < num2:
        num1= num1+1
    else:
        num2 = num2 + 1
print("We just multiplied your two numbers only by addition! Isn't that clever??:")
print(num1+num2)