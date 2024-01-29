num = int(input())
key = str(input())

Adrian = 'ABC'
Bruno = 'BABC'
Goran = 'CCAABB'

name = ['Adrian', 'Bruno', 'Goran']
score = [0, 0, 0]

for n in range(num):

    if Adrian[n%3] == key[n]:
        score[0] = score[0]+1

    if Bruno[n%4] == key[n]:
        score[1] = score[1]+1

    if Goran[n%6] == key[n]:
        score[2] = score[2]+1

#print(score)
print(max(score))

if score[0] == max(score):
    print("Adrian")
if score[1] == max(score):
    print("Bruno")
if score[2] == max(score):
    print("Goran")

#print(name[score.index(max(score))])