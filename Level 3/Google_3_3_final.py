#from sys import stdin,stdout
def selectminroute(routesDist, visited):
    maximum=999999999
    initpos= None
    for i in range(0,len(routesDist)):
        for j in range(0,len(routesDist[0])):
            if visited[i][j]==0:
                if routesDist[i][j] < maximum:
                    maximum=routesDist[i][j]
                    initpos=[i,j]
    return initpos
def findMinRoutes(matrix):
    routeDistances=[]
    visited=[]
    maximum=999999999
    for x in matrix:
        row = []
        visitedrow = []
        for y in x:
            row.append(maximum)
            visitedrow.append(0)
        routeDistances.append(row)
        visited.append(visitedrow)
    routeDistances[0][0]=1
    currPos=[0,0]

    while True:
        #checks if goal state reached
        if currPos[0]==len(matrix)-1 and currPos[1]==len(matrix[0])-1:
            return routeDistances[len(matrix)-1][len(matrix[0])-1]
        
        toRight = [currPos[0]+1, currPos[1]]
        toLeft = [currPos[0]-1, currPos[1]]
        toUp = [currPos[0], currPos[1]-1]
        toDown = [currPos[0], currPos[1]+1]
        #checks current distance
        currentdist = routeDistances[currPos[0]][currPos[1]]

        if  toRight[0]<len(matrix) and visited[toRight[0]][toRight[1]]==0: 
            if matrix[toRight[0]][toRight[1]] == 0:
                if currentdist + 1 < routeDistances[toRight[0]][toRight[1]]:
                    routeDistances[toRight[0]][toRight[1]] = currentdist + 1

        if toLeft[0] >= 0 and visited[toLeft[0]][toLeft[1]]==0:
            if matrix[toLeft[0]][toLeft[1]] == 0:
                if currentdist + 1 < routeDistances[toLeft[0]][toLeft[1]]:
                    routeDistances[toLeft[0]][toLeft[1]] = currentdist + 1

        if toUp[1] >= 0 and visited[toUp[0]][toUp[1]]==0:
            if matrix[toUp[0]][toUp[1]] == 0:
                if currentdist + 1 < routeDistances[toUp[0]][toUp[1]]:
                    routeDistances[toUp[0]][toUp[1]] = currentdist + 1

        if toDown[1] < len(matrix[0]) and visited[toDown[0]][toDown[1]]==0:
            if matrix[toDown[0]][toDown[1]] == 0:
                if currentdist + 1 < routeDistances[toDown[0]][toDown[1]]:
                    routeDistances[toDown[0]][toDown[1]] = currentdist + 1
                    
        #mark current as visited
        visited[currPos[0]][currPos[1]]=1
        #calculate minimum route based on distance
        currPos=selectminroute(routeDistances, visited)
        #to prevent value error
        if currPos==None:
            return maximum

def answer(matrix):
    allMinRoutes=[]
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j]==1:
                matrix[i][j]=0
                allMinRoutes.append(findMinRoutes(matrix))
                matrix[i][j]=1
    return min(allMinRoutes)

print answer([[0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0]])
print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
