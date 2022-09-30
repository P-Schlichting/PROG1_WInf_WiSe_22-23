v = float(input("Wie viel milliliter Alkohol wurde getrunken: "))
e = float(input("Wie viel Prozent Alkohol hatte das Getränk: "))
m = float(input("Wie schwer ist die Person: "))
r_angabe = input("Ist die Person Männlich, Weiblich oder ein Kind (bitte klein angeben): ")
if r_angabe == "männlich":
    r = 0.7
elif r_angabe == "weiblich":
    r = 0.6
elif r_angabe == "kind":
    r = 0.8
else:
    print("Bitte geben Sie beim nächsten mal einen richtigen Personen Wert an. Das Programm beendet sich nun.")
    exit()
p = 0.8
a = v * (e / 100) * p
c = a / (m*r)
print(c)