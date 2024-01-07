
print("Hello there! this is my first game ever!\nplease enjoy! lol")
name = input("please enter ur name:\n")
age = int(input("hello " + name + " ! now enter your age:\n"))
health = 10

if age >= 12:
    print("you are old enough to continue!")

    wants_to_play = input("do you wanna play?(yes/no)\n").lower()
    if wants_to_play == "yes":
        print("you have", health, "healths now")
        print("lets play now!")

        left_or_right = input("ok first choice, left or right?(left/right)\n")
        if left_or_right == "left":
            ans = input("nice, u keep going then u reach a lake... would ya cross it or go around?(across/around)\n")
            if ans == "across":
                print("u managed to get across but were bit by a fish and lost 5 healths\n")
                health = health - 5
            elif ans == "around":
                print(" u successfully reached the other side of the lake")

            ans = input("u notice a house and a river, which do u go to?(house/river)\n")
            if ans == "house":
                print("u go in there but the owner will shoot u and u lose 5 health")
                health = health - 5
                if health <= 0:
                    print("u have 0 health and lost the game")
                else:
                    print(" u have survived, u win!")
            elif ans == "river":
                print("u fell in the river and lost")
        elif ans == "left":
            print("u fell down and lost")

    else:
        print("well good luck then! bye!")

else:
    print("oh no you are too young :(((")
    