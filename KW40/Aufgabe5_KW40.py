"""
Aufgabe 5
Erstellen Sie ein Python-Programm das solange eine natürliche Zahl einliest, bis keine Zahl
oder eine falsche Eingabe erfolgt. Am Ende soll die größte Zahl von den eingegebenen
Zahlen auf der Konsole ausgegeben werden.
Bitte geben Sie eine natürliche Zahl ein: 2
Bitte geben Sie eine natürliche Zahl ein: 8
Bitte geben Sie eine natürliche Zahl ein: 5
Bitte geben Sie eine natürliche Zahl ein: h
Die größte Zahl war: 8
Überlegen Sie zunächst einen Algorithmus in Prosa: wie geht man vor, um die Aufgabe zu
lösen. Setzen Sie dann den Algorithmus in Python um.
"""
repeat = True
max_number = 0

# Schleife die sich wiederholt solange repeat True ist
while repeat == True:

    # Eingabe der Zahlen
    number = input("Bitte geben Sie eine natürliche Zahl ein: ")

    # Überprüfung ob es sich um eine Zahl handelt mit Try (Checkt ob es ein Error gibt und würde dann ab except weiter laufen)
    try:
        number = int(number)
        if max_number < number:
            max_number = number
    except:
        repeat = False

# Ausgabe
print(f"Die größte Zahl was: {max_number}")
