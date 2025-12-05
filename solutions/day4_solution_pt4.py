# Input einlesen
with open('day4_input.txt', 'r') as f:
    grid = [line.strip() for line in f]

# Counter initialisieren
accessible_count = 0

# Für jede Zeile
for row in range(len(grid)):
    # Für jede Spalte
    for col in range(len(grid[row])):
        # Prüfe nur @-Felder
        if grid[row][col] == '@':
            # TODO: Zähle die @-Nachbarn in den 8 umgebenden Feldern
            neighbor_count = 0
            
            # TODO: Gehe durch alle 8 Richtungen (-1,0,1 für row und col)
            #       for dr in [-1, 0, 1]:
            #           for dc in [-1, 0, 1]:
            #               - Überspringe (0,0) - das Feld selbst
            #               - Berechne neue Position: new_row = row + dr, new_col = col + dc
            #               - Prüfe ob in Bounds (0 <= new_row < len(grid) etc.)
            #               - Wenn grid[new_row][new_col] == '@': neighbor_count += 1
            
            # TODO: Wenn neighbor_count < 4:
            #           accessible_count += 1

# Ergebnis ausgeben
print(f"Accessible rolls: {accessible_count}")
