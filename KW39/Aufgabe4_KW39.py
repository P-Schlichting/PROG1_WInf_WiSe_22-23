"""
Aufgabe 4
Das folgende Programm zur Kapitalverzinsung enthält mehrere Fehler.
# Eingabe
kapital = input('Kapital (in Euro):')
# Verarbeitung
zinssatz = 2.0%
zinsen = kapital * zinssatz
kapital = kapital + zinsen
# Ausgabe
print('neues kapital: kapital')
Suchen Sie und korrigieren Sie den Fehler!
"""

# Eingabe
kapital = float(input("Kapital (in Euro): "))
# Verarbeitung
zinssatz = 2.0
zinsen = kapital / 100 * zinssatz
kapital = kapital + zinsen
# Ausgabe
print("neues Kapital ist: ", kapital)
