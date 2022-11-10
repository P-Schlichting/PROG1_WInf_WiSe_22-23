"""
Aufgabe 5
Erstellen Sie ein Python-Programm mit einer Funktion reverse(text), die einen
gegebenen String in umgekehrter Reihenfolge zurückgibt. Die selbstgeschriebene Funktion
soll eine for- oder eine while- Schleife verwenden!
Beispiel: reverse(’informatik’) → ’kitamrofni’.
"""

string1 = "informatik"
string2 = ""
counter = 0

for x in range(len(string1) - 1, -1, -1):
    string2 += "" + string1[x]

print(string1)
print(string2)
