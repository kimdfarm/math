import math
import sympy as sp
x = sp.Symbol('x')
def Taylor(n=10, TN =x):
    ty = type(TN)
    l = 0
    if ty != int:
        if TN==x:
            for i in range(n+1):
                ft = sp.factorial(i)
                dx = x**(i)
                dt = dx/ft
                l = l+dt
            return l
        else:
            for i in range(n + 1):
                Ty = sp.diff(TN,x,i)
                l = l+Ty
            return l
    else:
        for i in range(n+1):
            ft = sp.factorial(i)
            dx = TN**(i)
            dt = dx/ft                
            l = l+dt
            
        f_return = l.subs(x, TN)
        return l

