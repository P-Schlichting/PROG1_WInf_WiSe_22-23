"""
Aufgabe 2
Schreiben Sie ein Programm, welches eine Liste bestehend aus ganzen Zahlen aufsteigend
sortiert. Der Benutzer soll per Eingabe entscheiden, welche Elemente in die Liste kommen
und er soll so viele Elementen eingeben können, wie er will. Wenn er mit der Eingabe fertig
ist, soll er mit einem Befehl (zum Beispiel q) die Eingabe beenden.
"""

repeat = True
counter = 0
pre_list = []
final_list = []
zahl = 0

while repeat == True:
    if counter == 0:
        pre_list[counter] = int(input(f"Bitte geben sie ihre erste Zahl ein."))
    else:
        pre_list[counter] = int(input(f"Bitte geben sie ihre nächste Zahl ein."))

    counter += 1

    if input("Wollen sie noch eine Zahl eingeben? (Ja/Nein)") == "Nein":
        repeat = False

final_list[0] = pre_list[0]
final_list[1] = pre_list[1]

counter = 1

while len(pre_list) != len(final_list): 
    zahl = pre_list[counter]
    for i in range(len(final_list)):

    