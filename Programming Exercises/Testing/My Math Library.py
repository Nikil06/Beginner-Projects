import math

pi = 3.14159265359
e  = 2.71828182846
'''
def log(num: float, base = None)->float:
    if base == None or base == e:
        x = num - 1
        n = 2
        inf_sum = x
        prev_power = x
        while (prev_power*x)/n > 1e-6:
            if n%2 == 0:
                inf_sum += -(prev_power*x)/n
            else:
                inf_sum += (prev_power*x)/n
            #print(inf_sum)
            prev_power *= x
            n += 1
        return inf_sum
'''

def log(x, base=None):
    if x <= 0:
        return float('nan')
    if base is not None and base <= 0:
        return float('nan')
    if base is not None and base == 1:
        return float('nan')
    if x == 1:
        return 0
    if base is not None and x == base:
        return 1

    if base is None or base == math.e:
        # Compute natural logarithm using Taylor series variation
        m = 0
        while x >= 2:
            x /= 2
            m += 1
        f = x - 1
        g = f / (2 + f)
        s = 0
        term = 1
        n = 1
        while abs(term) > 1e-6:
            term *= -g
            s += term / n
            n += 1
        return (m + s) * math.log(2) + math.log(1 + f)

    else:
        # Compute logarithm in base 'base' using change of base formula
        return log(x) / log(base)

for i in range(1, 2050):
    out_1 = log(i)
    out_2 = math.log(i)

    err_percent = 0
    if out_2 != 0:
        err_percent = round(100*((out_2-out_1)/out_2),2)

    print('-'*30)
    print('Number  :', i)
    print('My Func :', out_1)
    print('Lib Func:', out_2)
    print('Error % :', err_percent)
    
