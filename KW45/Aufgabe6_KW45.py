"""
Aufgabe 6
Schreiben Sie eine (eigene) Funktion, die eine Binärzahl in eine Dezimalzahl transformiert.
Beispiel: dualToInt(’1001’) → 9.
"""

string1 = "1001"
string2 = ""
wert = 0

for x in range(len(string1) - 1, -1, -1):
    string2 += "" + string1[x]

for i in range(len(string2)):
    if string2[x] == "1":
        wert += 2 ** (x + 1)

print(wert)
