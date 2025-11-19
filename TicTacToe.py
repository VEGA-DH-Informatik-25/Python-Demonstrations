# tictactoe.py
# Übersetzung der gegebenen Java-Implementierung in Python

UNBELEGT = 0
minimumX = 0
minimumY = 0

# 1 ist der menschliche Spieler
# 2 ist der Computer
feld = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def ausgabe():
    for zeile in range(3):
        for spalte in range(3):
            print(feld[zeile][spalte], end=" ")
        print()
    print()

def auswertung():
    """
    Liefert:
      0  -> Computer (2) hat gewonnen
      2  -> Mensch (1) hat gewonnen
      1  -> Unentschieden
     -1  -> Spiel noch nicht entschieden (freie Felder vorhanden, kein Gewinner)
    """
    # Reihen prüfen
    for x in range(3):
        if feld[x][0] == 1 and feld[x][1] == 1 and feld[x][2] == 1:
            return 2
        if feld[x][0] == 2 and feld[x][1] == 2 and feld[x][2] == 2:
            return 0

    # Spalten prüfen
    for y in range(3):
        if feld[0][y] == 1 and feld[1][y] == 1 and feld[2][y] == 1:
            return 2
        if feld[0][y] == 2 and feld[1][y] == 2 and feld[2][y] == 2:
            return 0

    # Diagonalen prüfen
    if feld[0][0] == 1 and feld[1][1] == 1 and feld[2][2] == 1:
        return 2
    if feld[0][2] == 1 and feld[1][1] == 1 and feld[2][0] == 1:
        return 2
    if feld[0][0] == 2 and feld[1][1] == 2 and feld[2][2] == 2:
        return 0
    if feld[0][2] == 2 and feld[1][1] == 2 and feld[2][0] == 2:
        return 0

    # Gibt es noch freie Felder?
    for x in range(3):
        for y in range(3):
            if feld[x][y] == 0:
                return -1

    # Keine freien Felder und kein Gewinner -> Unentschieden
    return 1

def max_value():
    ev = auswertung()
    if ev != -1:
        return float(ev)

    maximalWert = -999.0
    for x in range(3):
        for y in range(3):
            if feld[x][y] == 0:
                feld[x][y] = 1  # Mensch macht Zug (maximierer)
                wert = min_value()
                if wert > maximalWert:
                    maximalWert = wert
                feld[x][y] = 0
    return maximalWert

def min_value():
    ev = auswertung()
    if ev != -1:
        return float(ev)

    minimalWert = 999.0
    for x in range(3):
        for y in range(3):
            if feld[x][y] == 0:
                feld[x][y] = 2  # Computer macht Zug (minimierer)
                wert = max_value()
                if wert < minimalWert:
                    minimalWert = wert
                feld[x][y] = 0
    return minimalWert

def minwo():
    """Wie min_value, aber speichert die beste Zugposition in minimumX, minimumY (globale Variablen)."""
    global minimumX, minimumY
    ev = auswertung()
    if ev != -1:
        return float(ev)

    minimalWert = 999.0
    for x in range(3):
        for y in range(3):
            if feld[x][y] == 0:
                feld[x][y] = 2
                wert = max_value()
                if wert < minimalWert:
                    minimalWert = wert
                    minimumX = x
                    minimumY = y
                feld[x][y] = 0
    return minimalWert

def spielen():
    global minimumX, minimumY
    while auswertung() == -1:
        ausgabe()
        # Eingabe X
        while True:
            try:
                x = int(input(" Dein X (1-3): "))
                x=x-1
                if 0 <= x <= 2:
                    break
                print("Bitte nur Werte von 1 bis 3")
            except ValueError:
                print("Bitte eine ganze Zahl eingeben (1-3).")
        # Eingabe Y
        while True:
            try:
                y = int(input(" Dein Y (1-3): "))
                y=y-1  # Korrigieren, da Benutzer 1-3 eingibt
                if 0 <= y <= 2:
                    break
                print("Bitte nur Werte von 1 bis 3")
            except ValueError:
                print("Bitte eine ganze Zahl eingeben (1-3).")

        if feld[y][x] != 0:
            print("Dieses Feld ist bereits belegt. Bitte wähle ein anderes.")
            continue

        feld[y][x] = 1  # menschlicher Zug
        ausgabe()

        # Nachdem Mensch gezogen hat: Computerzug berechnen
        if auswertung() != -1:
            break  # Spiel vorbei nach dem Zug des Menschen

        minwo()
        # falls minimumX/Y eine gültige Position sind
        feld[minimumX][minimumY] = 2
        print(f"Computer zieht: {minimumX+1}, {minimumY+1}")

    # Endausgabe und Ergebnis
    ergebnis = auswertung()
    ausgabe()
    if ergebnis == 2:
        print("Du hast gewonnen")
    elif ergebnis == 0:
        print("Du hast verloren")
    elif ergebnis == 1:
        print("Unentschieden")

if __name__ == "__main__":
    spielen()
