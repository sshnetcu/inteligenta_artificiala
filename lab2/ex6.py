def aventura():
    inventar = []

    print("🌲 Te afli într-o pădure magică...")
    alegere = input("Alegi direcția: stânga sau dreapta? ").lower()

    if alegere == "stanga":
        print("🐺 Ai întâlnit un lup!")
        actiune = input("Fugi sau lupți? ").lower()

        if actiune == "fugi":
            print("Ai scăpat! Ai găsit o poțiune magică.")
            inventar.append("poțiune")
        elif actiune == "lupti":
            print("Ai învins lupul! Ai primit o sabie.")
            inventar.append("sabie")
        else:
            print("Ai stat pe loc... lupul te-a speriat și ai fugit.")

    elif alegere == "dreapta":
        print("💰 Ai descoperit o comoară!")
        inventar.append("aur")

        actiune = input("Continui sau te întorci? ").lower()

        if actiune == "continui":
            print("🧙 Ai întâlnit un vrăjitor care îți dă un inel magic.")
            inventar.append("inel magic")
        else:
            print("Te-ai întors în siguranță.")

    else:
        print("Nu ai ales corect direcția... te-ai rătăcit.")

    print("\n🎒 Inventarul tău:", inventar)


aventura()