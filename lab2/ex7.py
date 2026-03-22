def analiza_comentariu():
    pozitiv = ["bine", "frumos", "super", "excelent", "minunat"]
    negativ = ["urat", "prost", "groaznic", "dezamagitor"]

    comentariu = input("Introdu comentariul: ").lower()

    if any(cuvant in comentariu for cuvant in pozitiv):
        print("Comentariu pozitiv!")
    elif any(cuvant in comentariu for cuvant in negativ):
        print("Comentariu negativ!")
    else:
        print("Comentariu neutru.")


analiza_comentariu()