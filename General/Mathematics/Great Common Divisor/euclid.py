def gcd(a, b):

    if (a == 0):
        return b
    if (b == 0 ):
        return a

    if (a == b):
        return a

    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)


if __name__ == '__main__':
    a = 66528
    b = 52920
    if(gcd(a, b)):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print('not found')
