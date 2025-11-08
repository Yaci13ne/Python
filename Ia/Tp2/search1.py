MyResearchSpace={ 'A': ['B'], 
                 'B': ['C','D'],
                 'C': ['D'], 
                 'D': ['A','E','F','G'], 
                 'E': [],
                 'F': ['E','G'],
                     'G': [],
}

def generer_successeurs(noeud):
    return MyResearchSpace[noeud]


def test_etat_final(noeudC,listF):
    if (noeudC in listF):
        return True
    else:
        return False
    

def search(I, F):
    Open = []    
    Closed = []
    Open.append(I)

    while Open:
        N = Open.pop() 
        Closed.append(N)
        print(N)
        if test_etat_final(N, F):
            return True
        
        for i in generer_successeurs(N):
            if i not in Open and i not in Closed:
                Open.append(i)

    return False


'''la nouvelle stratégie de recherche de cette fonction  :  DFS'''













print(f"search('A',['G']= {search('A',['G'])}")



