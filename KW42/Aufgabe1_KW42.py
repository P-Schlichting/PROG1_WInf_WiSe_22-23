"""
Aufgabe 1
Wandeln Sie den BMI-Rechner aus den Vorlesungsfolien in ein neues Programmdesign um
mit den folgenden Anforderungen:
• Eine erste Funktion, die aus Gewicht und Größe den BMI zurückliefert.
• Eine zweite Funktion, die die Interpretation des BMI (zu schwer, zu leicht,..) ausgibt.
Ein Hauptprogramm verwendet die zwei Funktionen, um den kompletten Ablauf
umzusetzen.
"""

# Funktion die den BMI ausrechnet
def bmi_rechner(groesse, gewicht):
    bmi = gewicht / ((groesse / 100) ** 2)
    return bmi


# Funktion die den BMI interpretiert
def bmi_interpret(bmi):
    if bmi < 17:
        str = "zu leicht"
    elif bmi > 25:
        str = "zu schwer"
    else:
        str = "im Normalbereich"

    return str


# Input der Größe und Gewicht
groesse = int(input("Größe in cm:"))
gewicht = int(input("Gewicht in kg:"))

# Aufrufen der Funktion "bmi_rechner" dessen Ruckgabewert in bmi geschrieben wird
bmi = bmi_rechner(groesse, gewicht)

print(f"Sie haben einen BMI von {bmi} d.h. sie sind {bmi_interpret(bmi)}.")
