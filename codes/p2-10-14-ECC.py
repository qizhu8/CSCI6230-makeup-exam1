#!/usr/bin/env python3

from ECC_Class import ECC
import Number_Package as npkg

# ecc = ECC([9, 17], 23)
ecc = ECC([1, 7], 11)

print(ecc)

P = [3, 2]

for i in range(13):
    Q = ecc.multiply(P, i+1)
    print(str(i+1) +"G & (" + str(Q[0]) + "," + str(Q[1]) + ")")


# 10-15
G = (3, 2)
nB = 7
Pm = (10, 7)
k = 5

PB = ecc.multiply(G, nB)

Cm = [ecc.multiply(G, k), ecc.add(Pm, ecc.multiply(PB, k))]
print(Cm)

Pm_dec = ecc.minus(Cm[1], ecc.multiply(Cm[0], nB))
print(Pm_dec)
