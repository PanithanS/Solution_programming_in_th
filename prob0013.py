list = []
for _ in range(9):
    list.append(int(input()))

sum_num = sum(list)

for i in range(9):
    for j in range(9):
        
        res = sum_num - (int(list[i])+int(list[j]))

        if res == 100:
            index = [i, j]
            break

for i in range(9):
    if i not in index:
        print(list[i])