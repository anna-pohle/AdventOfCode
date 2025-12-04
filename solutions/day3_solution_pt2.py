# Input einlesen
with open('day3_input.txt', 'r') as f:
    banks = [line.strip() for line in f]

# Counter initialisieren
counter = 0

# Für jede Bank
for bank in banks:
    # Wie viele Ziffern müssen wir entfernen?
    to_remove = len(bank) - 12
    removed = 0
    
    # Stack für das Ergebnis
    stack = []
    
    # Gehe durch jede Ziffer
    for digit in bank:
        # TODO: Solange:
        #   - stack nicht leer ist UND
        #   - oberste Ziffer im stack < aktuelle digit UND
        #   - wir noch Ziffern entfernen dürfen (removed < to_remove):
        #     → Entferne oberste Ziffer aus stack
        #     → Erhöhe removed um 1
        
        # TODO: Füge aktuelle digit zum stack hinzu
        pass
    
    # Falls wir am Ende zu viele Ziffern haben (sollte nicht passieren bei korrektem Algorithmus)
    # schneide vom Ende ab
    if len(stack) > 12:
        stack = stack[:12]
    
    # Konvertiere Stack zu Zahl
    joltage = int(''.join(stack))
    
    # Addiere zum Counter
    counter += joltage

# Ergebnis ausgeben
print(f"Total output joltage: {counter}")
