def compter_nb_elements():
    # On part de -1 pour ne pas compter la première qui sert pour les catégories
    elements = -1
    # On compte le nombre de lignes présentes dans le fichier csv
    for ligne in csvfichier:
        elements+=1
    return elements

print(compter_nb_elements())

