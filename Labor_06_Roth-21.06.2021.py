# 1) Ändern Sie das Wörterbuch-Beispiel so, dass Sie den Code unter Verwendung von Funktionen
#    (Unterprogrammen) strukturieren. Beispielsweise könnten Sie jeweils ein Unterprogramm für
#    die jeweiligen Funktionalitäten erstellen:
#
# 2) Funktion zur Eingabe des Befehls
# 3) Funktion zur Eingabe des Suchbegriffs bzw. Wortes
# 4) Funktion zur Suche
# 5) Funktion zur Ausgabe

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich", "Annanas", "Erdbeere"]
woerterbuch_englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach", "pineapple", "strawberry"]

# -------------------- X --------------------

def addWord(deutschesWort, englischesWort):
    try:
        searchWord(deutschesWort)
        print("Wort bereits vorhanden")
    except:
        woerterbuch_deutsch.append(deutschesWort)
        woerterbuch_englisch.append(englischesWort)

# -------------------- X --------------------

def searchWord(wordInput):
    index = 0
    for wort in woerterbuch_deutsch:  
        if wordInput.lower() == wort.lower():  
            break
        index +=1   
    
    if index == len(woerterbuch_deutsch):
        index=0
        for wort in woerterbuch_englisch:     
            if wordInput.lower() == wort.lower():
                break
            index +=1    
        
        if index == len(woerterbuch_englisch):
            raise Exception("Dieses Wort steht nicht im Wörterbuch")
    return (woerterbuch_deutsch[index], woerterbuch_englisch[index], index)

# -------------------- X --------------------

def delWord():
    try:
        output = searchWord(input("Welches Wort wollen Sie löschen?: "))
        woerterbuch_deutsch.remove(output[0])
        woerterbuch_englisch.remove(output[1])
    except Exception as e:
        print(e)

# -------------------- X --------------------

def getWord():
    try:
        output = searchWord(input("Welches Wortwollen Sie übersetzen: "))
        print(output[0], "DE")
        print(output[1], "EN")
    except Exception as e:
        print(e)

# -------------------- X --------------------

def eingabeBefehl():
    while True:
        auswahl = input("Auswahl einer Aktion, [E]infügen, [L]öschen, [S]uche, [B]eenden - ")
        if auswahl.lower() == "e" or  auswahl.lower() =="l" or auswahl.lower() =="s" or auswahl.lower() =="b":
            return auswahl.lower()
        else:
            print("Falsche Eingabe!")
    
# -------------------- X --------------------

while True:
    auswahl = eingabeBefehl()
    if auswahl == "e":
        addWord(input("Deutsches Wort eingeben: "), input("Englisches Wort eingeben: "))
        
        print(woerterbuch_deutsch)
        print(woerterbuch_englisch)
        
# -------------------- X --------------------        
        
    elif auswahl == "l":
        delWord()
        
        print(woerterbuch_deutsch)
        print(woerterbuch_englisch)
        
# -------------------- X --------------------        
        
    elif auswahl == "b":
        break
    
# -------------------- X --------------------

    else:
        getWord()

        print(woerterbuch_deutsch)
        print(woerterbuch_englisch)
    