from math import sqrt
import numpy as np
C = 50
H = 30
D = float(input("Veuillez saisir la valeur de D :"))
Q = sqrt((2*C*D)/H)
print(int(Q))