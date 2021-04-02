# AUFGABE 1

# Schreiben Sie ein Python-Programm, dass
# 1) den Benutzer berüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summe der beiden Zahlen berechnet und ausgibt
# 5) die Diffenenz der kleineren von der größeren Zahl berechnet und ausgibt
# 6) das Produkt der beiden Zahlen berechnet und ausgibt
# 7) den Quotient der kleineren zahl durch größeren Zahl berechnet und ausgibt (inkl. Nachkommastellen)

print ("Hallo und Willkommen lieber Benutzer")
Zahl_1 = input ("Eingabe der ersten Zahl:")
erste_Zahl = float (Zahl_1)
print ("Die Eingabe lautet:" , erste_Zahl)
zweite_Zahl = float (input ("Eingabe der zweiten Zahl:"))
print ("Die Eingabe lautet:" , zweite_Zahl)
# -------------------- Addition --------------------
print ("Summe =", erste_Zahl + zweite_Zahl)
# ------------------ Subtraktion -------------------
if erste_Zahl >= zweite_Zahl:
    print ("Differenz =", erste_Zahl - zweite_Zahl)
elif erste_Zahl < zweite_Zahl:
    print ("Differenz =", zweite_Zahl - erste_Zahl)
# ----------------- Multiplikation -----------------
print ("Produkt =", erste_Zahl * zweite_Zahl)
# -------------------- Division --------------------
if erste_Zahl >= zweite_Zahl:
    print ("Quotient =", erste_Zahl / zweite_Zahl)
elif erste_Zahl < zweite_Zahl:
    print ("Quotient =", zweite_Zahl / erste_Zahl)
