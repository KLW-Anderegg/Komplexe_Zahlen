import math
class komplex:
    def __init__(self, re, im):
        self.re = re
        self.im = im
        self.betrag = math.sqrt(re**2+im**2)
        if self.re > 0:
            self.arg = math.atan(self.im / self.re)
        elif self.re < 0:
            self.arg = math.atan(self.im / self.re) + math.pi
        elif self.re == 0 and self.im > 0:
            self.arg = math.pi / 2
        elif self.re == 0 and self.im < 0:
            self.arg = - math.pi / 2
        else:
            self.arg = None
      
    def __str__(self):
        if self.im == 0:
            normalform = str(self.re)
        elif self.im < 0:
            normalform = str(self.re) + "" + str(self.im) + "i"
        else:
            normalform = str(self.re) + "+" + str(self.im) + "i"
        
        polarform = str(self.betrag) + "cis(" + str(self.arg) + ")"

        return normalform + " oder  " + polarform

    def plus(self,w):
        return komplex (self.re + w.re, self.im + w.im)

    def minus(self, w):
        return komplex (self.re - w.re, self.im - w.im)
    
    def mal(self, w):
        return komplex (self.re * w.re - self.im * w.im, self.im * w.re + self.re * w.im)

    def durch(self, w):
        return komplex ((self.re * w.re + self.im * w.im)/(w.im**2 + w.re**2), (self.im * w.re - self.re * w.im)/(w.im**2 + w.re**2))
    
    def konjugiert(self):
        return komplex(self.re, -self.im)



z = komplex(1,1)
print(z)
w = komplex(2,3)
print(z.plus(w))

print(w.plus(z.konjugiert().mal(z)))
# w = komplex(5,12)

# print(z.plus(w))
# print(z.minus(w))
# print(z.mal(w))
# print(z.durch(w))
# print(w.konjugiert())
