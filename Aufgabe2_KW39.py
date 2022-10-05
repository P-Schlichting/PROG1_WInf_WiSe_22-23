"""
Aufgabe 2
Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
• Es soll aus einem eingegebenen Nettobetrag die 19% Mehrwertsteuer und der
Bruttobetrag errechnet und angezeigt werden.
"""

# Eingabe des Nettobetrags
netto = float(input("Bitte geben Sie den Netto Preis an: "))

# Rechnung von Netto auf Brutto
brutto = netto + (netto / 100 * 19)

# Ausgabe des Bruttobetrags
print("Der Bruttobetrag lautet: ", brutto)
