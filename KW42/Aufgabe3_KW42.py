"""
Aufgabe 3
Programmieren Sie ein Adventure. Folgender Spielablauf könnte hier passieren:
Du befindest Dich in einem Land voller Drachen. Vor Dir siehst Du zwei Höhlen.
In einer Höhle ist der Drache freundlich und gibt Dir sein ganzes Gold.
Der andere Drache ist gierig und hungrig und wird Dich sofort fressen.
In welche Höhle wirst du gehen? (1 oder 2)
1
Du näherst dich der Höhle.....
Es ist dunkel und gruselig.....
Ein großer Drache springt vor dir hervor! Er öffnet seine Kiefer und.....
verschlingt Dich in einem Bissen!
Willst du wieder spielen? (ja oder nein)
nein.

Ablaufplan
Start-->Spielanleitung-->Spieler wählt eine Höhle-->Test auf guten oder bösen Drache-->Spieler gewinnt oder verliert
-->Frage auf wiederholung mit Sprung auf "Spielanleitung" oder zum Ende
"""
# Import os damit ich den Terminal befehl cls nutzen kann um das Terminal zu clearen
import os

clear = lambda: os.system("cls")

repeat = True

# Funktion zur Ausgabe der Anleitung/Beschreibung
def anleitung():
    print(
        f"Du befindest dich vor der Wahl welche Höhle du betreten willst.\nIn der einen Höhle befindet sich ein freubdlich gesinter Drache der dir sein gesamten Schatz schenken würde. Doch in der anderen befindet sich ein böser Drache der nur drauf wartet das sein neues Festmahl zu im kommt."
    )
    print(f"Nun wähle deinen Weg und betrette die Höhle.")
    input("Beliebige Taste zum fortfahren drücken...")
    clear()


# Funktion die den Spielablauf ausgibt und die überprüfung übernimmt
def spiel():
    x = int(input(f"Vor dir befinden sich die zwei Höhlen. Welche wählst du?: "))
    print(
        f"Du näherst dich der Höhle.....\nEs ist dunkel und gruselig....\nEin großer Drache springt vor dir hervor! Er öffnet seinen Kiefer und....."
    )
    match x:
        case 1:
            print(f"verschlingt Dich in einem Bissen!")
        case 2:
            print(f"grüßt dich und mach dir den Weg zu seinem Schatz frei.")
    input("Belibege Teste zum fortfahren drücken...")
    clear()


while repeat:
    clear()
    anleitung()
    spiel()
    # Input um das Spiel zu wiederholen / zu schließen
    var = input(
        "Wenn du nochmal spielen willst drucke ENTER ansonsten geben Exit/exit ein um das Spiel zu beenden."
    )
    clear()
    if var == "exit" or var == "Exit":
        repeat = False
