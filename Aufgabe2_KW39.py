"""
Aufgabe 2
Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
• Es soll aus einem eingegebenen Nettobetrag die 19% Mehrwertsteuer und der
Bruttobetrag errechnet und angezeigt werden.
"""

netto = float(input("Bitte geben Sie den Netto Preis an: "))
brutto = netto + (netto / 100 * 19)
print("Der Bruttobetrag lautet: ", brutto)
