##############################
# Nettoyage de fichier V 1.0.0
# Bertrand GARGAUD
# 12-2020
##############################

#-----------------------Modules-----------------------

import os
import sys
import pandas as pd # lire le csv et ses colonnes
import re # ajoute les valeurs dans le nouveau fichier
import shutil # copie le fichier source txt
import colorama # ajoute de la couleur pour la mise en forme
from tkinter import * # interface pour aller chercher le fichier
from tkinter import filedialog # interface pour aller chercher le fichier
from tkinter.filedialog import askopenfilename # interface pour aller chercher le fichier

#-----------------------Fonctions-----------------------

try: # englobe l'intégralité du script pour quitter proprement le script en cas de "KeyboardInterrupt"

    def etapecsv(): #choix du csv
        print ("\n ***************************************\n" +
        " Choix du fichier CSV\n" +
        " ***************************************\n")
        def bouton_quitter(): # Défini l'action du bouton quitter
            print(colorama.Fore.RED +"Vous avez quitté volontairement le script !",colorama.Fore.RESET)
            sys.exit()

        def import_csv(): # Ouvre et ajoute le fichier source en variable
            global fichiersource
            fichiersource = filedialog.askopenfilename(title = "*** Choissiez votre fichier source ***", filetypes = (("Fichiers CSV", ".csv"),))
            fenetre.destroy()

        fenetre = Tk()
        # Créé le bouton de recherche b1 du fichier et le bouton pour quitter b2
        b1 = Button(fenetre, text = "*** Choissiez votre fichier source ***", command = import_csv).pack()
        b2 = Button(fenetre,text="Quitter",command=bouton_quitter).pack()
        fenetre.mainloop()
        print ("Vous avez choisi le fichier source: ",fichiersource)
        etapecsvbis()


    def etapecsvbis(): #choix de la colonne du .csv
        print ("\n ***************************************\n" +
        " Choix de la colonne concernée\n" +
        " ***************************************\n")
        data = pd.read_csv(fichiersource, sep = ';', header = 0) # ajoute tout le contenu du csv dans une variable
        #print(data) # affiche le contenu du fichier csv source
        nbcolonne = len(data.columns)
        nblignes = len(data.index)
        print("Votre fichier .csv comporte", nbcolonne,"colonnes et", nblignes,"lignes\n") #nombre de colonnes et lignes du .csv
        colonnename = list(data.columns) #intègre le nom des colonnes dans une list
        print("Voici le nom des colonnes :" ,colonnename, "\n") #affiche le nom des colonnes
        global choicecsvbis
        choicecsvbis = (input("Indiquer le nom de la colonne choisi :\n(Faites 9 pour revenir au menu précédent)\n"))
        if choicecsvbis in colonnename:
            # print(data[choicecsvbis]) # affiche de contenu de la colonne sélectionnée
            fichier = open("donneescript.txt", "w") # Ouvre le fichier
            fichier.write(str(data[choicecsvbis])) # Ecrit les éléments de la colonne choisie
            fichier.close() # Ferme le fichier
            etape2()
        
        if choicecsvbis =="9":
            etapecsv()

        else:
            print(colorama.Fore.RED + "Vous devez saisir un des noms de colonne pour continuer !",colorama.Fore.RESET)
            etapecsvbis()


    def etapetxt():
        print ("\n ***************************************\n" +
        " Choix du fichier TXT\n" +
        " ***************************************\n")
        def bouton_quitter(): # Défini l'action du bouton quitter
            print(colorama.Fore.RED +"Vous avez quitté volontairement le script !",colorama.Fore.RESET)
            sys.exit()

        def import_txt(): # Ouvre et ajoute le fichier source en variable
            global fichiersource
            fichiersource = filedialog.askopenfilename(title = "*** Choissiez votre fichier source ***", filetypes = (("Fichiers TXT", "*.txt"),))
            fenetre.destroy()

        fenetre = Tk()
        # Créé le bouton de recherche b1 du fichier et le bouton pour quitter b2
        b1 = Button(fenetre, text = "*** Choissiez votre fichier source ***", command = import_txt).pack()
        b2 = Button(fenetre,text="Quitter",command=bouton_quitter).pack()
        fenetre.mainloop()
        print ("Vous avez choisi le fichier source: ",fichiersource)

        shutil.copy(fichiersource,"donneescript.txt") # Copie le convenu du fichier source dans le fichier tampon
        etape2()


    def etape2(): # Choix du délimiteur
        print ("\n ***************************************\n" +
        " Choix de l'élément concerné\n" +
        " ***************************************\n")
        global delimiteur
        delimiteur= input ("Indiquez le ou les caractères concerné(s) par le reformatage :\n\n>>")
        if not delimiteur:
            print(colorama.Fore.RED + "Vous devez saisir un ou plusieurs caractère(s) pour continuer !",colorama.Fore.RESET)
            etape2()
        
        else:
            etape3()


    def etape3(): #choix de l'action add ou del
        print ("\n ***************************************\n" +
        " Que souhaitez vous faire ?\n" +
        " ***************************************\n")
        print ("1 - Ajouter du contenu")
        print ("2 - Supprimer du contenu")
        print ("3 - Modifier du contenu")
        print ("9 - Revenir à l'étape précédente")
        print ("0 - Quitter")
        choice3 = (input("\nQuel est votre choix ?\n\n>>"))
        if choice3 =="1":
            etape3a()

        if choice3 =="2":
            etape3b()

        if choice3 =="3":
            etape3c()

        if choice3 =="9":
            etape2()

        if choice3 =="0":
            print ("\nMerci d'avoir utilisé mon script et à bientôt !\n")
            sys.exit()
        
        else:
            print (colorama.Fore.RED + "Veuillez saisir un des choix proposés !",colorama.Fore.RESET)
            etape3()


    def etape3a(): #choix du contenu à ajouter
        print ("\n ***************************************\n" +
        " Ajout de contenu\n" +
        " ***************************************\n")
        global addcontenu
        addcontenu = (input("\n- Que souhaitez vous ajouter ?\n(Faites 9 pour revenir au menu précédent)\n\n>>"))
        if addcontenu == "9":
            etape3()
        
        else:
            etape4a()


    def etape3b(): #choix de garder ou pas le caractère spécial dans l'action de suppression
        print ("\n ***************************************\n" +
        " Suppression de contenu\n" +
        " ***************************************\n")
        print ("Souhaitez vous inclure \"",delimiteur,"\" dans la suppression?")
        print ("1 - Oui")
        print ("2 - Non")
        choice3b = (input("\n- Quel est votre choix ?\n(Faites 9 pour revenir au menu précédent)\n\n>>"))
        if choice3b =="1":
            etape4b()

        if choice3b =="2":
            etape4c()

        if choice3b == "9":
            etape3()

        else :
            print (colorama.Fore.RED + "Veuillez saisir un des choix proposés !",colorama.Fore.RESET)
            etape3b()


    def etape3c(): #modification de contenu
        print ("\n ***************************************\n" +
        " Modification du contenu : \"",delimiteur,"\" \n" +
        " ***************************************\n")
        newtext = (input("Par quelle valeur souhaitez vous remplacer le contenu ?\n(Faites 9 pour revenir au menu précédent)\n\n>>"))
        if newtext =="9":
            etape3()
            
        else :
            choice3c = (input("\nQuel nom souhaitez vous pour le nouveau fichier ?\n(Faites 9 pour revenir au menu précédent)\n\n>>"))
            if choice3c =="9":
                etape3c()
            
            else :
                with open("donneescript.txt") as fichier_tampon:
                    lines = []
                    for line in fichier_tampon: # exécute la suite tant qu'une ligne est trouvée dans le ficher
                        fichier = open(choice3c, "a") # Ouvre le nouveau fichier
                        fichier.write(re.sub(delimiteur, newtext, line)) # Ajoute dans le txt une nouvelle ligne avec la valeur reformatée
                        fichier.close() # Ferme le fichier
            print(colorama.Fore.GREEN,"\nVotre fichier \"",choice3c,"\" a été créé avec succès avec les valeurs modifiées (\"",delimiteur,"\" a été remplacé par \"",newtext,"\")",colorama.Fore.RESET)
            os.remove("donneescript.txt") # Supprime le fichier tampon
            etapeend()


    def etape4a(): #choix du sens d'ajout de contenu
        print ("\n ***************************************\n" +
        " Souhaitez vous ajouter le contenu avant ou après \"",delimiteur,"\" ?\n" +
        " ***************************************\n")
        print ("1 - Avant")
        print ("2 - Après")
        print ("9 - Revenir à l'étape précédente")
        print ("0 - Quitter")
        choice4a = (input("\nQuel est votre choix ?\n\n>>"))
        if choice4a =="1":
            nomfichier = (input("\nQuel nom souhaitez vous pour le nouveau fichier ?\n(Faites 9 pour revenir au menu précédent)\n\n>>"))
            if nomfichier =="9":
                etape4a()
            
            else :
                with open("donneescript.txt") as fichier_tampon:
                    lines = []
                    for line in fichier_tampon: # exécute la suite tant qu'une ligne est trouvée dans le ficher
                        fichier = open(nomfichier, "a") # Ouvre le nouveau fichier
                        fichier.write((addcontenu + delimiteur).join(line.split(delimiteur))) # Ajoute dans le txt une nouvelle ligne avec la valeur reformatée
                        fichier.close() # Ferme le fichier
            print(colorama.Fore.GREEN,"\nVotre fichier \"",nomfichier,"\" a été créé avec succès avec les valeurs modifiées (Le contenu \"",addcontenu,"\" a été ajouté AVANT le caractère \"",delimiteur,"\")",colorama.Fore.RESET)
            os.remove("donneescript.txt") # Supprime le fichier tampon
            etapeend()
            
        if choice4a =="2":
            nomfichier = (input("\nQuel nom souhaitez vous pour le nouveau fichier ?\n(Faites 9 pour revenir au menu précédent)\n\n>>"))
            if nomfichier =="9":
                etape4a()
            
            else :
                with open("donneescript.txt") as fichier_tampon:
                    lines = []
                    for line in fichier_tampon: # exécute la suite tant qu'une ligne est trouvée dans le ficher
                        fichier = open(nomfichier, "a") # Ouvre le nouveau fichier
                        fichier.write((delimiteur + addcontenu).join(line.split(delimiteur))) # Ajoute dans le txt une nouvelle ligne avec la valeur reformatée
                        fichier.close() # Ferme le fichier
            print(colorama.Fore.GREEN,"\nVotre fichier \"",nomfichier,"\" a été créé avec succès avec les valeurs modifiées (Le contenu \"",addcontenu,"\" a été ajouté APRES le caractère \"",delimiteur,"\")",colorama.Fore.RESET)
            os.remove("donneescript.txt") # Supprime le fichier tampon
            etapeend()

        if choice4a =="9":
            etape3a()

        if choice4a =="0":
            print ("\nMerci d'avoir utilisé mon script et à bientôt !\n")
            sys.exit()

        else :
            print (colorama.Fore.RED + "Veuillez saisir un des choix proposés !",colorama.Fore.RESET)
            etape4a()


    def etape4b(): #choix du sens de suppression incluant le caractère spécial
        print ("\n ***************************************\n" +
        " Souhaitez vous supprimer le contenu avant ou après \"",delimiteur,"\" ?\n" +
        " ***************************************\n")
        print ("1 - Avant")
        print ("2 - Après")
        print ("9 - Revenir à l'étape précédente")
        print ("0 - Quitter")
        choice4b = (input('\nQuel est votre choix ?\n\n>>'))
        if choice4b =="1":
            nomfichier = (input("\nQuel nom souhaitez vous pour le nouveau fichier ?\n(Faites 9 pour revenir au menu précédent)\n\n>>"))
            if nomfichier =="9":
                etape4b()
            
            else :
                rx_to_first = r'^.*?{}'.format(re.escape(delimiteur)) # supprime tout depuis le début de la chaîne jusqu'à la variable "delimiteur"
                with open("donneescript.txt") as fichier_tampon:
                    lines = []
                    for line in fichier_tampon: # exécute la suite tant qu'une ligne est trouvée dans le ficher
                        fichier = open(nomfichier, "a") # Ouvre le nouveau fichier
                        fichier.write(re.sub(rx_to_first, '', line, flags=re.DOTALL).strip()+'\n') # Ajoute dans le txt une nouvelle ligne avec la valeur reformatée
                        fichier.close() # Ferme le fichier
            print(colorama.Fore.GREEN,"\nVotre fichier \"",nomfichier,"\" a été créé avec succès avec les valeurs nettoyées (Le contenu AVANT le caractère \"",delimiteur,"\" en l'incluant a été supprimé)",colorama.Fore.RESET)
            os.remove("donneescript.txt") # Supprime le fichier tampon
            etapeend()

        if choice4b =="2":
            nomfichier = (input("\nQuel nom souhaitez vous pour le nouveau fichier ?\n(Faites 9 pour revenir au menu précédent)\n\n>>"))
            if nomfichier =="9":
                etape4b()
            
            else :        
                with open("donneescript.txt") as fichier_tampon:
                    lines = []
                    for line in fichier_tampon: # exécute la suite tant qu'une ligne est trouvée dans le ficher
                        fichier = open(nomfichier, "a") # Ouvre le nouveau fichier
                        fichier.write(line.split(delimiteur, 1)[0]+'\n') # Ajoute dans le txt une nouvelle ligne avec la valeur reformatée
                        fichier.close() # Ferme le fichier
            print(colorama.Fore.GREEN,"\nVotre fichier \"",nomfichier,"\" a été créé avec succès avec les valeurs nettoyées (Le contenu APRES le caractère \"",delimiteur,"\" en l'incluant a été supprimé)",colorama.Fore.RESET)
            os.remove("donneescript.txt") # Supprime le fichier tampon
            etapeend()

        if choice4b =="9":
            etape3b()

        if choice4b =="0":
            print ("\nMerci d'avoir utilisé mon script et à bientôt !\n")
            sys.exit()

        else :
            print (colorama.Fore.RED + "Veuillez saisir un des choix proposés !",colorama.Fore.RESET)
            etape4b()


    def etape4c(): #choix du sens de suppression en conservant le caractère spécial
        print ("\n ***************************************\n" +
        " Souhaitez vous supprimer le contenu avant ou après \"",delimiteur,"\" ?\n" +
        " ***************************************\n")
        print ("1 - Avant")
        print ("2 - Après")
        print ("9 - Revenir à l'étape précédente")
        print ("0 - Quitter")
        choice4c = (input("\nQuel est votre choix ?\n\n>>"))
        if choice4c =="1":
            nomfichier = (input("\nQuel nom souhaitez vous pour le nouveau fichier ?\n(Faites 9 pour revenir au menu précédent)\n\n>>"))
            if nomfichier =="9":
                etape4c()
            
            else :
                rx_to_first = r'^.*?{}'.format(re.escape(delimiteur)) # supprime tout depuis le début de la chaîne jusqu'à la variable "delimiteur"
                with open("donneescript.txt") as fichier_tampon: 
                    lines = []
                    for line in fichier_tampon: # exécute la suite tant qu'une ligne est trouvée dans le ficher
                        fichier = open(nomfichier, "a") # Ouvre le nouveau fichier
                        fichier.write(re.sub(rx_to_first, delimiteur, line, flags=re.DOTALL).strip()+'\n') # Ajoute dans le txt une nouvelle ligne avec la valeur reformatée
                        fichier.close() # Ferme le fichier
            print(colorama.Fore.GREEN,"\nVotre fichier \"",nomfichier,"\" a été créé avec succès avec les valeurs nettoyées (Le contenu AVANT le caractère \"",delimiteur,"\" en le conservant a été supprimé)",colorama.Fore.RESET)
            os.remove("donneescript.txt") # Supprime le fichier tampon
            etapeend()

        if choice4c =="2":
            nomfichier = (input("\nQuel nom souhaitez vous pour le nouveau fichier ?\n(Faites 9 pour revenir au menu précédent)\n\n>>"))
            if nomfichier =="9":
                etape4c()
            
            else :        
                with open("donneescript.txt") as fichier_tampon:
                    lines = []
                    for line in fichier_tampon: # exécute la suite tant qu'une ligne est trouvée dans le ficher
                        fichier = open(nomfichier, "a") # Ouvre le nouveau fichier
                        fichier.write(line.split(delimiteur, 1)[0]+delimiteur+'\n') # Ajoute dans le txt une nouvelle ligne avec la valeur reformatée
                        fichier.close() # Ferme le fichier
            print(colorama.Fore.GREEN,"\nVotre fichier \"",nomfichier,"\" a été créé avec succès avec les valeurs nettoyées (Le contenu APRES le caractère \"",delimiteur,"\" en le conservant a été supprimé)",colorama.Fore.RESET)
            os.remove("donneescript.txt") # Supprime le fichier tampon
            etapeend()

        if choice4c =="9":
            etape3b()

        if choice4c =="0":
            print ("\nMerci d'avoir utilisé mon script et à bientôt !\n")
            sys.exit()

        else :
            print (colorama.Fore.RED + "Veuillez saisir un des choix proposés !",colorama.Fore.RESET)
            etape4c()


    def etapeend(): #menu final
        print ("\n ***************************************\n" +
        " Continuer l'aventure ? \n" +
        " ***************************************\n")
        print ("Souhaitez vous reformater un autre fichier ?\n")
        print ("1 - Oui")
        print ("2 - Non")
        choiceend = (input('\n- Quel est votre choix ?\n>>'))
        if choiceend =="1":
            menu()

        if choiceend =="2":
            print ("\nMerci d'avoir utilisé mon script et à bientôt !\n")
            sys.exit()

        else :
            print (colorama.Fore.RED + "Veuillez saisir un des choix proposés !",colorama.Fore.RESET)
            etapeend()

