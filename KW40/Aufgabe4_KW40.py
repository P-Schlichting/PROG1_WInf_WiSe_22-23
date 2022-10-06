"""
Aufgabe 4
Erstellen Sie ein Python-Programm, das für ein eingegebenes beliebiges Datum die Anzahl
der bisher im Jahr vergangenen Tage ausgibt. (Der Einfachheit halber soll davon ausgegeben
werden, dass der Februar immer 28 Tage hat.)
"""

tage = 0

# Eingabe des Datums und aufsplitten in eine Liste nach Tag Monat Jahr
datum = input("Bitte geben sie ein Datum an (z.B. 5.12.2022): ")
datum_list = datum.split(".")

# Umwandeln der string Werte in der Liste zu int Werten
for i in range(0, len(datum_list)):
    datum_list[i] = int(datum_list[i])

# Überprüfung ob es sich um ein Datum handelt
if datum_list[1] > 12 or len(datum_list) > 4:
    print("Bitte gebe ein gültiges Datum an.")

# Berechnung der vergangenen Tage
for t in range(1, datum_list[1]):
    if t == 1 or t == 3 or t == 5 or t == 7 or t == 8 or t == 10 or t == 12:
        tage = tage + 31
    elif t == 4 or t == 6 or t == 9 or t == 11:
        tage = tage + 30
    else:
        tage = tage + 28
tage = tage + datum_list[0]

# Ausgabe
print(f"Bis zum {datum} sind schon {tage} Tage des Jahres vergangen.")
