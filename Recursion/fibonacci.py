__author__ = "Surya Pratap Singh"
__python_version__ = "3.7.0"
__maintainer__ = "Surya Pratap Singh"
__email__ = "surya1.singh@gmail.com"

import datetime

def fibonacci(num):
    if num < 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

d = {0:1, 1:1}
def fibonacci_memorization(num):
    global d
    if d.get(num):
        return d[num]
    d[num] = fibonacci_memorization(num-2) + fibonacci_memorization(num-1)
    return d[num]

if __name__ == "__main__":
    st = datetime.datetime.now()
    print(fibonacci(10))
    print(fibonacci(20))
    print(fibonacci(30))
    print(fibonacci(35))
    print("total microseconds fibonacci: ", (datetime.datetime.now()-st).microseconds)

    st = datetime.datetime.now()
    print(fibonacci_memorization(10))
    print(fibonacci_memorization(20))
    print(fibonacci_memorization(30))
    print(fibonacci_memorization(35))
    print(fibonacci_memorization(100))
    print("total microseconds fibonacci_memorization: ", (datetime.datetime.now()-st).microseconds)
