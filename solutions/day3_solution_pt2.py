# Input einlesen
with open('day3_data.txt', 'r') as f:
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
        # Solange stack nicht leer ist UND oberste Ziffer im stack < aktuelle digit UND es dürfen noch Ziffern entfernt werden
        while stack != [] and stack[-1] < digit and removed < to_remove:
            stack.pop() # Entferne oberste Ziffer aus stack
            removed += 1 # inkrementiere removed
        # Füge aktuelle digit zum stack hinzu
        stack.append(digit)

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
