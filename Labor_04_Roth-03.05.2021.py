# 1) Eingabe Suchbegriffe (deutsch)
# 2) Bestimmung der Gesamtzahl der Elemente (= maximaler Index)
# 3) Schleife: Vergleich Eingabe mit jew. Listenelement
# 4) Wenn Element gefunden -> Index Speichern
# 5) Zugriff auf Listenelement [Index] in Liste (enlisches Wörterbuch)

# 6) Erweitern sie das Wörterbuch-Beispiel um die Möglichkeit, Einträge zu egänzen bzw. zu löschen
# 7) Ändern sie das Wörterbuch-Beispiel so, dass Sie anstelle der Listen Dictionaries verwenden. Mittels try/except
#    soll die Abfrage nach nicht-existenten Bgriffen fehlerfrei gestaltet werden, bzw. die wahlweise Eingabe von deutschen
#    oder englischen Begriffen möglich sein. Ein Ergänzen bzw. Löschen von Begriffen ist nicht gefordert.

running = True

while True:
    woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich", "Annanas", "Erdbeere"]
    woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach", "pineapple", "strawberry"]

    laenge = len(woerterbuch_deutsch)
    length = len(woerterbuch_english)

# -------------------- X --------------------

    awahl = input("Auswahl einer Aktion: [E]infügen, [L]öschen, [S]uchen, [B]eenden  -")
    auswahl = awahl.lower()

# -------------------- X -------------------- Einfügen

    if auswahl == 'e' :
        sprach = input("Eingabe in welcher Sprache: [D]eutsch oder [E]nglisch ?  -")
        sprache = sprach.lower()
        
        if sprache == 'd':
            eingabe = input("Eingabe des deutschen Wortes:")
            woerterbuch_deutsch.append(eingabe)
        
            übersetzung = input ("Eingabe der passenden Übersetzung:")
            woerterbuch_english.append(übersetzung)
            print (woerterbuch_deutsch)
            print (woerterbuch_english)
        
        elif sprache == 'e':
            intake = input("Eingabe des englischen Wortes:")
            woerterbuch_english.append(intake)
        
            translation = input ("Eingabe der passenden Übersetzung:")
            woerterbuch_deutsch.append(translation)
        
            print (woerterbuch_english)
            print (woerterbuch_deutsch)
        
# -------------------- X -------------------- Löschen

    elif auswahl == 'l' :
        print (woerterbuch_english)
        print (woerterbuch_deutsch)

        entf = input ("Eingabe des zu entfernenden Begriffes:")
        entfernen = entf.lower()
    
        k = 0
        o = 0
        while o < laenge or k < length:
    
            if woerterbuch_deutsch[o].lower() == entfernen:
                print(entfernen, "und", woerterbuch_english[o], "werden aus den Wörtebüchern gelösch")
                woerterbuch_deutsch.remove (woerterbuch_deutsch[o])
                woerterbuch_english.remove (woerterbuch_english[o])
                print (woerterbuch_english)
                print (woerterbuch_deutsch)
                break
            o = o + 1
            
            if o == laenge:
                print ("Begriff ist nicht Enthalten!")
    
            if woerterbuch_english[k] == entfernen:
                print (entfernen, "and", woerterbuch_deutsch[k], "will be removed from list")
                woerterbuch_deutsch.remove (woerterbuch_deutsch[k])
                woerterbuch_english.remove (woerterbuch_english[k])
                print (woerterbuch_english)
                print (woerterbuch_deutsch)
                break
            k = k + 1
            
            if k == length:
                print ("Submission is not included!")
    
# -------------------- X -------------------- Suchen

    elif auswahl == 's' :

        sbegriff = input ("Eingabe des gewünschten Begriffes:")
        suchbegriff = sbegriff.lower()

        j = 0
        i = 0
        while i < laenge or j < length:
    
            if woerterbuch_deutsch[i].lower() == suchbegriff:
                print("Die Übersetzung Ihres Begriffes lautet:", woerterbuch_english[i], "EN")
                break
            i = i + 1
    
            if i == laenge:
                print ("Begriff konnte nicht gefunden werden!")
        
            if woerterbuch_english[j] == suchbegriff:
                print("Die Übersetzung Ihres Begriffes lautet:", woerterbuch_deutsch[j], "DE")
                break
            j = j + 1
    
            if j == length:
                print ("Definition could not be found!")
                    
# -------------------- X -------------------- Beenden

    elif auswahl == 'b' :
        break 
    
