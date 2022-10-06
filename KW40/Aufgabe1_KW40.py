"""
Aufgabe 1
Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
    •   Der Anwender soll dazu aufgefordert werden, sein monatliches Bruttogehalt
        einzugeben.
    •   Liegt das Gehalt über 2.500 €, sind 22% Steuern zu zahlen, ansonsten 18%.
    •   Innerhalb des Programms soll anhand des Gehalts entschieden werden, welcher
        Steuersatz zur Anwendung kommt.
    •   Die Ausgabe kann zum Beispiel wie folgt aussehen:

    Geben Sie Ihr Bruttogehalt in Euro ein:
    3000
    Es ergibt sich ein Steuerbetrag von 660.0 Euro
    oder sie kann so aussehen:
    Geben Sie Ihr Bruttogehalt in Euro ein:
    2000
    Es ergibt sich ein Steuerbetrag von 360.0 Euro
"""


# Eingabe des monatliches Bruttogehaltes
bruttogehalt = float(input("Bitte geben Sie ihr monatliches Bruttogehalt: "))

# Bestimmung des Steuersatzes an höhe des monatlichen Bruttogehalts
if bruttogehalt >= 2500:
    zinssatz = 0.22
else:
    zinssatz = 0.18

# Rechnung des monatlichen Nettogehalts und Steuerbetrags
steuerbetrag = bruttogehalt * zinssatz
nettogehalt = bruttogehalt - steuerbetrag

# Ausgabe des monatlichen Nettobetrags und Steuerbetrags
print(f"Ihr Nettogehalt beträgt {nettogehalt}€ und der Steuerbetrag {steuerbetrag}€.")
