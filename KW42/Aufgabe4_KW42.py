"""
Aufgabe 4 (schwer)
Implementieren Sie die Wurzelberechnung mit dem Newton-Verfahren. Sie sollen beliebige
vom Nutzer eingegebene Werte berechnen können. Beachten Sie, dass aus negativen
Werten per Definition keine Wurzel gezogen werden kann!
Mit dem Newton-Verfahren nähert man sich der Wurzel von x mithilfe eines Startwerts z
durch Wiederholen der folgenden Berechnung an:

z' = z - (z^2 - x)/2z

z’ soll hier den neuen Wert für z bezeichnen, der sich aus einer Berechnung ergibt.
Lösen Sie das Problem mit einer Schleife. Beenden Sie die Schleife sobald sich das Ergebnis
nicht mehr ändert, d. h. abs(z’-z) < delta, wobei z. B. delta = 0.0000001 ist.
Ein typischer Programmablauf könnte so aussehen:

Geben Sie bitte eine Zahl x ein: 2
Die Wurzel von 2 lautet: 1.4142135623730951
Ich musste hierzu 5 Iterationen durchführen
Python behauptet die Wurzel von 2.0 sei 1.4142135623730951.
"""


def berechnung(x):
    delta = 0.0000001
    z_org = 1
    repeat = True
    while repeat:
        z_new = z_org - (z_org**2 - x) / 2 * z_org
        if abs(z_new - z_org) < delta:
            repeat = False
        else:
            z_org = z_new

    return z_new


x = int(input("Bitte geben sie ihren Wert an: "))

print(f"Die Wurzel von {x} lautet: {berechnung(x)}")
