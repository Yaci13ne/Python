from collections import deque


class Node:
    def __init__(self, name, parent, action):
        self.name = name
        self.parent = parent
        self.action = action


def dfs_search(I, F):
    open = []
    closed = []
    ordreVisite = []

    open.append(Node(I, None, ""))

    while open:
        N = open.pop()
        ordreVisite.append(N.name)

        if test_etat_final(N, F):
            return True, ordreVisite, get_solution(N)

        else:
            closed.append(N)
            succ = gener_successur(N)
            if len(succ) > 0:
                for s in succ:
                    if s.name not in [x.name for x in open] and s.name not in [x.name for x in closed]:
                        open.append(s)

    return False, ordreVisite, []




def bfs_search(I, F):
    open = deque()
    closed = []
    ordreVisite = []

    open.append(Node(I, None, ""))

    while open:
        N = open.popleft()
        ordreVisite.append(N.name)

        if test_etat_final(N, F):
            return True, ordreVisite, get_solution(N)

        else:
            closed.append(N)
            succ = gener_successur(N)
            if len(succ) > 0:
                for s in succ:
                    if s.name not in [x.name for x in open] and s.name not in [x.name for x in closed]:
                        open.append(s)

    return False, ordreVisite, []

def test_etat_final(N, F):
    return N.name in F


def gener_successur(N):
    successeurs = []
    for s in MyResearchSpace.get(N.name, []):
        successeurs.append(Node(s, N, None))
    return successeurs


def get_solution(N):
    path = []
    while N is not None:
        path.insert(0, N.name)
        N = N.parent
    return path


MyResearchSpace = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A', 'E', 'F', 'G'],
    'E': [],
    'F': ['E', 'G'],
    'G': [],
}

n = Node('A', None, None)
print([s.name for s in gener_successur(n)])  

print(f'DFS A->F : {dfs_search('A', ['F'])}')
print(f'BFS A->F : {bfs_search('A', ['F'])}')
