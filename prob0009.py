number = list(map(int, input().split(" ")))
number = sorted(number)
string = input("").upper()
line = ""
for char in string:
    match char:
        case "A":
           line = line + str(number[0]) + " "
        case "B":
           line = line + str(number[1]) + " "
        case "C":
           line = line + str(number[2]) + " "
print(line)