string = input().upper()
this_state =[1, 0, 0]

for char in string:
    match char:

        case "A":
            to_swap = this_state
            to_swap[0], to_swap[1]= to_swap[1], to_swap[0]
            this_state = to_swap

        case "B":
            to_swap = this_state
            to_swap[1], to_swap[2]= to_swap[2], to_swap[1]
            this_state = to_swap
        
        case "C":
            to_swap = this_state
            to_swap[0], to_swap[2]= to_swap[2], to_swap[0]
            this_state = to_swap
            
print (this_state.index(1) + 1) #becourse python index start with 0