#-----------------------Menu-----------------------

    def menu(): #menu principal
        print ("\n ***************************************\n" +
        " Choix du fichier type de fichier\n" +
        " ***************************************\n")
        print ("Veuillez choisir votre type de fichier à reformater :\n")
        print ("1 - .csv")
        print ("2 - .txt")
        print ("0 - Quitter")
        typefichier = input("\nQuel est votre choix ?\n(Faites 0 pour quitter)\n\n>>") # va cherche le fihcier source à retravailler  
        if typefichier =="1":
            etapecsv()

        if typefichier =="2":
            etapetxt()

        if typefichier =="0":
            print ("\nMerci d'avoir utilisé mon script et à bientôt !\n")
            sys.exit()

        else :
            print (colorama.Fore.RED + "Veuillez saisir un des choix proposés !",colorama.Fore.RESET)
            menu()

        typefichier = input("Chemin d'accès du fichier source .csv :\n(Faites 0 pour quitter)\n\n>>") # va cherche le fihcier source à retravailler
    menu()

#-----------------------Fermeture du script en cas d'interuption forcée (CTRL+C)-----------------------

except KeyboardInterrupt: # englobe l'intégralité du script pour quitter proprement le script en cas de "KeyboardInterrupt"
    print(colorama.Fore.RED +"Vous avez quitté volontairement le script !",colorama.Fore.RESET)
    try:
        if os.path.exists("donneescript.txt"): # Vérifie si le fichier tampon existe
            os.remove("donneescript.txt") # Supprime le fichier tampon
            sys.exit()
        else :
            sys.exit()  
    except SystemExit:
        os._exit(0)
