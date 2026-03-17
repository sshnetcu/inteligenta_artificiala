nota = 0
fail = False
while nota > 10 or nota <= 0:
    if fail:
        print("Introduceti o nota intre 1 si 10!!!")
    nota = int(input("Nota: "))
    if nota > 10 or nota <= 0:
        fail = True

out = "text"
if nota >= 9:
    out = "Excelent"
elif nota >= 7:
    out = "Bine"
elif nota >= 5:
    out = "Suficient"
else:
    out = "Reexaminare"

print(out)