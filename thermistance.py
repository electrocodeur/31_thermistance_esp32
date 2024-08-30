from machine import ADC, Pin
from time import *
import math

B = 3950        # B valeur résistance en fonction de la version du capteur de température Grove
R0 = 10000     # R0 = 10k


can = ADC(Pin(34))               # crée un objet ADC sur la broche 34 (A3)
can.atten(ADC.ATTN_11DB)         # étendue totale : 3.3V


while True:
    a = can.read()                                  # conversion analogique-numérique de la broche A3   0-4095
    R = ((4095/(a+140))-1) * R0                     # calcul résistance (140 pour corriger l'offset du can)          
    temp = 1/(math.log(R/R0)/B+1/298.15)-273.15     # calcul de la température
    temp = round(temp, 1)                           # arrondi au 1/10
    print("température=", temp)                     # affichage sur la console REPL de la valeur numérique
    sleep_ms(500)
