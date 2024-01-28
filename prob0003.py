m , n = map(int,input().split())

mattrix_a = []
mattrix_b = []

for i in range(m):
    r = list(map(int,input().split()))
    mattrix_a.append(r)

for i in range(m):
    r = list(map(int,input().split()))
    mattrix_b.append(r)

mattrixl_result = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(mattrix_a[i][j]) + int(mattrix_b[i][j]))
    mattrixl_result.append(row)

#print (mattrixl_result)

for r in mattrixl_result:
   print(" ".join(map(str,r)))