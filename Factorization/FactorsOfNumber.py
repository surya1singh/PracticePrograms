__author__ = "Surya Pratap Singh"
__python_version__ = "3.7.0"
__maintainer__ = "Surya Pratap Singh"
__email__ = "surya1.singh@gmail.com"

import datetime
from sieve_of_eratosthenes import soe

def trial_division(num):
    if num < 0:
        return None
    elif num < 2:
        return [num]
    else:
        solution = [1,num]
    for i in range(2,num//2+1):
        if num%i == 0:
            solution.append(i)
    return solution


def optimiz_trial_division(num):
    solution = [1,num]
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            solution.append(i)
            if i*i != num:
                solution.append(num//i)
    return solution


def prime_factorization(num):
    "return all prime factors of number with count"
    solution = []
    i = 2
    for i in range(2,num//2+1):
#    while num > 1:
        ct = 0
        while num%i == 0:
            num = num//i
            ct += 1
        if ct:
            solution.append([i,ct])
        i += 1
        if num == 1:
            break
    return solution

def prime_factorization_using_soe(num):
    "return all prime factors of number with count"
    solution = []
    primes = soe(num//2+1)
    for i in primes:
        ct = 0
        while num%i == 0:
            num = num//i
            ct += 1
        if ct:
            solution.append([i,ct])
        if num == 1:
            break
    return solution



if __name__ == "__main__":
    st = datetime.datetime.now()
    print(trial_division(1))
    print(trial_division(2))
    print(trial_division(10))
    print(trial_division(1282))
    print(trial_division(12312425))
    print(trial_division(198632728))
    print("total microseconds trial_division: ", (datetime.datetime.now()-st).microseconds)

    st = datetime.datetime.now()
    print(optimiz_trial_division(1))
    print(optimiz_trial_division(2))
    print(optimiz_trial_division(10))
    print(optimiz_trial_division(1282))
    print(optimiz_trial_division(12312425))
    print(optimiz_trial_division(198632728))
    print("total microseconds optimiz_trial_division: ", (datetime.datetime.now()-st).microseconds)

    st = datetime.datetime.now()
    print(prime_factorization(1))
    print(prime_factorization(2))
    print(prime_factorization(10))
    print(prime_factorization(1282))
    print(prime_factorization(12312425))
    print(prime_factorization(198632728))
    print(prime_factorization(1680701576121023221767680707955313575515351815549339943291174422040502801585613647025935845139938576898870319522250970335771118093482752517102287789820548241008363379192275740146686781116757117688030825751017332757211573677641671814902971889422562574003718123612949957218193216810604477568616635660271189307917571167790582431116019239910514005361443538244960528445930721450847883046327079766917746710724001642237376752793965824064409943))
    print("total microseconds prime_factorization: ", (datetime.datetime.now()-st).microseconds)

    st = datetime.datetime.now()
    print(prime_factorization_using_soe(1))
    print(prime_factorization_using_soe(2))
    print(prime_factorization_using_soe(10))
    print(prime_factorization_using_soe(1282))
    print(prime_factorization_using_soe(12312425))
    print(prime_factorization_using_soe(198632728))
    print("total microseconds prime_factorization: ", (datetime.datetime.now()-st).microseconds)
