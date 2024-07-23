salary: int = int (input("What's your salary, Sir?"))
tax: float = None
if salary <= 6000:
    tax = 0
    per_cent = "0%"
elif  12000 >= salary > 6000 :
    tax = salary * 0.1
    per_cent = "10%"
elif 18000 >= salary > 12000:
    tax = salary * 0.2
    per_cent = "20%"
elif 25000 >= salary > 18000:
    tax = salary * 0.3
    per_cent = "30%"
elif 35000 >= salary > 25000:
    tax = salary * 0.4
    per_cent = "40%"
elif 50000 >= salary > 35000:
    tax = salary * 0.45
    per_cent = "45%"
elif salary > 50000:
    tax = salary * 0.51
    per_cent = "51%"
print (f"Dear Sir, according to our records, you need to pay {tax} Shequel tax, which is {per_cent} of your salary")
