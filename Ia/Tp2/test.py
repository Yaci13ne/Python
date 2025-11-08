def gener_successur(N):
    x, y = N.name
    succ = []

    # R1 : fill jar 1
    succ.append(Node((4, y), N, "R1"))
    # R2 : fill jar 2
    succ.append(Node((x, 3), N, "R2"))
    # V1 : empty jar 1
    succ.append(Node((0, y), N, "V1"))
    # V2 : empty jar 2
    succ.append(Node((x, 0), N, "V2"))

    # T12 : pour J1 → J2
    pour = min(x, 3 - y)
    succ.append(Node((x - pour, y + pour), N, "T12"))

    # T21 : pour J2 → J1
    pour = min(y, 4 - x)
    succ.append(Node((x + pour, y - pour), N, "T21"))

    return succ





class Jarre:
    def __init__(self, capacite, quantite=0):
        self.capacite = capacite
        self.quantite = quantite

    def vider(self):
        self.quantite = 0

    def remplir(self):
        self.quantite = self.capacite

    def transvaser(self, autre_jarre):
        espace_dispo = autre_jarre.capacite - autre_jarre.quantite
        quantite_a_verser = min(self.quantite, espace_dispo)

        self.quantite -= quantite_a_verser
        autre_jarre.quantite += quantite_a_verser
