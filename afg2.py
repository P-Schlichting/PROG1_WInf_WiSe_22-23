from operator import ne


netto = float(input("Bitte geben Sie den Netto Preis an: "))
brutto = netto + (netto/100*19)
print("Der Bruttobetrag ist: ", brutto)