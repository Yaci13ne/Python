class jarre : 
    def __init__(self,capacite,quantite):
        self.capacite=capacite
        self.quantite=quantite

    def vider(self):
        self.quantite=0

    def remplir(self):
        self.quantite=self.capacite

    def transvaser(self,autre_jarre):
        espace = autre_jarre.capacite - autre_jarre.quantite
        q_transvaser = min(self.quantite,espace)    
        self.quantite -= q_transvaser
        autre_jarre.quantite += q_transvaser




#main
R1=jarre(4,0)
R2=jarre(3,0)



'''Considérons le problème suivant :Vous disposez de deux jarres : l'une de 4 litres et l'autre de 3 litres. L'objectif est d'obtenir exactement 2 litres d'eau, sans avoir d'unité de mesure spécifique. Pour cela, vous pouvez réaliser les opérations suivantes (sans contraintes sur la quantité d'eau disponible) :
•Vider la première jarre : V1.
•Vider la deuxième jarre : V2.
•Remplir la première jarre :R1.
•Remplir la deuxième jarre :R2.
•Transvaser le contenu la première jarre la deuxième : T12.
•Transvaser le contenu la deuxième jarre la première : T12.
Les deux jarres sont initialement vides.
Les tâches à accomplir :
1.Modéliser ce problème pour qu’il puisse être résolu par un algorithme de recherche.
2.Adapter les programmes développés dans ce TP afin de résoudre ce problème.'''