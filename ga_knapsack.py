import random


def generatePops(benda,n):
    pops = []
    for i in range(n):
        pops.append([random.randint(0,1) for i in range(len(benda.keys()))])
    return pops    

def calcVal(pop):
    totalVal = 0
    for i,k in enumerate(benda.keys()):
        if pop[i]==1:
            totalVal+=benda[k][0]
    return totalVal

def calcWg(pop):
    totalWg = 0
    for i,k in enumerate(benda.keys()):
        if pop[i]==1:
            totalWg+=benda[k][1]      
    return totalWg

def calcFit(pop):
    return calcVal(pop)/2*calcWg(pop)

def selectedPops(pops,cap):
    selected = []
    for pop in pops:
        if calcWg(pop)<=cap and calcWg(pop)!=0 and pop not in selected:
            selected.append(pop)
    return selected

def selectParents(selected):
    rank = []
    buffer = dict()
    for i,pop in enumerate(selected):
        buffer[calcFit(pop)] = i
    for k in buffer.keys():
        rank.append(k)
    father = selected[buffer[rank[-1]]]
    try:
        mother = selected[buffer[rank[-2]]]
    except:
        mother = father
    return father,mother  
                     

def crossover(father,mother):
    half = round(len(father)/2)
    childs = []
    father_part = [father[0:half],father[half:len(father)]]
    mother_part = [father[0:half],mother[half:len(mother)]]
    for i in range(2):
        for j in range(2):
            if i!=j:
                childs.append(father_part[i]+mother_part[j])
    for i in range(2):
        for j in range(2):
            if i!=j:
                childs.append(father_part[j]+mother_part[i])            
    return childs        

            
"""
mutate the child at the rate of 1%
"""
def mutations(childs):
    rate = [1] + [0]*99
    for i in childs:
        mutate = random.sample(rate,1)[0]
        if mutate==1:
            index = random.randint(0,len(childs)-1)
            childs[index] = random.sample(childs[index],len(childs[0]))
    return childs
 
    
"""
choosing the best breed
"""
def bestPop(newPops):
    newPops = selectedPops(pops,cap)
    bestFit=0
    bestChild = []
    kamus_best = dict()
    for i in newPops:
        k = str(i)
        kamus_best[k] = calcVal(i),calcWg(i),calcFit(i)
        temp = calcFit(i)
        if bestFit<temp:
            bestFit = temp
            bestChild = i
        elif bestFit == temp:
            if calcWg(bestChild)<calcWg(i):
                bestChild=i
    return bestChild,bestFit,kamus_best        


def genetic_main(pops,cap,NCMax):
    pop = pops
    NC = 0
    while NC<NCMax:
        selected = selectedPops(pop,cap)
        f,m = selectParents(selected)
        c = crossover(f,m)
        pop = mutations(c)
        NC+=1    
    return bestPop(pop)

def decode(chromosome,benda):
    hasil = []
    for i,v in enumerate(benda.keys()):
        if chromosome[i]==1:
            hasil.append(v)
    return hasil


if __name__=="__main__":
    benda = {'sepatu': [20, 10], 'buah': [20, 10],'odol':[2,11],'sikat gigi':[20,1],\
             'rokok':[100,5],'buku':[50,10],'sambiloto':[10,30],'playstation':[10,50]\
             ,'sabun':[50,10],'minuman':[10,50],'sambel':[5,10],'makanan ringan':[70,10]}
    
    cap = 100
    pops = generatePops(benda,10000)
    b,k,w = genetic_main(pops,cap,5)    
    print(decode(b,benda))
