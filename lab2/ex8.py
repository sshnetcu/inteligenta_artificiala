def sistem_bancar():
    tari_risc = ["Coreea de Nord", "Siria", "Iran"]
    tranzactii = []
    tranzactii_suspecte = 0

    n = int(input("Câte tranzacții vrei să introduci? "))

    for i in range(n):
        print(f"\nTranzacția {i+1}:")
        suma = float(input("Suma (RON): "))
        tara = input("Țara: ")

        rezultat = "Sigură"

        if suma > 10000:
            rezultat = "Suspicioasă (sumă mare)"
            tranzactii_suspecte += 1

        if tara in tari_risc:
            rezultat = "Frauduloasă (țară cu risc ridicat)"
            tranzactii_suspecte += 1

        tranzactii.append((suma, tara, rezultat))

    print("\nProcesăm tranzacțiile...\n")

    for t in tranzactii:
        print(f"Tranzacție: {t[0]} RON din {t[1]} → {t[2]}")

    if tranzactii_suspecte >= 3:
        print("\n⚠️ 3 tranzacții suspecte detectate! Cont blocat.")
    else:
        print("\n✅ Contul este în siguranță.")


sistem_bancar()