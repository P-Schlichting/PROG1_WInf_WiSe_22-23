"""
Aufgabe 3
Erstellen Sie ein Python-Programm mit den folgenden Anforderungen:
• Umrechnung von Fahrenheit nach Celsius
• Umrechnung von Celsius nach Fahrenheit
Dies kann sicher helfen:
Celsius = 5/9 * (Fahrenheit - 32).
"""

wahl = input(
    "Bitte geben Sie an auf was Sie umrechnen wollen (celsius oder fahrenheit): "
)

if wahl == "celsius":
    fahrenheit = float(input("Bitte geben Sie einen Fahrenheits Wert an: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(celsius)
else:
    celsius = float(input("Bitte geben Sie einen Celsius Wert an: "))
    fahrenheit = celsius * 1.8 + 32
    print(fahrenheit)
