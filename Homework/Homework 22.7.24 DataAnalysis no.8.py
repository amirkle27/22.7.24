num: int = int (input("Please enter a number and we'll check if it's prime"));
prime: bool = (True, False)
for i in range (2, num):
    if num % num == 0 and num % 1 == 0 and not num % i == 0:
        prime = True
    else:
        prime = False
    if prime == False:
        break;
if prime == True:
    print(f"{num} is a prime number!");
else:
    print(f"{num} is not a prime number...")




