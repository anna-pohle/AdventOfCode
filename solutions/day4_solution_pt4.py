# Input einlesen
with open('day4_data.txt', 'r') as f:
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

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    # Überspringe (0,0) - das Feld selbst
                    if dr == 0 and dc == 0:
                        continue

                    # Berechne neue Position
                    new_row = row + dr
                    new_col = col + dc

                    # Prüfe ob in Bounds
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]):
                        # Wenn Nachbar ein @ ist
                        if grid[new_row][new_col] == '@':
                            neighbor_count += 1

            # Wenn weniger als 4 Nachbarn: zugänglich!
            if neighbor_count < 4:
                accessible_count += 1

# Ergebnis ausgeben
print(f"Accessible rolls: {accessible_count}")
