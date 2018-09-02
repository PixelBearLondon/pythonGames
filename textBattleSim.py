import random
userHP = 100
monHP = 50
rnd = 0

print("--------------------")
print("  TEXT BATTLE SIM   ")
print("--------------------")
print("       STORY:       ")
print("")
print("Your walking.")
print("Suddenly, a Vloger.")
print("He turns on a phone")
print("You turn on a phone")
print("Game on!")
print("--------------------")

while userHP > 1 and monHP > 1:
    print("YourHP:", userHP)
    print("VloggerHP:", monHP)
    answer = input("Will you B:block or A:attack?")
    if answer.lower() == "a":
        rnd = random.randint(1, 50)
        if rnd < 39:
            if monHP == 10:
                break
            else:
                monHP = monHP - 10
                print("you attack and do 10 damage")
        else:
            print("you attack but miss")
        if userHP == 5:
            break
        else:
            userHP = userHP - 5
            print("He attacked so you lost 5HP")
    elif answer.lower() == "b":
        print("He attacked but you blocked")
if userHP == 5:
    print("")
    print("Oh no!You lost!Please try again.")
else:
    print("")
    print("You won!Please try again")
