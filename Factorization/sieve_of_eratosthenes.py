__author__ = "Surya Pratap Singh"
__python_version__ = "3.7.0"
__maintainer__ = "Surya Pratap Singh"
__email__ = "surya1.singh@gmail.com"

def soe(num):
    "return all prime number less than given number"
    primes = [1]*(num+1)
    primes[0] = primes[1] = 0

    for i in range(2, int(num**0.5)+1):
        if primes[i] == 1:
            for j in range(2,num//i+1):
                primes[i*j] = 0
    return [i for i,n in enumerate(primes) if n == 1]


if __name__ == "__main__":
    print(soe(1))
    print(soe(2))
    print(soe(13))
    print(soe(101))
    print(soe(1001))
