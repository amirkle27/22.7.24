num: int = int(input("Enter a number"));
num1 = num // 10
num2 = float ((num/100)*10)
num3 = int (10*(num2-num1))
num2 = int (num2 //1)
print (f"As you first entered the number {num}, your new number is {num3}{num2}")