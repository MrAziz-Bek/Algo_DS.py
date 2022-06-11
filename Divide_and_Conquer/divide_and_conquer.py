def gcd_residue(a, b):
    if a == 0:
        return b
    return gcd_residue(b % a, a)


def gcd_substract(a, b):
    if a == 0:
        return b
    if a > b:
        a, b = b, a
    return gcd_substract(b - a, a)

if __name__ == "__main__":
    print(gcd_residue(168, 64), 'gcd_residue()')
    print(gcd_substract(168, 64), "gcd_substract()")