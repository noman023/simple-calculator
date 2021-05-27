print("Welcome to the game!")
name = input("What is your name?: ")
age = int(input("What is your age?: "))
if age >= 18:
    print("You are old enough!")

    want_to_play = input("Do you want to play?: ").lower()
    if want_to_play == "yes":
        print("Let's play!")

        left_or_right = input("First Choice ... Left or right (left/right)?").lower()
        if left_or_right == "right":
            ans= input("Nice, you follow the path and reach a river...do you want to swim accross or go by a boat(swim/boat)? ").lower()

            if ans == "swim":
                print("You're attacked by a crocodile ...YOU'VE LOST ")

            else:
                print("Crongratulations you cross the river safely ... YOU'VE WON")  

        else:
            print("You fell down and lost try again!")  
    else:
        print("Thank You!! Come Again!")
else:
    print("You are not old enough to play")
