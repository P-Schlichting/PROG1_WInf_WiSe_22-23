"""
Aufgabe 5
Ab 0,5 Promille Blutalkoholkonzentration darf man nach der derzeitigen Rechtslage kein
Kraftfahrzeug führen. Aber auch schon bei einer geringeren Blutalkoholkonzentration ist die
Konzentrations- und Reaktionsfähigkeit eingeschränkt.
Die Blutalkoholkonzentration hängt von zahlreichen Faktoren ab und lässt sich wie folgt
berechnen:
mit A = V∗ϵ∗ρ
c: Alkoholkonzentration im Blut in [g/kg]
A: Aufgenommene Masse des Alkohols in [g]
r: Verteilungsfaktor im Körper (Männer: r ≈ 0,7 / Frauen: r ≈ 0,6 / Kinder: r ≈ 0,8)
m: Masse der Person in [kg]
V: Volumen des Getränks in [ml]
ϵ: Alkoholvolumenanteil in [%] (z. B. Bier ≈ 0,05)
ρ: Dichte von Alkohol [g/ml] → ρ ≈ 0,8g/ml
Schreibe ein Programm, das die Blutalkoholkonzentration mit der Widmark-Formel
berechnet. Die Eingabegrößen sollen dabei flexibel einstellbar sein.
"""

v = float(input("Wie viel milliliter Alkohol wurde getrunken: "))
e = float(input("Wie viel Prozent Alkohol hatte das Getränk: "))
m = float(input("Wie schwer ist die Person: "))
r_angabe = input(
    "Ist die Person Männlich, Weiblich oder ein Kind (bitte klein angeben): "
)
if r_angabe == "männlich":
    r = 0.7
elif r_angabe == "weiblich":
    r = 0.6
elif r_angabe == "kind":
    r = 0.8
else:
    print(
        "Bitte geben Sie beim nächsten mal einen richtigen Personen Wert an. Das Programm beendet sich nun."
    )
    exit()
p = 0.8
a = v * (e / 100) * p
c = a / (m * r)
print(c)
