name = input("What is your name? ")
print("Welcome", name , "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Type left to go left and right to go right. ").lower()

if answer == "left":
    answer = input("You have come across a river. You can walk around it or swim across. Type walk to walk around and swim to swim across. ").lower()

    if answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    elif answer == "swim":
        print("You swam across and were eaten by an alligator.")
    else:
        print("Not a valid option.")

elif answer == "right":
    answer = input("You come across a bridge, it looks wobly. Do you want to cross it or head back. (cross/back) ").lower()

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them. Yes/No: ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN")
        elif answer == "no":
            print("You go back and loose.")
        else:
            print("Not a valid option.")

    elif answer == "back":
        print("You go back and loose.")
    else:
        print("Not a valid option.")

else:
    print("Not a valid option.")

print("Thank you for tring", name)