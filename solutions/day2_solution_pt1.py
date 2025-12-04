# Input einlesen
with open('day2_input.txt', 'r') as f:
    line = f.read().strip()

# Counter initialisieren
counter = 0

# Splitte am Komma um Ranges zu bekommen
ranges = line.split(',')

# Für jeden Range
for range_str in ranges:
    # Splitte am Strich um Start und Ende zu bekommen
    start, end = range_str.split('-')
    start = int(start)
    end = int(end)
    
    # Für jede Zahl im Range
    for i in range(start, end + 1):
        # TODO: Konvertiere zu String
        
        # TODO: Prüfe ob gerade Länge
        
        # TODO: Teile in Hälften
        
        # TODO: Prüfe ob beide Hälften gleich sind
        
        # TODO: Wenn ja, addiere i zum counter

# Ergebnis ausgeben
print(f"Total sum of invalid IDs: {counter}")
