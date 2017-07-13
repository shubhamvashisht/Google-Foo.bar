def travel(totaldist, visited , currpos, matrix , wall):
    #length of matrix_arr
    lenmat=len(matrix)
    #if current position is final position
    if currpos == [len(matrix)-1, len(matrix)-1]:
        return totaldist
    
    #stores distance per direction
    travelledDist=[]
    
    #all posible directions to move, cannot move diagonally
    toRight=[currpos[0]+1,currpos[1]]
    toLeft=[currpos[0]-1,currpos[1]]
    toUp=[currpos[0],currpos[1]-1]
    toDown=[currpos[0],currpos[1]+1]

    #moves recursively to right

    if toRight not in visited and toRight[0]<lenmat:
        if matrix[toRight[0]][toRight[1]]==0:
            visited.append(toRight)
            travelledDist.append(travel(totaldist+1,visited,toRight,matrix,wall))
            visited.pop()
        elif wall==False:
            visited.append(toRight)
            travelledDist.append(travel(totaldist+1,visited,toRight,matrix,True))
            visited.pop()
            
    #moves recursively to left
    if toLeft not in visited and toLeft[0]>=0:
        if matrix[toLeft[0]][toLeft[1]]==0:
            visited.append(toLeft)
            travelledDist.append(travel(totaldist+1,visited,toLeft,matrix,wall))
            visited.pop()
        elif wall==False:
            visited.append(toRight)
            travelledDist.append(travel(totaldist+1,visited,toLeft,matrix,True))
            visited.pop()
            
    #move recursively to up
    if toUp not in visited and toUp[1]>=0:
        if matrix[toUp[0]][toUp[1]]==0:
            visited.append(toUp)
            travelledDist.append(travel(totaldist+1,visited,toUp,matrix,wall))
            visited.pop()
        elif wall==False:
            visited.append(toUp)
            travelledDist.append(travel(totaldist+1,visited,toUp,matrix,True))
            visited.pop()

    #move recursively to down
    if toDown not in visited and toDown[1]<lenmat:
        if matrix[toDown[0]][toDown[1]]==0:
            visited.append(toDown)
            travelledDist.append(travel(totaldist+1,visited,toDown,matrix,wall))
            visited.pop()
        elif wall==False:
            visited.append(toDown)
            travelledDist.append(travel(totaldist+1,visited,toDown,matrix,True))
            visited.pop()
    if len(travelledDist)==0:
        return 9999999999999

    return min(travelledDist)

def answer(matrix):
    #src position
    initpos=[0,0]
    #distance travelled when on src
    initDist=1
    #initially only src pos(0,0) is visited
    visited=[[0,0]]
    return travel(initDist,visited,initpos,matrix,False)


"""matrix=[[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
        [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
        [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
        [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
        [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]"""
print answer([[0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0]])
print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
