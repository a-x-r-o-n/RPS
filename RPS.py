import random

logic = True



while logic:

    picker = random.choice(["rock", "paper", "scizzors"])
    usr = input("\n\n|======| RPS - GAME |======|\n\nROCK\tPAPER\tSCIZZOR\n\nEnter any of the above option enter \"Quit\" to terminate the session\n>>> ")

    usr = usr.lower()
    if usr == picker:

        print("It's a Draw")

    elif usr == "Quit":

        print("thank you for playing")
        logic = False

    elif (picker == "rock" and usr == "paper") or (picker == "scizzors" and usr == "rock") or (picker == "paper" and usr == "scizzers"):

        print("you won!!")

    elif (picker == "rock" and usr == "scizzors") or (picker == "scizzors" and usr == "paper") or (picker == "paper" and usr == "rock"):

        print("you lose!!")


    else:

        print("You've entered wrong word try again!!")