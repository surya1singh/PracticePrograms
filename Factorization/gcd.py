def euclid_gcd(a,b):
    if b > a:
        return euclid_gcd(b,a)
    elif a == b:
        return a
    elif a%b == 0:
        return b
    else:
        return euclid_gcd(b, a%b)


if __name__ == "__main__":
    print(euclid_gcd(1,2))
    print(euclid_gcd(5,5))
    print(euclid_gcd(12, 36))
    print(euclid_gcd(45, 35))
    print(euclid_gcd(907, 101))
