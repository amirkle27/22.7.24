count = 0
For: list = []
Against: list = []
Sustained: list = []
Veto: list = []
sub: str = str(input("Hello, what are we voting for today?"))
while count < 44:
    vote: int = int (input("How would you like to vote? \n[1 - For\n2 - Against\n3 - Sustained\n4 - Veto]"))
    try:
        match vote:
            case 1: For.append(count)
            case 2: Against.append(count)
            case 3: Sustained.append(count)
            case 4:
                Veto.append(count)
                print(f"{' ' * 10}Country no. {count + 1} has Vetoed the vote! Added to Veto list.")
        if 5 > vote > 0 : count+=1
        if vote == 4:
            break;
    except Exception as e:
        print("It seems the last vote was invalid. Please try again")
print("After the vote, we had:")
print(f"{len(For)} countries voting For {sub}:  {For}")
print(f"{len(Against)} countries voting Against {sub}:   {Against}")
print(f"{len(Sustained)} countries Sustained:   {Sustained}")
print(f"and {len(Veto)} Vetoes:   {Veto}")
if len(For) > 0:
    print(f"The first country who voted For {sub} was: {For[0]}")
if len(Against) > 0:
    print(f"The last country who voted Afainst {sub} was {Against[-1]}")
