hour = 60
time: int = int (input("Please enter a movie's length in minutes"));
sheerit: int = 0
time1 = time//60
if not time % hour == 0:
    sheerit = (time - 60*time1)
print (f" The length of your movie is {time//60} hours and {sheerit} minutes")



