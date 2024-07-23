num: int = int(input("Enter a number"));
num1 = num // 10
num2 = float ((num/100)*10)
num3 = (10*(num2-num1))
ans = (num1+num3)
print (f"As you first entered the number {num}, the sum of the digits of your number is {ans:.0f}")
