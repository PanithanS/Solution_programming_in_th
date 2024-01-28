list = map(int, input().split(" "))

def gcd(list):
    list = sorted(list)
    a = int(list[0])
    b = int(list[1])
    if b%a == 0:
        return a
    list = [a, b%a]
    return gcd(list)

val = gcd(list)
print(val)