import statistics
temp: int = int (input("What's the average temperature in Tel Aviv this month?"))
temps: list = []
for i in range (11):
    if -5 <= temp <= 40:
        temps.append(temp)
        temp = int(input("What's the average temperature in Tel Aviv this month?"))
    else:
        break;
for i in range ((len(temps)+1)):
    if temps[i] == temps[i + 1] ==0:
        print(f"There seems to be some kind of mistake, as you entered the temperature 0 twice in a row")
        print(f"These temperatures were for the {temps.index(i)} and {temps.index(i+1)} month")
        print (temps)
        index1 = int (input(print(f"Please modify your first input. For which month do you want to revise?")))
        new_temp1: int = int (input(f"And the new temperature for month no. {index1}?"))
        index2 = int (input(print(f"Please modify your second input. For which month do you want to revise?")))
        new_temp2: int = int (input(f"And the new temperature for month no. {index2}?"))
        temps.insert (index1-1,new_temp1)
        temps.insert(index2-2, new_temp2)
        print(f"OK, the updated list of annual temperatures for 2023 is \n{temps}")


print("Correct Data" if -5 < temp < 40 else "Wrong Date")
print(temps)
print(f"The annual average temp for the year 2023 was {statistics.mean(temps)}")
print(f"The highest temperature this year was {max(temps)}")
print(f"The lowest temperature this year was {min(temps)}")
