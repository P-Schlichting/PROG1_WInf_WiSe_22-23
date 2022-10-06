"""
Aufgabe 4
Erstellen Sie ein Python-Programm, das für ein eingegebenes beliebiges Datum die Anzahl
der bisher im Jahr vergangenen Tage ausgibt. (Der Einfachheit halber soll davon ausgegeben
werden, dass der Februar immer 28 Tage hat.)
"""

einundreizig_list = [1, 3, 5, 7, 8, 10, 12]
dreizig_list = [4, 6, 9, 11, 23, 24, 25]
max_tage = 0

datum = input("Bitte geben sie ein Datum an (z.B. 5.12.2022): ")
datum_list = datum.split(".")

for i in range(0, len(datum_list)):
    datum_list[i] = int(datum_list[i])
if datum_list[1] > 12 or len(datum_list) > 4:
    print("Bitte gebe ein gültiges Datum an.")

match datum_list[1]:
    case 1:
        tage = datum_list[0]
    case 2:
        tage = datum_list[0]
        for m in range(datum_list[2] - 2):
            for t in range(7):
                if t == einundreizig_list[t]:
                    max_tage = max_tage + 31
                elif t == dreizig_list[t]:
                    max_tage = max_tage + 30
                elif t == 2:
                    max_tage = max_tage + 28
        tage = datum_list[0] + max_tage
    case 3:
        tage = datum_list[0]
        for m in range(datum_list[2] - 2):
            for t in range(7):
                if t == einundreizig_list[t]:
                    max_tage = max_tage + 31
                elif t == dreizig_list[t]:
                    max_tage = max_tage + 30
                elif t == 2:
                    max_tage = max_tage + 28
        tage = datum_list[0] + max_tage
    case 4:
        tage = datum_list[0]
        for m in range(datum_list[2] - 2):
            for t in range(7):
                if t == einundreizig_list[t]:
                    max_tage = max_tage + 31
                elif t == dreizig_list[t]:
                    max_tage = max_tage + 30
                elif t == 2:
                    max_tage = max_tage + 28
        tage = datum_list[0] + max_tage
    case 5:
        tage = datum_list[0]
        for m in range(datum_list[2] - 2):
            for t in range(7):
                if t == einundreizig_list[t]:
                    max_tage = max_tage + 31
                elif t == dreizig_list[t]:
                    max_tage = max_tage + 30
                elif t == 2:
                    max_tage = max_tage + 28
        tage = datum_list[0] + max_tage
    case 6:
        tage = datum_list[0]
        for m in range(datum_list[2] - 2):
            for t in range(7):
                if t == einundreizig_list[t]:
                    max_tage = max_tage + 31
                elif t == dreizig_list[t]:
                    max_tage = max_tage + 30
                elif t == 2:
                    max_tage = max_tage + 28
        tage = datum_list[0] + max_tage
    case 7:
        tage = datum_list[0]
        for m in range(datum_list[2] - 2):
            for t in range(7):
                if t == einundreizig_list[t]:
                    max_tage = max_tage + 31
                elif t == dreizig_list[t]:
                    max_tage = max_tage + 30
                elif t == 2:
                    max_tage = max_tage + 28
        tage = datum_list[0] + max_tage
    case 8:
        tage = datum_list[0]
        for m in range(datum_list[2] - 2):
            for t in range(7):
                if t == einundreizig_list[t]:
                    max_tage = max_tage + 31
                elif t == dreizig_list[t]:
                    max_tage = max_tage + 30
                elif t == 2:
                    max_tage = max_tage + 28
        tage = datum_list[0] + max_tage
    case 9:
        tage = datum_list[0]
        for m in range(datum_list[2] - 2):
            for t in range(7):
                if t == einundreizig_list[t]:
                    max_tage = max_tage + 31
                elif t == dreizig_list[t]:
                    max_tage = max_tage + 30
                elif t == 2:
                    max_tage = max_tage + 28
        tage = datum_list[0] + max_tage
    case 10:
        tage = datum_list[0]
        for m in range(datum_list[2] - 2):
            for t in range(7):
                if t == einundreizig_list[t]:
                    max_tage = max_tage + 31
                elif t == dreizig_list[t]:
                    max_tage = max_tage + 30
                elif t == 2:
                    max_tage = max_tage + 28
        tage = datum_list[0] + max_tage
    case 11:
        tage = datum_list[0]
        for m in range(datum_list[2] - 2):
            for t in range(7):
                if t == einundreizig_list[t]:
                    max_tage = max_tage + 31
                elif t == dreizig_list[t]:
                    max_tage = max_tage + 30
                elif t == 2:
                    max_tage = max_tage + 28
        tage = datum_list[0] + max_tage
    case 12:
        tage = datum_list[0]
        for m in range(datum_list[2] - 2):
            for t in range(7):
                if t == einundreizig_list[t]:
                    max_tage = max_tage + 31
                elif t == dreizig_list[t]:
                    max_tage = max_tage + 30
                elif t == 2:
                    max_tage = max_tage + 28
        tage = datum_list[0] + max_tage

print(tage)
