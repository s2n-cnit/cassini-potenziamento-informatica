import math


import math

def cerchio(r):
    print("Area", r*r*math.pi)
    print("Circonferenza" 2*math.pi*r)

def quadrato(l):
    print("Area", l*l)
    print("Perimetro" 4*l)

def rettangolo(a, b):
    print("Area", a*b)
    print("Perimetro", 2*(a+b))

def triangolo(a, b, c):
    p = (a+b+c)/2
    print("Area", math.sqrt(p*(p-a)*(p-b)*(p-c)))
    print("Perimetro" a+b+c)
