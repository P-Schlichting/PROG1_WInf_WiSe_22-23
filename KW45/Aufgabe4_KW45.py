"""
Aufgabe 4
Erstellen Sie ein Python-Programm mit den folgenden Anforderungen.
a) Der Anwender soll dazu aufgefordert werden, einen beliebigen Satz einzugeben, z. B.
„Der Hund läuft in die Küche“
b) Erstellen Sie eine Funktion, welche analysiert, wie viel Wörter in dem Satz
vorkommen
c) Erstellen Sie eine Funktion, welche analysiert, wie die durchschnittliche Wortlänge im
Satz ist
"""

string = input("Bitte geben sie einen Satz ein: ")
list = string.split(" ")


def anzahl():
    print(f"Der Satz hat {len(list)} Wörter")


def länge():
    wert = 0
    for x in list:
        wert += len(x)
    wert = wert / len(list)
    print(f"Der Satz hat eine durchschnitts Wortlänge von {wert} Wörtern")


anzahl()
länge()
