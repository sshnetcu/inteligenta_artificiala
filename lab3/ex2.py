def genereaza_factura(client, **kwargs):
    print("Factura pentru: " + client)
    for i,v in kwargs.items():
        print(str(i) + ": " + str(v))

genereaza_factura("marius", lapte = 1, paine = 5)