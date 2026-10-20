import math
def quadratic(a, b, c):
    if b*b-4*a*c<0:
        return 
    elif b*b-4*a*c==0:
        return -b/(2*a)
    else:
        return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))