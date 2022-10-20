"""
Aufgabe 2
Der optimale Puls bei Ausdauersportarten hängt vom Alter ab. Er lässt sich mit der Formel
P = 165 - 0.75 * Alter
bestimmen.
Schreiben Sie ein Programm, das folgenden Dialog ermöglicht:
Alter: 18
optimaler Puls: 151.5
Bringen Sie die Berechnung der Formel in eine Funktion und binden Sie die Funktion in Ihr
Programm ein!
"""

# Funktion die den optimal Puls beim Ausdauersport berechnet
def puls_rechner(alter):
    p = 165 - 0.75 * alter
    return p


# Input des Alters und Ausgabe des Optimalenpuls durch aufrufen der Funktion "puls_rechner" innerhalt des pirnt befehls
alter = int(input("Alter: "))
print(f"Ihr optimaler Puls beim Ausdauersport bei {puls_rechner(alter)}")
