import math


def add_num(num_1, num_2):
    return num_1 + num_2


def subtract_num(num_1, num_2):
    return num_1 - num_2


def multiply_num(num_1, num_2):
    return num_1 * num_2


def divide_num(num_1, num_2):
    return num_1 / num_2


def exponent_num(base, power):
    return base ** power


def log_base_e(x: float):
    if x <= 0.0:
        return "Error: Invalid input"
    elif x == 1.0:
        return 0.0
    else:

        y = 0.0
        z = (x - 1.0) / (x + 1.0)
        z2 = z * z
        z_power = z
        term = z_power
        i = 1
        while term > 1e-9:
            y += term
            i += 2
            z_power *= z2
            term = z_power / i
        return 2.0 * y
        '''
        t = float(x - 1.0)
        t_power = t*t
        result = t
        i = 2
        while abs(t_power/i) > 1e-6:
            t_power *= t
            i += 1
            if i % 2 == 0:
                result += t_power/i
            else:
                result -= t_power/i
        return result'''


def log_num(base, num):
    return None

x = 7965985478
print(math.log(x))
print(log_base_e(x))