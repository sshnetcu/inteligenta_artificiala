import random

numere = []

while len(numere) < 6:
    num = int(input("Inserisci un numero " + str(numere) + ": "))
    if num > 49 or num < 1:
        print("Inserisci un numero between 1 and 49!")
        continue
    if num in numere:
        print("No repeats!")
        continue
    numere.append(num)

lotto = []
for i, v in enumerate(numere):
    entry = random.Random().randint(1, 49)
    while entry in lotto:
        entry = random.Random().randint(1, 49)
    lotto.append(entry)

print(numere)
print(lotto)
print("Numere ghicite: ")
for i,v in enumerate(numere):
    if v in lotto:
        print(v)
if numere == lotto:
    "JUCKPOT!"