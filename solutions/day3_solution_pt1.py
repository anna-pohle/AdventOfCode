# Input einlesen
with open('day3_input.txt', 'r') as f:
    banks = [line.strip() for line in f]

# Counter initialisieren
counter = 0

# Für jede Bank
for bank in banks:
    # Erster Loop: Finde höchste Ziffer (aber nicht die letzte)
    highest_a = -1
    position_a = -1

    for i in range(len(bank) - 1):  # Bis zur vorletzten Position
        # TODO: Konvertiere bank[i] zu int
        # TODO: Wenn diese Ziffer > highest_a, dann speichere sie
        # TODO: Speichere auch die Position
        pass

    # Zweiter Loop: Finde höchste Ziffer nach position_a
    highest_b = -1

    for i in range(position_a + 1, len(bank)):  # Ab der Position nach highest_a bis Ende
        # TODO: Konvertiere bank[i] zu int
        # TODO: Wenn diese Ziffer > highest_b, dann speichere sie
        pass

    # Berechne Joltage
    joltage = highest_a * 10 + highest_b

    # Addiere zum Counter
    counter += joltage

# Ergebnis ausgeben
print(f"Total output joltage: {counter}")
