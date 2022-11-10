"""
Aufgabe 3
Datenkompression ist aus unserem Alltag nicht wegzudenken. Wir alle haben mit Sicherheit
schon unzählige ZIP-Dateien geöffnet. Einen simplen Kompressionsalgorithmus für Strings
wollen wir in dieser Aufgabe programmieren.
Der Aufbau der zu komprimierenden Strings ist dabei sehr besonders, da diese nur aus den
Zeichen 'W' und ' B' bestehen. Das Kompressionsverfahren zählt alle aufeinanderfolgenden
gleichen Zeichen. Anschließend ersetzt es diese durch die numerische Anzahl, gefolgt vom
gezählten Zeichen.
Beispiel:   "WWWWBBBWBBBBBBWW" → "4W3B1W6B2W"
            "BBBBWWWWWWWWWB" → "4B9W1B"
            "WBBBBWWWWWWB" → "1W4B6W1B"
"""
counter = 1

pre_string = "WWWWBBBWBBBBBBWW"
final_string = ""

pre_list = list(pre_string)
final_list = []

for i in range(1, len(pre_list)):
    if pre_list[i - 1] == pre_list[i]:
        counter += 1
    else:
        final_list.append(counter)
        final_list.append(pre_list[i - 1])
        counter = 1

# final_string.join(str(final_list))

final_string = "".join(str(x) for x in final_list)

print(pre_string)
print(final_string)

for
