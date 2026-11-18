import math
def 一元二次(a,b,c):
    if b**2-4*a*c<0:
        return False
    elif b**2-4*a*c==0:
        x1=-b/(2*a)
        x2=-b/(2*a)
        return x1,x2
    else:
        x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2
print("一元二次(1,3,-4)",一元二次(1,3,-4))