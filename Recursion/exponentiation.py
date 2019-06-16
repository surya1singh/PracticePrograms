__author__ = "Surya Pratap Singh"
__python_version__ = "3.7.0"
__maintainer__ = "Surya Pratap Singh"
__email__ = "surya1.singh@gmail.com"

import datetime

def pow(num, exponent):
    if exponent == 1:
        return num
    else:
        return num * pow(num, exponent-1)

def pow_optimized(num, exponent):
    if exponent == 1:
        return num
    if exponent%2 == 0:
        x = pow_optimized(num, exponent//2)
        return x*x
    else:
        return num * pow_optimized(num, exponent-1)

if __name__ == "__main__":
    st = datetime.datetime.now()
    x = (pow(3**2000, 512))
    print("total microseconds pow: ", (datetime.datetime.now()-st).microseconds)

    st = datetime.datetime.now()
    x = (pow_optimized(3**2000, 512))
    print("total microseconds pow_optimized: ", (datetime.datetime.now()-st).microseconds)
