from Fonctions import *
import csv

class Traitement():
    def __init__(self, deb,fin,lieu,dom):
        self.deb=deb
        self.fin=fin
        self.lieu=lieu
        self.dom=dom

    def search(self):
        csvfichier = open(r'C:\Users\PTWV699\Documents\Python\Open Data Festival\panorama-des-festivals.csv', encoding='utf-8', newline="")
        reader = csv.reader(csvfichier, delimiter=";")

        test1="Ca marche"
        test2="Ca marche pas"
        # nb = compter_nb_elements(csvfichier)

        for row in reader:
            if self.deb!="":
                print("sortie")
                # if verif_date(self.deb)==True:
                if row[14]==self.deb:
                    test1=self.deb
                    return str(test1)
            # elif self.deb=="":
            #     return str(test2)
            # if self.fin!="":
            #     list[1]=self.fin
            # if self.lieu!="":
            #     list[2]=self.lieu
            # if self.dom!="":
            #     list[3]=self.dom

        return test1

    def test_cont(self,test):
        if test=="":
            return str("Critère non communiqué")
        else:
            return str(test)

    def __str__(self):
        return "Voici vos critères de recherche | Date de début : "+self.test_cont(self.deb)+" | Date de fin : "+self.test_cont(self.fin)+" | Localisation : "+self.test_cont(self.lieu)+" | Domaine(s) : "+self.test_cont(self.dom)+"""
        Liste : """+self.search()
