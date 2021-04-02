"""
Erstellen Sie ein Python-Programm, das unter Verwendung der Leibniz-Reihe
den Wert der Zahl Pi näherungsweise berechnet. Dabei soll es für den/die BenutzerIn
möglich sein, die Anzahl der Iterationen bei Programmbeginn einzugeben. Am Ende
des Programmlaufs soll der Näherungswert für Pi ausgegeben werden, optional können
auch die Zwischenwerte und Iterationsstufen zur Ausgabe gelangen. Laden Sie den Programmcode
in das Github-Repository aus Teil 1, Aufgabe 2.

Zusätzlich sind auch die Programmdateien mit den
Beispielen 1 (Eingabe zweier Zahlen, Vergleich, arithmetische Berechnungen) und
2 (while-Schleife zur Summenbildung) dort hochzuladen.

Deadline: 2. Mai 2021, Mitternacht."""

N = input ("Eingabe n (Anzahl der zu berechnenden Brüche):")
n = float (N)
Wert = input ("Eingabe für gewünschten Wert:")
wert = float (Wert)
k = (0)
ergebnis = (0)

while k < n:
    ergebnis = ergebnis + (4*((-1)**k)/(2*k+1))
    k = k + 1
    #print (k)
    if wert == k:
        print ("Zwischenergebnis aus Durchlauf:", k, "= ", ergebnis)
print ("Anzahl der berechneten Brüche:", k, "=", ergebnis)
    