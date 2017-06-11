def answer(num):
    moves = 0
    binfy = bin(int(num))[2:]
    #f = bin(int(n))
    #print(b)
    while len(binfy) > 1:
        moves += 1
        #print("moves",moves)
        if binfy[-1] == '0':
            binfy = binfy[:-1]
            #print(binfy[:-1])
            #print(binfy)
        elif binfy[-2] == '1':
            #special case for '3'
            if binfy == '11':
                moves += 1
                binfy = '1'
            else:
                binfy = bin(int(binfy,2) + 1)[2:]
        else:
            binfy = bin(int(binfy,2)-1)[2:]
    return moves

#print(answer('15'))
#print(answer('4'))
