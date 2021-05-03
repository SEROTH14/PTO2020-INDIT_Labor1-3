# 1) Eingabe Suchbegriffe (deutsch)
# 2) Bestimmung der Gesamtzahl der Elemente (= maximaler Index)
# 3) Schleife: Vergleich Eingabe mit jew. Listenelement
# 4) Wenn Element gefunden -> Index Speichern
# 5) Zugriff auf Listenelement [Index] in Liste (enlisches Wörterbuch)


woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich", "Annanas", "Erdberre"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach", "pineapple", "strawberry"]

# -------------------- X --------------------

sbegriff = input ("Eingabe des gewünschten Begriffes:")
suchbegriff = sbegriff.lower()

# -------------------- X --------------------

laenge = len(woerterbuch_deutsch)
length = len(woerterbuch_english)

# -------------------- X --------------------

j = 0
i = 0
while i < laenge or j < length:
    
    if woerterbuch_deutsch[i].lower() == suchbegriff:
        print("Die Übersetzung Ihres Begriffes lautet:", woerterbuch_english[i], "EN")
        break
    i = i + 1
    
    if i == laenge:
        print ("Begriff konnte nicht gefunden werden!")
        
# -------------------- X -------------------- 
        
    if woerterbuch_english[j] == suchbegriff:
        print("Die Übersetzung Ihres Begriffes lautet:", woerterbuch_deutsch[j], "DE")
        break
    j = j + 1
    
    if j == length:
        print ("Definition could not be found!")

    
