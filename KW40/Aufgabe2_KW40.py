"""
Aufgabe 2
Erstellen Sie ein Python-Programm mit den folgenden Anforderungen.
    a) Mit der Konstruktion von zwei geeigneten Schleifen soll folgendes 20x5 Rechteck
    entstehen:

        ********************
        ********************
        ********************
        ********************
        ********************
        
    Tipp: Mit dem Zusatz end=“ “ verhindern Sie einen Zeilenumbruch bei der Ausgabe
    von print, z. B.
        print("Pink", end=" ")
        print("Octopus)
    b) Erweitern Sie Ihr Programm für beliebige Rechtecke in x/y-Richtung
"""

# Abfrage der Rechteck größe durch x und y Richtung
print("Bitte geben sie an wie größ ihr Rechteck sein soll.")
x = int(input("X Richtung: "))
y = int(input("Y Richtung: "))

# Ausgabe des Rechtecks durch zwei verschachtelte For Schleifen mit der Range von x und y
for i in range(y):
    print()
    for t in range(x):
        print("*", end=" ")
