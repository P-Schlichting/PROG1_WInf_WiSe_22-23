"""
Aufgabe 3
Schreiben Sie ein Programm, das eine Zahl n von der Konsole einliest und die Summe aller
natürlichen Zahlen (1 + 2 + 3 + ... + n) als Ergebnis zurückliefert.
"""
# Eingabe der Zahl n
n = int(input("Bitte geben sie eine Zahl an: "))

# Ausgabe der Summe aller Zahlen von 1 bis n durch die Funktion sum
print(sum(range(n + 1)))
