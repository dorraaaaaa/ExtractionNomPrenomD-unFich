# 1) Lecture du fichier texte encodé en UTF-16-LE
try:
    f = open("80jours.txt", "r", encoding="utf-16-le")
    lignes = f.readlines()
    f.close()
except FileNotFoundError:
    print("Fichier introuvable")
    exit()
except UnicodeDecodeError:
    print("Erreur d'encodage : le fichier doit être en UTF-16-LE.")
    exit()

# 2) fonction nettoyage
def nettoyer(m):
    return m.strip(",.;:?!()[]{}\"'«»")

# 3) Liste de prénoms connus 
prenoms_connus = {
    "phileas","jean","jules","marie","louis","alexander","sophie",
    "charles","edward","claire","martin","andrew","francis","gauthier",
    "james","joe","john","joseph","samuel","thomas","victor","william"
}

# normaliser en minuscules pour comparer facilement
prenoms_connus = set(p.lower() for p in prenoms_connus)

# 4) Extraction : on n'accepte que si le premier mot est un prénom connu
resultats = []
for ligne in lignes:
    mots = ligne.split()
    for i in range(len(mots) - 1):
        mot1 = nettoyer(mots[i])
        mot2 = nettoyer(mots[i + 1])

        # Conditions : deux mots (Majuscule initiale) et mot2 alphabétique
        if mot1.istitle() and mot2.istitle() and mot2.replace("-", "").isalpha():
            # Vérifier si mot1 est un prénom connu 
            if mot1.lower() in prenoms_connus:
                entree = "Résultat : " + mot1 + " " + mot2
                if entree not in resultats:
                    resultats.append(entree)

# 5) Écriture dans fichier UTF-8 avec BOM
try:
    g = open("resultats_personnes.txt", "w", encoding="utf-8-sig")
    for r in resultats:
        g.write(r + "\n")
    g.close()
except:
    print("Erreur lors de l’écriture du fichier")

print("Extraction terminée. Résultats enregistrés dans resultats_personnes.txt.")
print("Nombre d'entités extraites :", len(resultats))
