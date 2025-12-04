# Input einlesen
with open('day3_data.txt', 'r') as f:
    banks = [line.strip() for line in f]

# Counter initialisieren
counter = 0

# Für jede Bank
for bank in banks:
    # Erster Loop: Finde höchste Ziffer (aber nicht die letzte)
    highest_a = -1
    position_a = -1
    
    for i in range(len(bank) - 1):  # Bis zur vorletzten Position
        digit = int(bank[i])
        if digit > highest_a:
            highest_a = digit
            position_a = i
    
    # Zweiter Loop: Finde höchste Ziffer nach position_a
    highest_b = -1
    
    for i in range(position_a + 1, len(bank)):  # Ab der Position nach highest_a bis Ende
        digit = int(bank[i])
        if digit > highest_b:
            highest_b = digit
    
    # Berechne Joltage
    joltage = highest_a * 10 + highest_b
    
    # Addiere zum Counter
    counter += joltage

# Ergebnis ausgeben
print(f"Total output joltage: {counter}")
