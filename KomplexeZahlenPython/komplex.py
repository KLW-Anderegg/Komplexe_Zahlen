# Idee: Fasse z = a+bi als Liste [a,b] auf
import math

def c_print(z):
    if z[1] < 0:
        print(str(z[0]) + "" + str(z[1]) + "i")
    elif z[1] == 0:
        print(str(z[0]))
    else:
        print(str(z[0]) + "+" + str(z[1]) + "i")



def c_summe(z, w):
    return [z[0]+w[0] , z[1]+w[1]]

def c_differenz(z, w):
    return [z[0]-w[0] , z[1]-w[1]]

def c_produkt(z, w):
    return [z[0]*w[0] - z[1] * w[1], z[1]*w[0] + z[0] * w[1]]

def c_quotient(z, w):
    return [(z[0]*w[0] + z[1] * w[1]) / (w[0]**2 + w[1]**2), (z[1]*w[0] - z[0] * w[1]) / (w[0]**2 + w[1]**2)] 

def c_betrag(z):
    return  math.sqrt((z[0]**2 + z[1]**2))

def c_konjugiert(z):
    return  [z[0], -z[1]]



z = [-3,-5]
w = [5, 12]
c_print(w)

c_print(c_produkt(z,w))
c_print(c_quotient(z,w))
print(c_betrag(w))