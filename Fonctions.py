from datetime import datetime

def compter_nb_elements(csvfichier):
    # On part de -1 pour ne pas compter la première qui sert pour les catégories
    elements = -1
    # On compte le nombre de lignes présentes dans le fichier csv
    for ligne in csvfichier:
        elements+=1
    return elements

def verif_date(d):
    if len(d) == 10:
        vd=datetime.now()
        dt=vd.strftime('%Y-%m-%d')
        print(dt)
        part=d[0]+d[1]+d[2]+d[3]
        partd=dt[0]+dt[1]+dt[2]+dt[3]
        if part.isdigit()==True and int(part)<int(partd):
            if d[4]=="-":
                part=d[5]+d[6]
                if int(part)<=12:
                    if part.isdigit()==True:
                        if d[7]=="-":
                            part=d[8]+d[9]
                            if part.isdigit()==True:
                                print(d+" est bien une date ")
                                return True
                            print("Format date incorrecte")
                            return False
                        print("Format date incorrect")
                        return False
                    print("Format date incorrect")
                    return False
                print("Format date incorrect")
                return False
            print("Format date incorrect")
            return False
        elif part.isdigit()==True and int(part)==int(partd):
            if d[4] == "-":
                part = d[5] + d[6]
                partd=d[5] + d[6]
                if int(part)<partd and part.isdigit()==True:
                    if d[7] == "-":
                        part = d[8] + d[9]
                        if part.isdigit() == True:
                            print("Yes")
                elif int(part)==partd and part.isdigit()==True:
                    if d[7] == "-":
                        part = d[8] + d[9]
                        partd=d[8] + d[9]
                        if part.isdigit()==True and int(part)<=partd:
                            return True
                        else:
                            print("Format date incorrect")
                            return False
                    else:
                        print("Format date incorrect")
                        return False
                else:
                    print("Format date incorrect")
                    return False
            else:
                print("Format date incorrect")
                return False
        else:
            print("Format date incorrect")
            return False
    else:
        print("Format date incorrect")
        return False
