min: float = None;
num: float = float(input("Hello, please enter a decimal number"));
num1: float = float(input("Hello, please enter another decimal numbers"));
(min := num if num < num1 else (min := num1));
for j in range (3):
    print (min)
