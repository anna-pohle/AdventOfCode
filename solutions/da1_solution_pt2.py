# Input einlesen als Liste von Instructions
with open('input.txt', 'r') as f:
    instructions = [line.strip() for line in f]

# Initiale Liste erstellen (300 Elemente, 0-99 wiederholt)
dial = [i % 100 for i in range(300)]
# Input einlesen als Liste von Instructions
with open('day1_data.txt', 'r') as f:
    instructions = [line.strip() for line in f]

# Initiale Liste erstellen (300 Elemente, 0-99 wiederholt)
dial = [i % 100 for i in range(300)]

# Startposition und Counter
position = 150  # Index 150 zeigt auf die Zahl 50
counter = 0

# Durch alle Instructions gehen
for instruction in instructions:
    # Parse Richtung und Distanz
    direction = instruction[0]  # 'L' oder 'R'
    distance = int(instruction[1:])  # Die Zahl nach dem Buchstaben

    # Aktuelle Zahl auf dem Dial (nicht der Index!)
    current_number = dial[position]

    # Zähle komplette 100er-Runden
    vollstaendige_runden = distance // 100
    counter += vollstaendige_runden

    # Restliche Distanz nach den vollen Runden
    rest_distance = distance % 100

    # Berechne neue Position
    distance_for_movement = distance % 100
    if direction == 'L':
        neue_position = position - distance_for_movement
    else:  # direction == 'R'
        neue_position = position + distance_for_movement

    # Erweitere dial-Liste nur wenn out of range
    if neue_position < 0:
        neue_elemente = [i % 100 for i in range(100)]
        dial = neue_elemente + dial
        position = position + 100
        neue_position = neue_position + 100

    if neue_position >= len(dial):
        dial.extend([i % 100 for i in range(100)])

    # Bewege Position
    position = neue_position

    # Prüfe ob wir auf 0 gelandet sind
    landet_auf_null = (dial[position] == 0)

    # Prüfe ob die Restbewegung durch 0 geht
    geht_durch_null = False
    if direction == 'R':
        # Rechts: Gehe durch 0 wenn rest_distance die Lücke bis 100 überschreitet
        # ABER nur wenn wir nicht bei 0 starten!
        if rest_distance > 0 and current_number + rest_distance > 99 and current_number != 0:
            geht_durch_null = True
    else:  # direction == 'L'
        # Links: Gehe durch 0 wenn rest_distance größer als current_number
        # ABER nur wenn current_number nicht 0 ist (sonst starten wir bei 0)
        if rest_distance > current_number and current_number != 0:
            geht_durch_null = True

    # Zähle die Nullen:
    # Wenn wir auf 0 landen UND durch 0 gehen, dann ist es die gleiche 0!
    if landet_auf_null and geht_durch_null:
        counter += 1  # Nur einmal zählen
    elif landet_auf_null:
        counter += 1  # Landen auf 0
    elif geht_durch_null:
        counter += 1  # Durch 0 gehen

# Ergebnis ausgeben
print(f"Das Passwort ist: {counter}")
# Startposition und Counter
position = 150  # Index 150 zeigt auf die Zahl 50
counter = 0

# Durch alle Instructions gehen
for instruction in instructions:
    # Parse Richtung und Distanz
    direction = instruction[0]  # 'L' oder 'R'
    distance = int(instruction[1:])  # Die Zahl nach dem Buchstaben
    
    # Zähle Nullen während der Bewegung
    unterwegs_nullen = distance // 100  # Anzahl kompletter 100er-Runden
    counter += unterwegs_nullen
    
    # Reduziere Distanz für die Position
    distance = distance % 100
    
    # Berechne neue Position
    if direction == 'L':
        neue_position = position - distance
    else:  # direction == 'R'
        neue_position = position + distance
    
    # Erweitere dial-Liste nur wenn out of range
    if neue_position < 0:
        # Füge vorne 100 Elemente hinzu
        neue_elemente = [i % 100 for i in range(100)]
        dial = neue_elemente + dial
        position = position + 100
        neue_position = neue_position + 100
    
    if neue_position >= len(dial):
        # Füge hinten 100 Elemente hinzu
        dial.extend([i % 100 for i in range(100)])
    
    # Bewege Position
    position = neue_position
    
    # Prüfe ob auf 0 gelandet
    if dial[position] == 0:
        counter += 1

# Ergebnis ausgeben
print(f"Das Passwort ist: {counter}")
