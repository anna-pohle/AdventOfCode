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
        id_str = str(i)
        id_len = len(id_str)
        
        # Flag für ungültige ID
        ist_ungueltig = False
        
        # Teste alle möglichen Pattern-Längen (Teiler von id_len)
        for pattern_len in range(1, id_len):
            # Prüfe ob pattern_len ein Teiler von id_len ist
            if id_len % pattern_len == 0:
                
                # Wenn ja, nimm die ersten pattern_len Zeichen als Pattern
                pattern = id_str[:pattern_len]
                # Berechne wie oft das Pattern wiederholt werden muss
                wiederholungen = id_len // pattern_len
                # Wiederhole das Pattern entsprechend oft
                wiederholtes_pattern = pattern * wiederholungen
                # Prüfe ob das wiederholte Pattern gleich id_str ist
                if wiederholtes_pattern == id_str:
                    # Wenn ja, setze ist_ungueltig = True und brich ab
                    ist_ungueltig = True
                    break 
                
        # Wenn ungültig, addiere zum Counter
        if ist_ungueltig:
            counter += i

# Ergebnis ausgeben
print(f"Total sum of invalid IDs: {counter}")
