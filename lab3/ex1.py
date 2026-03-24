while True:
    print("Rock-Paper-Scissors")
    print("Choose: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    plr1 = int(input("Player 1: "))
    while plr1 > 3 or plr1 < 1:
        print("Input a valid option.")
        plr1 = int(input("Player 1: "))

    plr2 = int(input("Player 2: "))
    while plr2 > 3 or plr2 < 1:
        print("Input a valid option.")
        plr2 = int(input("Player 2: "))

    if plr1 == plr2:
        print("Player 1: " + str(plr1))
        print("Player 2: " + str(plr2))
        print("Tie!")

    if (plr1+1)%4 == plr2:
        print("Player 1: " + str(plr1))
        print("Player 2: " + str(plr2))
        print("Player2 wins.")
    else:
        print("Player 1: " + str(plr1))
        print("Player 2: " + str(plr2))
        print("Player1 wins.")

    choice = input("Play again? (Y/N):")
    if choice == "Y":
        continue
    break
