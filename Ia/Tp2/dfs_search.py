def dfs_search(I,F):
   open=[]
   closed=[]
   ordreVisite=[]
   open.append(Node(I, None, ""))
   while open:
    N = open.pop()
    ordreVisite.append(N.name)
    if test_etat_final(N, F):
        return True,ordreVisite,getSolution(N)
   else:
    closed.append(N)
    succ = gener_successur(N)
    if len(succ) > 0:
        for s in succ:
            if s.name not in [x.name for x in open] and s.name not in [x.name for x in closed]:
                open.append(s)
            return False,ordreVisite