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
        # Konvertiere zu String
        id = str(i)
        
        # Prüfe ob gerade Länge
        if len(id) % 2 == 0:
        
            # Teile in Hälften
            id_a = id[0 : (len(id) // 2)]
            id_b = id[(len(id) // 2):]
            
            #  Prüfe ob beide Hälften gleich sind
            if id_a == id_b:
            # Wenn ja, addiere i zum counter
                counter += i
        else:
            continue
# Ergebnis ausgeben
print(f"Total sum of invalid IDs: {counter}")
