class Etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = note

    def mention(self):
        cases = [
            (lambda note: note < 10, "Ajourné"),
            (lambda note: 10 <= note < 12, "Passable"),
            (lambda note: 12 <= note < 14, "Assez Bien"),
            (lambda note: 14 <= note < 16, "Bien"),
            (lambda note: note >= 16, "Très Bien"),
        ]
        for condition, texte in cases:
            if condition(self.note):
                return texte  

    def afficher_infos(self):
        return f"Nom: {self.nom}, Âge: {self.age}, Note: {self.note}, Mention: {self.mention()}"

    def rechercher_etudiant(liste_etudiants, nom_etudiant):
        trouve = False
        print(f"\nRésultats de la recherche pour le nom '{nom_etudiant}':")
        for etu in liste_etudiants:
            if etu.nom.lower() == nom_etudiant.lower():
                print(etu.afficher_infos()) 
                trouve = True
        if not trouve:
            print("Aucun étudiant trouvé avec ce nom.")



liste = [
    Etudiant("Yacine", 20, 15),
    Etudiant("Amina", 22, 9),
    Etudiant("Omar", 19, 17)
]

Etudiant.rechercher_etudiant(liste, "yacine")

print("\nÉtudiants avec mention 'Bien' ou plus :")
for etu in liste:
    if etu.note >= 14:
        print(etu.afficher_infos())
