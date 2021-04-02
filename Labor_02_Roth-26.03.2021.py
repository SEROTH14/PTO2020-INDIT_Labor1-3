# Schleifenvariable oder Zielvariable = i (j,k)
"""
counter = 10
# 'counter' muss zu beginn vor der Schleife initialisiert werden
while counter >= 0:
# solange der counter >= 0 ist mach das folgende:
    print (counter)
    counter = counter -1 # alternative: counter -= 1
# Um Schleife zu beenden muss counter begrenzt werden, counter - 1 in jedem durchlauf der Schleife
"""

# Addieren Sie in einer Schleife(!) die Zahlen von 1 - 100 und geben Sie das Ergebniss aus.
counter = 0
summe = 0
while counter < 100:
    counter = counter + 1
    #print (counter)
    #Gibt den Counter nach jedem Durchlauf der Schleife wieder.
    summe = summe + counter   
print ('Summe 1 -> 100 = ', summe)    
