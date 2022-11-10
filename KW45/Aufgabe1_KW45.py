"""
Aufgabe 1
Um für Reisen mit dem Auto besser planen zu können, wollen wir herausfinden, wie viele
Kilometer wir im Durchschnitt mit einer vollen Tankfüllung gefahren sind. Dafür bekommen
wir eine Liste mit int-Werten übergeben, welche die Gesamtzahl an Kilometern angeben, die
wir mit einer Tankfüllung gefahren sind. Als Ergebnis wollen wir einen float-Wert mit der
Anzahl an Kilometern berechnen, die wir im Mittel mit einer Tankfüllung fahren können.
Beispiel: [123, 134, 120, 122] → 124.75
"""

kilometer_list = [123, 134, 120, 122]
wert = 0
for i in range(len(kilometer_list)):
    wert = wert + kilometer_list[i]
wert = wert / len(kilometer_list)
print(f"Durchschnittliche Km = {wert}km")
