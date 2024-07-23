age: int = int (input ("Hello and welcome to our rollercoaster! please state your age"))
height: int = int (input ("And your height? (in cm, if you please)"))
if 8 <= age <= 18 and height >= 115 or age > 18 and height > 100:
    print("Well, it seems you can go on the rollercoaster! Pleae enjoy a wonderful ride!")
else:
    print("Well, it seems you can't go on the rollercoaster this time...! Come again when you're older or higher :(")