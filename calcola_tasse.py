# 2019, basato su https://www.informazionefiscale.it/aliquote-scaglioni-irpef-2019

import math  

inps = 0.24 # valore percentuale quota inps (questo è il valore per la cassa previdenziale Artigiani e Commercianti)
tassa_regionale = 0.0124 # valore percentuale tassa regionale (questo è il valore per la regione Piemonte)
addizionale_regionale = 0.021 # valore percentuale addizionale regionale (questo è il valore per la regione Piemonte)
tassa_comunale = 0.08 # valore percentuale tassa comunale (questo è il valore per il comune di Torino)

lordo = int(input("Qual è il tuo reddito lordo? "))
irpef = 0
scaglione = 0
deduzioni = int(input("Qual è il totale delle tue spese deducibili dal reddito imponibile? "))
detrazioni = int(input("Qual è il totale delle tue spese detraibili dalle imposte? "))
inps_tot = lordo * inps

imponibile = lordo - (lordo * inps) - deduzioni
tax_reg = imponibile * tassa_regionale
add_reg = imponibile * addizionale_regionale
tax_com = imponibile * tassa_comunale

if imponibile <= 15000:
    irpef = imponibile *0.23
    scaglione = 1
elif imponibile <= 28000:
    irpef = 3450 + ((imponibile - 15000) *0.27)
    scaglione = 2
elif imponibile <= 55000:
    irpef = 6960 + ((imponibile - 28000) *0.38)
    scaglione = 3
elif imponibile <= 75000:
    irpef = 17220 + ((imponibile - 55000) *0.41)
    scaglione = 4
else:
    imponibile = 25420 + ((imponibile - 75000) *0.43)
    scaglione = 5

#netto = imponibile - (irpef - detrazioni)
netto = lordo - inps_tot - irpef - tax_reg - add_reg - tax_com + detrazioni
mensile = netto/12

print("Irpef dovuta (stima): ", round(irpef,2))
print("Scaglione: ", scaglione)
print("Inps dovuta (stima): ", round(lordo * inps,2))
print("Stima del netto: ", round(netto,2))
print("Stima del mensile: ", round(mensile,2))
