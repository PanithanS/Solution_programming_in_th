hw = int(input())
mid = int(input())
fin = int(input())

sum = hw+mid+fin
if sum >= 80:
    print("A")
elif sum >= 75:
    print("B+")
elif sum >= 70:
    print("B")
elif sum >= 65:
    print("C+")
elif sum >= 60:
    print("C")
elif sum >= 55:
    print("D+")
elif sum >= 50:
    print("D")
elif sum <= 49:
    print("F") 