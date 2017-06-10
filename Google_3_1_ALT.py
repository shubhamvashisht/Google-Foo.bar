def answer(probmatrix):
    byCol=len(probmatrix)
    byRow=len(probmatrix[0])
    mat=list(probmatrix)
    for i,elem in enumerate(mat):
        elem[i]=0
    lissum=[sum(i) for i in mat]
    terminals=[i for i,item in enumerate(lissum) if item==0]
    not_terminals=list((set(range(byCol)) - set(terminals)))
    L=len(not_terminals)
    for i in range(0,L-1):
        init_elem_each=not_terminals[L-i-1]
        for j in range(0,L-1):
            init_elem=not_terminals[j]
            #print("mat[init_elem]:before",mat[init_elem])
            mat[init_elem]=backTrace(mat[init_elem],init_elem,mat[init_elem_each],init_elem_each)
            #print("mat[init_elem]:after",mat[init_elem])
    finalizedlis=[]
    for i in terminals:
        finalizedlis.append(mat[0][i])
    tot=sum(finalizedlis)
    finalizedlis.append(tot)
    if tot == 0:
        finalizedlis=[1 for i in terminals]
        finalizedlis.append(len(terminals))
    return finalizedlis

def backTrace(mat_in_elem,index1,mat_in_elem_each,index2):
    lenV=len(mat_in_elem)
    indices=(set(range(lenV))-{index1,index2})
    sum2=sum(mat_in_elem_each)
    out = [0 for i in mat_in_elem]
    for i in indices:
        out[i]= sum2*mat_in_elem[i]+mat_in_elem[index2]*mat_in_elem_each[i]
    gc=gcdfyList(out)
    finalizedlis = [int( i / gc ) for i in out ]
    return finalizedlis
    

def gcdSimple (a,b):
    if (b == 0):
        return a
    else:
        return gcdSimple (b, a % b)
         
def gcdfyList(lst):
    L=len(lst)
    out=0
    for i in range(0,L):
        out=gcdSimple(out,lst[i])
    return out
