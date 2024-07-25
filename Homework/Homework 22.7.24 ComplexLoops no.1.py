import statistics
temps: list = []
for i in range(12):
    temp: int = int(input("What's the average temperature in Tel Aviv this month? "))
    if -5 <= temp <= 40:
        temps.append(temp)
    else:
        break;
for i in range (len(temps)-1):
    if temps[i] == 0 and temps[i + 1] == 0 and (len(temps)) == 12:
        print(f"There seems to be a mistake, as you entered the temperature 0 twice in a row.")
        print(f"These temperatures were for the {i + 1} and {i + 2} month")
        index1: int = int (input (f"Please modify your first input. For which month do you want to revise? "))
        new_temp1: int = int (input (f"And the new temperature for month no. {index1}? "))
        index2: int = int (input (f"Please modify your second input. For which month do you want to revise? "))
        new_temp2: int = int (input (f"And the new temperature for month no. {index2}? "))
        temps [index1 - 1] = new_temp1
        temps [index2 - 1] = new_temp2
        print(f"OK, the updated list of annual temperatures for 2023 is: \n{temps}")
if (len(temps)) == 12:
    print("Correct Data" if -5 < temp < 40 else None)
    print(f"Your annual list of average temperatures is {(temps)}")
    print(f"The annual average temperature for the year 2023 is {statistics.mean(temps):.2f}")
    print(f"The highest temperature this year was {max(temps)}")
    print(f"The lowest temperature this year was {min(temps)}")
else:
    print("Wrong Data")



