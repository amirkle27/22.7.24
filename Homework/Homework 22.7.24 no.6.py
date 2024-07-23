num: float = float (input("enter a number"))
num1 = num / 100
num2 = num // 100
ans: int = int (10* (num1 - num2))
print (f"The second digit from the right is {ans}")