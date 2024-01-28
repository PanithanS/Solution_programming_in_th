import math

r = int(input())

cir_area = math.pi*r**2
taxi_area = 0.5 * r**2 * 4 # area of Box in circle 


print("{:.6f}".format(cir_area))
print("{:.6f}".format(taxi_area))