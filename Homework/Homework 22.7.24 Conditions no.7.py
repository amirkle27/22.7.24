num: int = int(input("Enter a two digits number number"));
left_d = num // 10
right_d = num % 10
sum = (left_d+right_d)
print (f"As you first entered the number {num}, the sum of the digits of your number is {sum}")
