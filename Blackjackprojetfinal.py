# -----------------------------------------
# Nom: Elias Tarabey
# Titre: BlackJack Tkinter
# Description: Créer un jeu de blackjack en utilisant Tkinter
# ------------------------------------------
# Variables Globales:
# ------------------------------------------
# Déclaration de fonctions:
def cliqueJoueur(): # Fonction pour apporter le joueur à entrer leur nom.
    global reponse
    global btnOk
    global txtNom
    btnCommence.destroy() # On enlève le premier bouton du programme principale.
    for Regles2 in range(15): # Enlève les règles du jeu.
        Label = Regleslist[Regles2]
        Label.destroy()
    reponse = tk.StringVar() # Variable pour le nom de l'utilisateur.
    lblCarte = tk.Label(fenetre)
    lblCarte['image'] = Nombres[0]
    lblCarte.grid(row=2, column=5, columnspan=7, rowspan=3, pady=175, padx=10, sticky=tk.E)
    txtNom = tk.Entry(fenetre) # Boîte d'entrée pour mettre le nom.
    txtNom['width'] = 15
    txtNom['textvariable'] = reponse
    txtNom.grid(row=3,column=4,sticky=tk.NE,pady=135,columnspan=1,rowspan=1)
    btnOk = tk.Button(fenetre) # Bouton pour faire procéder le jeu.
    btnOk['text'] = "OK"
    btnOk['font'] = ("Arial 15")
    btnOk['command'] = cliqueBet
    btnOk.grid(row=3,column=3,columnspan=5,pady=180,padx=140,sticky=tk.W)
    lblJoueur['text'] = "C'est quoi votre nom?"
def cliqueOK(): # Fonction pour faire afficner les cartes, afficher les pointages, les boutons et passer à d'autres fonctions.
    global lblJoueur # On utilise beaucoup de variables différents à travers différents fonctions, alors on les met à global.
    global radBtn1
    global radBtn2
    global btnOk
    global cartePos2
    global Points1
    global Points2
    global Points3
    global Test
    global Deux
    global Bouton
    global Image
    global Column
    global Column2
    global Bouton2
    global ImagePos
    global CarteCouverte
    global i2
    global cartePos3
    global As
    global As2
    global Dealer
    global Image2
    global Column3
    global btnCarte
    global btnStand
    global Dealerhand
    global Dealerhand2
    global Valeur
    global lblBet
    global sclValeur
    global btnOk2
    global lblValeur
    global lblPoints2
    global lblPoints1
    global lblPoints2double
    global Double
    global Points4
    global Points5
    global PointsDealer
    global Deux2
    global Image3
    global btnDeux
    global Bouton3
    global Affiche
    global Bet
    global Valeur2
    global Oui
    if Bouton3 == 1: # Enlève le bouton split lorsqu'on l'appuie dessus.
        btnDeux.destroy()
        Bouton3 = 0
    if Double2 == 1: # Permet de passer à afficher les cartes de fenetre2 (deuxième fenêtre) et d'afficher le pointage de cette fenêtre (Double = 1)
        Double = 1
    if Double3 == 1: # Permet de mettre les cartes du fenetre2 à les mêmes positions que ceux de fenetre.
        Column2 = 3
        Column3 = 7
        Image2 = 65
        Column = 4
        Image3 = 50
        Bouton2 = 0
        Deux2 = 0
    if Bouton == 0: # Enlève les objets pour mettre un parier et permettre de créer le pointage des deux joueurs.
        lblBet.destroy()
        sclValeur.destroy()
        btnOk2.destroy()
        lblValeur2.destroy()
        lblPoints1 = tk.Label(fenetre) # Affiche les points de l'ordinateur.
        lblPoints1['font'] = ("Arial 14")
        lblPoints1['background'] = 'yellow'
        lblPoints1.grid(row=1, rowspan=5, columnspan=3, sticky=tk.N, pady=25)
        lblPoints2 = tk.Label(fenetre) # Affiche les points de l'utilisateur.
        lblPoints2['font'] = ("Arial 14")
        lblPoints2['background'] = 'yellow'
        lblPoints2.grid(row=4, column=1, columnspan=3, sticky=tk.SW, padx=8)
        Valeur = Valeur - Bet.get() # Enlève la valeur du parier du valeur total.
        lblBet = tk.Label(fenetre) # Permet d'afficher le parier.
        lblBet['text'] = "Parier: {}".format(Bet.get())
        lblBet['font'] = ("Arial 12")
        lblBet['background'] = "yellow"
        lblBet.grid(row=0,column=5,sticky=tk.NE,columnspan=5,rowspan=5,pady=35)
        lblValeur = tk.Label(fenetre) # Permet d'afficher la valeur restante du joueur.
        lblValeur['text'] = "Valeur Restant: {}".format(Valeur)
        lblValeur['font'] = ("Arial 12")
        lblValeur['background'] = "yellow"
        lblValeur.grid(row=0,column=5,columnspan=5,sticky=tk.NE,rowspan=5)
        Bet = Bet.get()
    if Points2 == 0:
        Range = 4 # Permet de faire apparaître 4 cartes au début du jeu et de calculer les points des deux côtés (seulement un carte du dealer).
    else:
        Range = 1 # Permet de faire apparaître un carte seulement.
    if Dealer == 1:
        CarteCouverte['image'] = Nombres[ImagePos] # Si c'est le tour du dealer, on affiche sa carte de couverte et on affiche un nouveau pointage.
        Points1 = sum(Dealerhand2)
    while Range == 4 or (Points2 < 21 and Dealer == 0 and Stand == 0) or (Points3 < 21 and Dealer == 0 and Stand == 0) or Points1 < 17 and Dealer == 1 or Double == 1 and Dealer == 0:
        # Cette boucle aide à générer les cartes et points au début du jeu (Range = 4), lorsqu'on appuie sur "Hit" ou pour faire jouer l'ordinateur jusqu'à 17 points.
        if Dealer == 1:
            Image2 += 14
            Column3 += 1
        for i in range(Range): # Cette boucle for permet de faire apparaître les cartes et les ajouter aux tableaux appropriés pour qu'on calcule les points.
            # C'est basé sur la valeur de Range (4 ou 1)
            if Bouton == 1:
                Image += 20
                Image3 = Image3 + 2
                if Double3 == 0:
                    i += Image # En changeant la valeur d'Image ou Image3, on peut les ajouter à la valeur de i pour générer un nouveau image de carte.
                    # Ceci prévient des erreurs.
                else:
                    i = i + Image3
                Column += 1 # Permet de déplacer les images à différents positions pour qu'ils ne soient pas un dessus de l'autre.
                Column2 += 2
            while Test == 0:
                nbCartes = len(paquet2)
                cartePos = random.randint(0, nbCartes-1) # Ceci cherche et génère la carte pigé du paquet.
                if cartePos in paquet: # Si cartePos n'est pas dans paquet, on fait jouer la boucle une autre fois pour piger une nouvelle carte.
                    # Ceci prévient qu'on génère des dupliqués dans un jeu.
                    Test = 1
            Test = 0
            cartePos2 = 0
            paquet.remove(cartePos) # On enlève la carte à cause qu'on là pigé de paquet.
            i2 = i # Permet de sauvegarder la valeur numérique de i avant que c'est transformé dans un label.
            print(As,"Jesus is Lord")
            if i == 1: # Met la deuxième carte de l'ordinateur à l'envers.
                CarteCouverte = tk.Label(fenetre)
            elif Double == 1: # Permet d'ajouter les images et les valeurs des cartes dans la fenêtre split.
                (i) = tk.Label(fenetre2)
                Joueur.append(i) # Les images vont ici.
                if len(Asdouble) == 0: # Permet d'ajouter la valeur d'un des cartes double dans le tableau de pointage du fenêtre split.
                    Asdouble.append(As[0])
                    Asdouble2.append(As2[0])
            else: # Ajoute les images au tableau pour fenêtre et de créer les labels pour ceci. .
                (i) = tk.Label(fenetre)
                Joueur.append(i)
            Joueur2.append(cartePos) # Tableau pour utiliser dans cliqueSepare.
            if Dealer == 1:
                Dealerlist.append(cartePos) # Tableau pour utiliser dans cliqueGagnantsplit.
            if (i2 != 0 and Bouton == 1) or i2 != 1: # Affiche les images des cartes autre que la carte cachée de l'ordinateur au début du jeu.
                (i)['image'] = Nombres[cartePos]
            else: # Affiche une carte cachée pour l'ordinateur seulement au début du jeu.
                CarteCouverte['image'] = Nombres[0]
                ImagePos = cartePos # Permet de sauvegarder la valeur de la carte actuelle pour le relever plus tard.
            if i2 == 1: # Conditions booléens pour l'affichage des cartes dans la ou les fenêtre(s).
                CarteCouverte.grid(row=2, column=1, rowspan=2, columnspan=6)
            elif i2 == 2:
                (i).grid(row=4, column=2, padx=70, columnspan=4, sticky=tk.W)
            elif i2 == 3:
                (i).grid(row=4, column=2, pady=5, sticky=tk.E, columnspan=3, padx=33)
            elif i2 == 0:
                (i).grid(row=2, column=1, pady=90, sticky=tk.S, padx=50, columnspan=5)
            elif Dealer == 1:
                (i).grid(row=2, column=2, columnspan=Column3, rowspan=2, padx=Image2+48, sticky=tk.W)
            elif Double3 == 0:
                (i).grid(row=4, column=3,columnspan=Column2,padx=Image+25,sticky=tk.W)
            else:
                (i).grid(row=4, column=3, columnspan=Column2+2, padx=Image+22, sticky=tk.W)
            if cartePos <= 13: # Valeur numérique (pour points) de la carte s'il est un pique.
                cartePos2 = cartePos
            elif cartePos <= 26: # Valeur numérique pour un coeur.
                cartePos2 = cartePos - 13
            elif cartePos <= 39: # Valeur numérique pour un trèfle.
                cartePos2 = cartePos - 26
            else: # Valeur numérique pour un diamand.
                cartePos2 = cartePos - 39
            if cartePos2 > 10: # Si cartePos2 est une figure, sa valeur est 10.
                cartePos2 = 10
            if cartePos2 == 1: # Si cartePos2 est un as, sa valeur est 11 ou 1 (plus tard).
                cartePos2 = 11
                if i2 >= 2:
                    Bouton2 = Bouton2 + 1
            if i2 == 0 or i2 == 1:
                if i2 == 0: # Permet d'ajouter les points du début (seulement une carte).
                    Points1 = Points1+cartePos2
                    PointsDealer = Points1 # Valeur des points de l'ordinateur pour fenetre2
                Dealerhand2.append(cartePos2)
            else: # Permet d'ajouter les valeurs numériques aux tableaux pour calculer les points.
                if cartePos2 == 11 and Dealer == 0 and i2 > 1:
                    if Double == 1: # Permet d'ajouter la valeur de l'as pour les points de l'utilisateur à fenetre2.
                        Asdouble.append(11) # On ajoute deux valeurs pour l'as, le tableau principale est Asdouble, mais si c'est > 21, on utilise la somme de Asdouble2.
                        Asdouble2.append(1)
                    else:
                        As.append(11) # Le même principe, mais pour le tableau pour les points de l'utilisateur pour fenetre.
                        As2.append(1)
                    Deux2 = 1
                    if Points3+1 <= 21 and As.count(11) >= 2 or Points4+1 <= 21 and Asdouble.count(11) >= 2:
                        # On ne peut pas avoir deux 11 dans un tableau à cause de la valeur double de l'as, alors, on enlève le 11 d'extra et on met 1.
                        if Double == 1:
                            Asdouble.remove(11)
                            Asdouble.append(1)
                        else:
                            As.remove(11)
                            As.append(1)
                    if As.count(11) > 0:
                        Deux = 1
                elif Dealer == 0 and i2 != 1: # Permet d'ajouter les valeurs numériques aux tableaux de l'utilisateur après les premières 4 cartes.
                    if Double == 1: # Ajoute si fenetre2 est présent.
                        Asdouble.append(cartePos2)
                        Asdouble2.append(cartePos2)
                    elif Double == 0: # Ajoute si fenetre2 n'est pas présent.
                        As.append(cartePos2)
                        As2.append(cartePos2)
                        if Points3 == 21 and i2 > 2 or Points4 == 21 and i2 > 2:
                            Bouton2 = Bouton2 + 1
                else: # Permet d'ajouter les valeurs numériques au tableau de l'ordinateur lorsque le joueur à complété son tour.
                    Dealerhand2.append(cartePos2)
                    if Dealerhand2.count(11) > 1 and cartePos2 == 11 or Points1+cartePos2 > 21 and Dealer == 1 and Dealerhand2.count(11) >= 1:
                        # S'il y a deux 11 dans le tableau de l'ordinateur, on enlève un et on le remplace par la valeur de 1.
                        Dealerhand2.remove(11)
                        Dealerhand2.append(1)
        if i2 == 3 or i2 > 3 or Double == 1 or Double3 == 1: # Code qui permet de sortir du boucle.
            if Dealer == 1:
                Points1 = sum(Dealerhand2) # Ajoute les points après un exécution du boucle, si Points < 17, le boucle se répète.
                PointsDealer = Points1
            else:
                break # Ceci aide à sortir du boucle.
    if Bouton == 0: # Création des boutons pour tirer une autre carte et pour Stand.
        btnCarte = tk.Button(fenetre)
        btnCarte['text'] = "Hit"
        btnCarte['font'] = ("Arial 10")
        btnCarte['command'] = cliqueOK
        btnCarte.grid(row=5,column=2,columnspan=5,padx=50)
        btnStand = tk.Button(fenetre)
        btnStand['command'] = cliqueStand
        btnStand['text'] = "Stand"
        btnStand['font'] = ("Arial 10")
        btnStand.grid(row=5,column=3,columnspan=5,padx=40)
        if As2[0] == As2[1] and Dealerhand2 != [11,10] and Dealerhand2 != [10,11] and Valeur > 1 and Valeur - math.ceil(Bet/2) > 0:
            # Création du bouton Split si la valeur des deux cartes tirées du joueur sont les mêmes et qu'il peut mettre plus de jetons dans son parier.
            btnDeux = tk.Button(fenetre)
            btnDeux['text'] = "Split"
            btnDeux['font'] = ("Arial 10")
            btnDeux['command'] = cliqueSepare
            btnDeux.grid(row=5,column=4,columnspan=5,padx=10)
            Bouton3 = 1
        Bouton = 1
    # --------------------------------------------
    if Dealerhand2 == [11,11]: # On ne peut pas avoir 22 avec 2 as à cause de sa valeur double.
        Dealerhand2.remove(11)
        Dealerhand2.append(1)
    if Double == 1: # On ajoute les points du fenetre split de l'utilisateur.
        Points4 = sum(Asdouble)
        Points5 = sum(Asdouble2)
    else: # On ajoute les points de l'utilisateur si c'est son tour.
        Points3 = sum(As)
        Points2 = sum(As2)
    if Dealer == 1: # On ajoute les points de l'ordinateur si c'est son tour.
        Points1 = sum(Dealerhand2)
        PointsDealer = Points1
    if sum(As) == 21 or sum(As2) == 21:
        Bouton2 = 4
        if Double == 0:
            Points1 = sum(Dealerhand2)
        PointsDealer = Points1
    # ---------------------------------------------
    if Double == 0:
        if Points3 > 21 or Points2 == 21:
            Deux = 0
    elif Double == 1:
        if Points4 > 21 or Points5 == 21:
            Deux2 = 0
    if Dealerhand2 == [11,10] or Dealerhand2 == [10,11]:
        # Permet d'arrêter le jeu si l'ordinateur reçois un blackjack;
        Points1 = sum(Dealerhand2) # On ajoute les points de l'ordinateur.
        PointsDealer = Points1
        if As.count(11) >= 1 and Double == 0: # On affiche la meilleur valeur des points de l'utilisateur s'il a au moins un as.
            lblPoints2['text'] = "{}: {}".format(reponse.get(),Points3)
        elif Asdouble.count(11) >= 1:
            lblPoints2double['text'] = "{}: {}".format(reponse.get(),Points5)
        else:
            if Double == 1:
                lblPoints2double['text'] = "{}: {}".format(reponse.get(),Points5)
            else:
                lblPoints2['text'] = "{}: {}".format(reponse.get(),Points2)
        btnCarte['state'] = 'disabled'
        btnStand['state'] = 'disabled'
        CarteCouverte['image'] = Nombres[ImagePos]
        if As != [11,10] and As != [10,11]: # On passe aux messages de fin si l'utilisateur n'a pas de blackjack.
            cliqueGagnant()
    if Deux2 == 1 and Bouton2 <= 4 and Points4 != 21 and Double == 1: # Affiche les deux valeurs possibles si il y a au moins un as et que Points4 < 21.
        lblPoints2double['text'] = "{}: {}/{}".format(reponse.get(),Points5,Points4)
    elif Deux == 1 and Bouton2 <= 4 and Points3 != 21 and Double == 0 and Points1 != 21:
        lblPoints2['text'] = "{}: {}/{}".format(reponse.get(),Points2, Points3)
    elif As == [11,10] and Double == 0 or As == [10,11] and Double == 0:
        # Exécute si le joueur reçois un blackjack.
        if Double3 == 1:
            Affiche = 1
        Points1 = sum(Dealerhand2) # On ajoute les points du dealer.
        PointsDealer = Points1
        CarteCouverte['image'] = Nombres[ImagePos] # On révèle la carte couverte.
        if Double3 == 1 and Points5 < 21 and Dealer == 0: # Permet de rejouer le tour de l'ordinateur si fenetre2 est présent.
            Dealer = 1
            cliqueOK()
        else: # On passe directement au messages du fin de jeu.
            cliqueGagnant()
        btnCarte['state'] = 'disabled'
        btnStand['state'] = 'disabled'
    elif Asdouble == [11,10] and Double == 1 or Asdouble == [10,11] and Double == 1:
        # Permet de passer à la main de la fenêtre principale si la main du fenetre2 a un blackjack.
        cliqueStand2()
    elif Points2 == 21 and Double == 0 or (Points3 == 21 and Bouton2 == 4 and Double == 0):
        if Double == 1: # Passe au fenêtre principale.
            cliqueStand2()
        else:
            # Met automatiquement les points de l'utilisateur à 21 et le programme affiche ceci.
            Points2 = 21
            lblPoints2['text'] = "{}: {}".format(reponse.get(),Points2)
            CarteCouverte['image'] = Nombres[ImagePos]
            btnCarte['state'] = 'disabled'
            btnStand['state'] = 'disabled'
            Points1 = sum(Dealerhand2)
            if Points1 < 17: # L'ordinateur prend des cartes jusqu'à ou moins que 17 à cause que ce n'est pas un blackjack.
                Dealer = 1
                cliqueOK()
            else:
                cliqueGagnant()
        Dealer = 1
    elif Points5 == 21 and Double == 1 or Points4 == 21 and Bouton2 == 4 and Double == 1:
        cliqueStand2() # On passe à la main principale venant de fenetre2.
    elif Points2 > 21 or Points5 > 21: # Si le joueur bust.
        if Double == 1:
            cliqueStand2()
        else:
            if Points2 > 21:
                # On affiche la carte couverte et les points de l'ordinateur.
                lblPoints1['text'] = "CPU: {}".format(Points1)
                lblPoints2['text'] = "{}: {}".format(reponse.get(),Points2)
                CarteCouverte['image'] = Nombres[ImagePos]
                btnCarte['state'] = 'disabled'
                btnStand['state'] = 'disabled'
                Points1 = sum(Dealerhand2)
                if Double3 == 1:
                    Affiche = 1
                if Points1 < 17 and Double3 == 1 and Points5 < 21 and Dealer == 0:
                    # On rejoue le boucle while si Points1 est < 17 et Points5 < 21
                    Dealer = 1
                    cliqueOK()
                else:
                    cliqueGagnant()
                    Oui = 1
            else:
                if Points3 < 21 and As.count(11) >= 1: # On affiche Points3 et Points2 si Points < 21 et qu'il y a au moins un as.
                    lblPoints2['text'] = "{}: {}/{}".format(reponse.get(),Points2, Points3)
                else:
                    lblPoints2['text'] = "{}: {}".format(reponse.get(),Points2)
        PointsDealer = Points1
    else:
        if Double == 1:
            lblPoints2double['text'] = "{}: {}".format(reponse.get(),Points5)
        else:
            lblPoints2['text'] = "{}: {}".format(reponse.get(),Points2)
    if i2 >= 3 or Dealer == 1:
        if Double == 0: # On affiche le pointage du l'ordinateur ici, dans ce cas, pour fenetre.
            lblPoints1['text'] = "CPU: {}".format(Points1)
        else: # On affiche les points de l'ordinateur pour fenetre2
            lblPoints1double['text'] = "CPU: {}".format(PointsDealer)
    if Double == 1 and len(Asdouble) == 1: # Permet de générer un nouveau carte pour les deux nouveaux mains.
        cliqueOK()
    if Affiche == 1 and Unefois == 0:
        cliqueGagnantsplit() # Permet d'afficher les messages de fin de jeu de fenetre2.
    if Points1 >= 17 and Points2 != 21 and Points1 != 21 and Double3 == 0 and Oui == 0 or Points1 == 21 and Dealer == 1 and Points2 != 21:
        cliqueGagnant() # NOTE: Il y a plusieurs conditions booléens pour ce if à cause qu'on veut pas répeter cette fonction deux fois.
def cliqueStand(): # Permet d'arrêter le tour du joueur et de commencer le tour du dealer si on clique sur Stand. On répète la fonction cliqueOK.
    global Dealer
    global Double
    global Double3
    global Stand
    global Affiche
    global Bet
    global Valeur2
    btnStand['state'] = 'disabled'
    btnCarte['state'] = 'disabled'
    if Double3 == 1:
        Affiche = 1
    Dealer = 1
    Stand = 1
    Double3 = 0
    cliqueOK()
def cliqueStand2(): # Ceci active le tour de fenetre partant de fenetre2, on répète cliqueOK() pour avoir une nouvelle carte pour la main de fenetre.
    global Points5
    global Double
    global Double2
    global Double3
    global Image
    global Deux
    global Deux2
    btnStand2['state'] = 'disabled'
    btnCarte2['state'] = 'disabled'
    btnCarte['state'] = 'active'
    btnStand['state'] = 'active'
    if Points4 <= 21:
        Points5 = Points4
    lblPoints2double['text'] = "{}: {}".format(reponse.get(),Points5)
    Deux2 = 0
    Image = 3
    Double = 0
    if Points3 > 21 and As.count(11) <= 1:
        Deux = 0
    Double2 = 0
    Double3 = 1
    cliqueOK()
def cliqueSepare(): # Permet de créer fenetre2 et une nouvelle main à partir de l'appui de Split.
    global Points2
    global Points3
    global fenetre2
    global Nombres
    global CarteCouverture2
    global Double
    global lblPoints1double
    global lblPoints2double
    global Points4
    global Points5
    global btnCarte2
    global btnStand2
    global Double2
    global Bouton3
    global Valeur
    global lblValeur3
    btnDeux.destroy()
    btnCarte['state'] = 'disabled'
    btnStand['state'] = 'disabled'
    Carte2 = Joueur[2]
    Carte2.destroy()
    Double2 = 1
    Bouton3 = 0
    Points2 = Points2 - As2[0] # On enlève la valeur d'un des cartes pour le split.
    Points3 = Points3 - As2[1]
    if As.count(11) >= 1:
        lblPoints2['text'] = "{}: {}/{}".format(reponse.get(),Points2, Points3)
    else:
        lblPoints2['text'] = "{}: {}".format(reponse.get(),Points2)
    As.remove(As[1]) # On enlève une des cartes des tableaux de l'utilisateur pour ne pas avoir un surplus de points.
    As2.remove(As2[0])
    Valeur = Valeur - int(math.ceil(Bet/2)) # On créer un nouveau parier pour la nouvelle main, qui est la moitié du premier parier.
    fenetre2 = tk.Toplevel() # Création de la fenetre pour la deuxième main.
    fenetre2.title("Split")
    fenetre2.geometry("700x500")
    fenetre2['background'] = "yellow"
    lblValeur3 = tk.Label(fenetre2)
    lblValeur3['text'] = "Valeur Restant: {}".format(Valeur) # On ajoute la nouvelle valeur.
    lblValeur3['font'] = ("Arial 12")
    lblValeur3['background'] = "yellow"
    lblValeur3.grid(row=0, column=5, columnspan=5, sticky=tk.NE, rowspan=5)
    lblValeur['text'] = "Valeur Restant: {}".format(Valeur)
    lblBet2 = tk.Label(fenetre2)
    lblBet2['text'] = "Parier: {}".format(math.ceil(Bet/2)) # On présente le nouveau parier.
    lblBet2['font'] = ("Arial 12")
    lblBet2['background'] = "yellow"
    lblBet2.grid(row=0, column=5, sticky=tk.NE, columnspan=5, rowspan=5, pady=35)
    ImgPersonne2 = tk.Label(fenetre2)
    ImgPersonne2['image'] = imgPersonne
    ImgPersonne2.grid(columnspan=10,row=0,sticky=tk.NW,rowspan=8,padx=275)
    for i7 in range(0,len(Joueur2)): # On met tout les cartes présents de fenetre (except pour une des cartes double de l'utilisateur) et on l'affiche dans fenetre2.
        i8 = i7
        print(i8)
        if i8 != 1:
            (i7) = tk.Label(fenetre2)
            (i7)['image'] = Nombres[Joueur2[i8]]
        else:
            CarteCouverture2 = tk.Label(fenetre2)
            CarteCouverture2['image'] = Nombres[0]
        if i8 == 0:
            (i7).grid(row=2, column=1, pady=90, sticky=tk.S, padx=50, columnspan=5)
        elif i8 == 1:
            CarteCouverture2.grid(row=2, column=1, rowspan=2, columnspan=6)
        elif i8 == 3:
            (i7).grid(row=4, column=2, padx=70, columnspan=4, sticky=tk.W)
    lblPoints1double = tk.Label(fenetre2) # Nouveau label pour les points de l'ordinateur.
    lblPoints1double['text'] = "CPU: {}".format(Points1)
    lblPoints1double['font'] = ("Arial 14")
    lblPoints1double['background'] = 'yellow'
    lblPoints1double.grid(row=1, rowspan=5, columnspan=3, sticky=tk.N, pady=25)
    lblPoints2double = tk.Label(fenetre2) # Nouveau label des Points de l'utilisateur.
    lblPoints2double['font'] = ("Arial 14")
    lblPoints2double['background'] = 'yellow'
    lblPoints2double.grid(row=4, column=1, columnspan=3, sticky=tk.SW, padx=8)
    lblCarte2 = tk.Label(fenetre2) # Bouton pour une nouvelle carte dans fenetre2
    lblCarte2['image'] = Nombres[0]
    lblCarte2.grid(row=2,column=5,columnspan=7,rowspan=3,pady=175,padx=10,sticky=tk.E)
    btnCarte2 = tk.Button(fenetre2)
    btnCarte2['text'] = "Hit"
    btnCarte2['font'] = ("Arial 10")
    btnCarte2['command'] = cliqueOK
    btnCarte2.grid(row=5, column=2, columnspan=5, padx=50)
    btnStand2 = tk.Button(fenetre2) # Bouton pour arrêter le tour du joueur dans fenetre2.
    btnStand2['command'] = cliqueStand2
    btnStand2['text'] = "Stand"
    btnStand2['font'] = ("Arial 10")
    btnStand2.grid(row=5, column=3, columnspan=5, padx=40)
    cliqueOK()
def cliqueGagnant(): # Permet d'afficher les messages de fin de jeu pour fenetre et de mettre à jour la valeur de l'utilisateur.
    global lblValeur
    global Points3
    global Points2
    global Blackjack
    global Bet
    global Valeur
    global lblPoints2
    global lblGagnant
    global lblBet2
    global lblContinue
    global btnOui
    global btnNon
    global Points5
    global Affiche
    global Bet3
    global Valeur2
    global lblValeur2
    Blackjack = 0
    Bet3 = Bet
    lblGagnant = tk.Label(fenetre) # Label pour afficher le message de qui a gagné.
    lblGagnant['font'] = ("Arial 12")
    lblGagnant['background'] = 'yellow'
    lblGagnant.grid(row=2,column=3,columnspan=6,padx=84,sticky=tk.SW,rowspan=5,pady=210)
    lblBet2 = tk.Label(fenetre) # Affiche le montant de points gagné, perdu ou reacquis.
    lblBet2['font'] = ("Arial 12")
    lblBet2['background'] = 'yellow'
    lblBet2.grid(row=2,column=3,columnspan=6,padx=80,sticky=tk.SW,rowspan=2,pady=15)
    if Points2 == 21 and Points4 > 0:
        Affiche = 1 # Permet de jouer la fonction de cliqueGagnantsplit.
    if Points2 <= 21 and Points1 <= 21: # Ceci joue lorsque les deux systèmes de points de fenetre sont <= 21.
        if (Points3 <= 21 and As.count(11) >= 1 and Double == 0): # Permet d'afficher le meilleur pointage s'il y a au moins un as dans As et que Points3 <= 21.
            Points2 = Points3
            lblPoints2['text'] = "{}: {}".format(reponse.get(),Points2)
            if As == [11,10] and Points1 != 21 and Double == 0 or As == [10,11] and Points1 != 21 and Double == 0:
                # Affiche un message que l'utilisateur a obtenu un blackjack.
                lblGagnant['text'] = "Blackjack! Tu gagnes."
                Bet3 = Bet3*2 + 50 # Il ou elle gagne deux fois son parier + 50 points.
                Valeur = Valeur + Bet3 # Mise à jour de la valeur totale.
                lblBet2['text'] = "Tu gagnes {} jetons de plus.".format(Bet3)
                Blackjack = 1
        Pointstotal = Points2 - Points1 # Permet d'obtenir la différence entre les deux points pour afficher les bonnes messages dans les conditions booléens qui se suivent.
        if Pointstotal > 0 and Blackjack == 0: # Si la différence est positive, l'utilisateur gagne.
            lblGagnant['text'] = "Tu as gagné."
            Valeur = Valeur + Bet3*2 # Il ou elle gagne deux fois sont parier.
            lblBet2['text'] = " Tu gagnes {} jetons de plus.".format(Bet3)
        elif Pointstotal < 0 and Blackjack == 0: # Si la différence est négative, l'utilisateur perd.
            lblGagnant['text'] = "L'ordinateur a gagné."
            lblBet2['text'] = "Tu perds {} jetons.".format(Bet3)
        elif Pointstotal == 0: # Si la différence est 0, c'est un égalité.
            lblGagnant['text'] = "Push"
            Valeur = Valeur + Bet3
            lblBet2['text'] = "Tu gardes tes jetons"
    elif Points2 > 21 and Points1 > 21 and Affiche == 1:
        lblGagnant['text'] = "L'ordinateur a gagné."
        Valeur = Valeur - Bet3 # L'utilisateur perd si ses points sont plus que 21.
        lblBet2['text'] = "Tu perds {} jetons.".format(Bet3)
    elif Points2 <= 21 and Points1 > 21 and Double == 0: # Ceci joue lorsque les points de l'utilisateur est moins ou égale à 21 et que les points de l'ordinateur sont plus que 21.
        if As == [11,10] or As == [10,11]: # Message si le joueur a obtenu un blackjack.
            lblGagnant['text'] = "Blackjack! Tu gagnes."
            Bet3 = Bet3 * 2 + 50 # Double les points et +50 points.
            Valeur = Valeur + Bet3
            lblBet2['text'] = "Tu gagnes {} de jetons de plus.".format(Bet3)
        elif Points3 <= 21 and As.count(11) >= 1 and Double == 0: # Si Points3 donne un meilleur pointage que Points2, il est utilisé au lieu de Points2.
            Points2 = Points3
            lblPoints2['text'] = "{}: {}".format(reponse.get(),Points2)
            lblGagnant['text'] = "Tu as gagné."
            Bet3 = Bet3 * 2
            Valeur = Valeur + Bet3
            lblBet2['text'] = " Tu gagnes {} jetons de plus.".format(Bet3)
        else:
            Bet3 = Bet3 * 2
            Valeur = Valeur + Bet3
            lblBet2['text'] = " Tu gagnes {} jetons de plus.".format(Bet3)
            lblGagnant['text'] = "Tu as gagné."
    elif Points2 > 21 and Points1 <= 21: # Si l'utilisateur a plus de 21 points, il ou elle perd.
        lblGagnant['text'] = "L'ordinateur a gagné."
        lblBet2['text'] = "Tu perds {} jetons.".format(Bet3)
    else:
        lblGagnant['text'] = "Push"
        Valeur = Valeur + Bet3
        lblBet2['text'] = "Tu gardes tes jetons"
    lblValeur['text'] = "Valeur Restant: {}".format(Valeur) # Mise à jour du valeur de fenetre.
    if Points5 > 0: # Mise à jour de valeur pour fenetre2.
        lblValeur3['text'] = "Valeur Restant: {}".format(Valeur)
    # Génération de l'option de continuer ou pas après que le jeu se termine.
    lblContinue = tk.Label(fenetre)
    lblContinue['text'] = "Veux-tu continuer?"
    lblContinue['font'] = ("Arial 12")
    lblContinue['background'] = "yellow"
    lblContinue.grid(row=2,column=6,columnspan=6,rowspan=5,sticky=tk.SE,pady=135,padx=20)
    btnOui = tk.Button(fenetre)
    btnOui['text'] = "Oui"
    btnOui['font'] = ("Arial 10")
    btnOui['command'] = cliqueOui
    btnOui.grid(row=2,column=6,columnspan=3,rowspan=5,sticky=tk.SE,pady=80,padx=40)
    btnNon = tk.Button(fenetre)
    btnNon['text'] = "Non"
    btnNon['font'] = ("Arial 10")
    btnNon['command'] = cliqueNon
    btnNon.grid(row=2,column=6,columnspan=4,rowspan=5,sticky=tk.SE,pady=80,padx=25)
    Blackjack = 0
    Valeur2 = Valeur
    if Affiche == 1 and Unefois == 0: # On passe pour afficher les messages de fin pour fenetre2 si c'est présent.
        cliqueGagnantsplit()
def cliqueGagnantsplit(): # Même concept que cliqueGagnant, except que c'est pour fenetre2.
    global Unefois
    global PointsDealer
    global Points5
    global Points4
    global Valeur
    global Image2
    global Bet
    Image2 = 65
    Unefois = 1 # Permet de faire jouer cette fonction une fois.
    CarteCouverture2['image'] = Nombres[ImagePos] # On révèle la carte couverte.
    if len(Dealerlist) > 0: # On affiche les mêmes cartes qui sont présents dans fenetre, car l'ordinateur a seulement un main.
        for Life in range(0,len(Dealerlist)):
            if Life == 1:
                Image2 = Image2 + 16
            Life2 = Life
            (Life) = tk.Label(fenetre2)
            (Life)['image'] = Nombres[Dealerlist[Life2]]
            (Life).grid(row=2,column=2, columnspan=Column3, rowspan=2, padx=Image2+48, sticky=tk.W)
    PointsDealer = Points1 # On met les points de l'ordinateur à fenetre2 les mêmes que celles de fenetre.
    # Code similaire à cliqueGagnant pour mettre à jour la valeur et afficher le gagnant.
    lblPoints1double['text'] = "CPU: {}".format(PointsDealer)
    lblGagnant2 = tk.Label(fenetre2)
    lblGagnant2['font'] = ("Arial 12")
    lblGagnant2['background'] = 'yellow'
    lblGagnant2.grid(row=2, column=3, columnspan=6, padx=84, sticky=tk.SW, rowspan=5, pady=210)
    lblBet3 = tk.Label(fenetre2)
    lblBet3['font'] = ("Arial 12")
    lblBet3['background'] = 'yellow'
    lblBet3.grid(row=2, column=3, columnspan=6, padx=80, sticky=tk.SW, rowspan=2, pady=15)
    Bet2 = int(math.ceil(Bet/2))
    if Asdouble == [11,10] and PointsDealer != 21 or Asdouble == [10,11] and PointsDealer != 21:
        lblGagnant2['text'] = "Blackjack! Tu gagnes."
        Valeur = Valeur + Bet2*2+50
        lblBet3['text'] = "Tu gagnes {} jetons cette ronde.".format(Bet2*2+50)
    elif Points5 > 21 and PointsDealer <= 21:
        lblGagnant2['text'] = "L'ordinateur a gagné"
        lblBet3['text'] = "Tu perds {} jetons cette ronde.".format(Bet2)
    elif Points5 < 21 and PointsDealer <= 21:
        Pointstotal2 = Points5 - PointsDealer
        if Pointstotal2 > 0:
            lblGagnant2['text'] = "Tu as gagné."
            Valeur = Valeur + Bet2*2
            lblBet3['text'] = "Tu gagnes {} jetons cette ronde.".format(Bet2*2)
        elif Pointstotal2 < 0:
            lblGagnant2['text'] = "L'ordinateur a gagné."
            lblBet3['text'] = "Tu perds {} jetons cette ronde.".format(Bet2)
        else:
            lblGagnant2['text'] = "Push"
            Valeur = Valeur + Bet2
            lblBet3['text'] = "Tu gardes tes jetons."
    elif Points5 == 21 and PointsDealer != 21:
        lblGagnant2['text'] = "Tu as gagné."
        Valeur = Valeur + Bet2 * 2
        lblBet3['text'] = "Tu gagnes {} jetons cette ronde.".format(Bet2*2)
    elif Points5 <= 21 and PointsDealer > 21:
        lblGagnant2['text'] = "Tu as gagné."
        Valeur = Valeur + Bet2 * 2
        lblBet3['text'] = "Tu gagnes {} jetons cette ronde.".format(Bet2*2)
    elif Points5 == 21 and PointsDealer == 21:
        lblGagnant2['text'] = "Push"
        Valeur = Valeur + Bet2
        lblBet3['text'] = "Tu gardes tes jetons."
    else:
        lblGagnant2['text'] = "L'ordinateur a gagné."
        lblBet3['text'] = "Tu perds {} jetons cette ronde.".format(Bet2)
    lblValeur['text'] = "Valeur Restant: {}".format(Valeur) # Mise à jour des valeurs des points dans les deux fenêtres.
    lblValeur3['text'] = "Valeur Restant: {}".format(Valeur)
    Tempssplit = threading.Thread(target=Time,daemon=True) # Un chronomètre qui se joue après que la ronde est fini en utilisant le module de Threading.
    Tempssplit.start() # Permet de le commencer.
def Time(): # Fonction que le Thread se refère à pour fonctionner.
    Temps2 = 5 # Il y a 5 secondes à ce chronomètre.
    for y in range(Temps2):
        Temps2 = Temps2 - 1
        time.sleep(1) # Délai de 1 seconde pour donner cette fonction les traits d'un chronomètre.
    fenetre2.destroy() # Lorsuqe le chronomètre est fini, fenetre2 se ferme toute seul.
def cliqueBet(): # Permet de mettre un parier.
    global lblBet
    global sclValeur
    global btnOk2
    global Bet
    global lblValeur2
    txtNom.destroy()
    lblJoueur.destroy()
    btnOk.destroy()
    lblValeur2 = tk.Label(fenetre)
    lblValeur2['text'] = "Valeur: {}".format(Valeur) # Affiche le montant qui reste.
    lblValeur2['font'] = ("Arial 15")
    lblValeur2['background'] = 'yellow'
    lblValeur2.grid(row=4,column=2,columnspan=6,rowspan=3,padx=125,pady=15,sticky=tk.N)
    lblBet = tk.Label(fenetre)
    lblBet['text'] = "Entrez votre parier ici."
    lblBet['font'] = ("Arial 14")
    lblBet['background'] = "yellow"
    lblBet.grid(row=3, column=1, pady=10, rowspan=2, columnspan=8,sticky=tk.N)
    sclValeur = tk.Scale(fenetre) # Une échelle est utilisé pour choisir la valeur désiré du parier.
    Bet = tk.IntVar() # Variable qui représente le parier entré.
    sclValeur['from'] = 1
    sclValeur['to'] = Valeur
    sclValeur['orient'] = "horizontal"
    sclValeur['background'] = 'yellow'
    sclValeur['variable'] = Bet
    sclValeur.grid(row=3,column=1,pady=48,rowspan=4,columnspan=5,padx=21,sticky=tk.NE)
    btnOk2 = tk.Button(fenetre) # Bouton pour faire progresser le programme.
    btnOk2['text'] = "OK"
    btnOk2['font'] = ("Arial 12")
    btnOk2['command'] = cliqueOK
    btnOk2.grid(row=2,column=2,rowspan=2,columnspan=5,padx=120,sticky=tk.SE)
def cliqueOui(): # Fonction pour réinitialiser le jeu après une ronde de jouer.
    global Points2
    global Points3
    global Points1
    global Bouton
    global lblContinue
    global lblGagnant
    global lblBet2
    global btnOui
    global Dealer
    global Column2
    global Column3
    global Image2
    global Image
    global Column
    global Bouton2
    global Deux
    global Points4
    global Points5
    global Stand
    global Deux2
    global Double
    global Affiche
    global Unefois
    global cliqueJeu_thread
    global Double3
    global Oui
    Dealerhand2.clear() # On utilise ceci pour recommmencer le tableau pour le prochain jeu.
    As.clear()
    As2.clear()
    paquet.clear()
    Asdouble.clear()
    Asdouble2.clear()
    Dealerlist.clear()
    Points1 = 0 # On remet les points à zéro pour la prochaine ronde.
    Points2 = 0
    Points3 = 0
    Points4 = 0
    Points5 = 0
    Stand = 0 # On remet quelques variables à 0 pour éviter des erreurs dans la prochaine joute.
    Deux2 = 0
    Double = 0
    Affiche = 0
    Unefois = 0
    Double3 = 0
    Oui = 0
    for i4 in range(1,52): # On réinitialise le paquet des cartes.
            paquet.append(i4)
    for i5 in range(0,len(Joueur)): # On enlève les cartes (images) de l'écran.
        Carte = Joueur[i5]
        Carte.destroy()
    Joueur.clear() # On enlève tout ce qui se présente sur l'écarn pour la prochaine ronde.
    Joueur2.clear()
    CarteCouverte.destroy()
    lblPoints2.destroy()
    lblPoints1.destroy()
    lblGagnant.destroy()
    lblBet2.destroy()
    lblContinue.destroy()
    btnOui.destroy()
    lblValeur.destroy()
    lblBet.destroy()
    btnCarte.destroy()
    btnStand.destroy()
    btnNon.destroy()
    Column2 = 3
    Column3 = 7
    Image2 = 65
    Image = 2
    Column = 4
    Bouton = 0
    Dealer = 0
    Bouton2 = 0
    Deux = 0
    if Valeur >= 1: # On peut mettre un parier si on a au moins un point, ce qui veut dire une autre joute.
        cliqueBet()
    else: # Si Valeur est zéro, on affiche que le jeu est fini et un chronomètre se met à fonctionner.
        lblJeu = tk.Label(fenetre)
        lblJeu['text'] = "Jeu fini! Il n'y a plus de points. Merci pour jouer."
        lblJeu['font'] = ("Arial 16")
        lblJeu['background'] = "yellow"
        lblJeu.grid(row=2, column=2, columnspan=8, rowspan=3, sticky=tk.W)
        cliqueJeu_thread = threading.Thread(target=cliqueJeu,daemon=True) # Thread pour le chronomètre.
        cliqueJeu_thread.start()
def cliqueNon(): # Si on clique Non après une ronde, le jeu se ferme.
    fenetre.destroy()
def cliqueJeu(): # Fonction pour le chronomètre.
    Temps = 3 # Il y a 3 secondes sur le chronomètre.
    for x in range(3):
        Temps = Temps - 1
        time.sleep(1)
    fenetre.destroy() # Après trois secondes, le jeu se ferme.
# ------------------------------------------
# Importations de modules:
import tkinter as tk # On importe les modules nécessaires pour faire fonctionner le programme graphique.
import random
import time
import threading
import math
# ------------------------------------------
# Programme principale:
Column2 = 3 # Ceux-ci sont les différents variables utilisés à travers du programme pour le faire performer les fonctions désirées.
Column3 = 7
Image2 = 65
Image = 2
Column = 4
Bouton = 0
Image3 = 0
Deux = 0
Points3 = 0
Points4 = 0
Points5 = 0
Test = 0
Points1 = 0
Bouton3 = 0
Joueur = []
Points2 = 0
Dealer = 0
Bouton2 = 0
Affiche = 0
paquet = [] # Utilisation de tableaux pour sauvegarder les valeurs des cartes, le pointage et les labels des cartes.
paquet2 = []
As = []
As2 = []
Asdouble = []
Asdouble2 = []
Dealerhand2 = []
Oui = 0
Double = 0
Double2 = 0
PointsDealer = 0
Double3 = 0
Deux2 = 0
Stand = 0
Unefois = 0
Valeur2 = 0
Joueur2 = []
Dealerlist = []
for i in range(1,52): # Génération du paquet de cartes. paquet2 est ajouté pour avoir tous les valeurs des cartes pendant tout le jeu.
    paquet.append(i)
    paquet2.append(i)
Valeur = 1000 # Valeur initiale des points.
fenetre = tk.Tk() # Création du fenêtre de jeu.
fenetre.title("Blackjack")
fenetre.geometry("700x500")
fenetre['background'] = "yellow"
Nombres = []
for Vie in range(0,53):
    Nombres.append(tk.PhotoImage(file=str(Vie)+".gif")) # Tableau pour sauvegarder les images du fichier dans le programme.
lblJoueur = tk.Label(fenetre)
lblJoueur['font'] = ("Arial 12")
lblJoueur['background'] = "yellow"
lblJoueur.grid(row=3, column=1, padx=25, pady=100, sticky=tk.NE, rowspan=2, columnspan=5)
imgPersonne = tk.PhotoImage(file="Blackjackdealer.gif") # Image de dealer.
lblPersonne = tk.Label(fenetre)
lblPersonne['image'] = imgPersonne
lblPersonne['background'] = 'yellow'
lblPersonne.grid(columnspan=10,row=0,sticky=tk.NW,rowspan=8,padx=275)
btnCommence = tk.Button(fenetre) # Permet de faire avancer le programme à la fonction cliqueJoueur.
btnCommence['text'] = "Clique ici pour commencer"
btnCommence['font'] = ("Arial 10")
btnCommence['command'] = cliqueJoueur
btnCommence.grid(sticky=tk.W,row=4,column=3,pady=10,columnspan=8,rowspan=4,padx=91)
Regleslist = [] # Liste permettant le boucle for de générer les règles du jeu.
for Regles in range(15):
    Regles2 = Regles # Permet de sauvegarder la valeur numérique du loop pour l'utiliser dans les condition booléens.
    (Regles) = tk.Label(fenetre) # Création des labels pour les règles du jeu, la valeur est différent à chaque répetition du boucle, ce qui génére un différent label.
    (Regles)['font'] = ("Arial 10")
    (Regles)['background'] = "yellow"
    Regleslist.append(Regles) # Permet de plus tard enlever les règles.
    # Conditions booléens pour positionner les règles du jeu.
    if Regles2 == 0:
        Regles['text'] = "Bienvenue à Blackjack! Voici les règles:"
        Regles.grid(row=1, columnspan=5, rowspan=4, sticky=tk.NE, pady=125, padx=67)
    elif Regles2 == 1:
        Regles['text'] = "Le but est d'avoir un pointage qui est le plus proche de 21, sans le dépasser."
        Regles.grid(row=2, column=2, columnspan=7, rowspan=4, sticky=tk.N, pady=150)
    elif Regles2 == 2:
        Regles['text'] = "Tu vas mettre un parier contre l'ordinateur, si tu perds, tu perds le montant dans le parier."
        Regles.grid(row=1, column=1, columnspan=5, rowspan=4, sticky=tk.NE, pady=180, padx=95)
    elif Regles2 == 3:
        Regles['text'] = "Si tu as un pointage de plus de 21, tu perds."
        Regles.grid(row=1, column=2, columnspan=4, rowspan=4, sticky=tk.N, pady=210, padx=95)
    elif Regles2 == 4:
        Regles['text'] = "Un pointage moins que 21, mais l'ordinateur à un meilleur pointage <= 21 et tu perds."
        Regles.grid(row=1, column=2, columnspan=4, rowspan=4, sticky=tk.NE, pady=230, padx=95)
    elif Regles2 == 5:
        Regles['text'] = "Si tu as un blackjack, tu gagnes double ton parier et + 50 points."
        Regles.grid(row=2, column=2, columnspan=4, rowspan=3, sticky=tk.N, pady=270, padx=95)
    elif Regles2 == 6:
        Regles['text'] = "Si les points sont égaux, tu gardes ton parier."
        Regles.grid(row=2, column=2, columnspan=4, rowspan=3, sticky=tk.S, pady=250, padx=70)
    elif Regles2 == 7:
        Regles['text'] = "Si tu as un meilleur pointage que l'ordinateur <= 21, tu gagnes."
        Regles.grid(row=2, column=2, columnspan=4, rowspan=3, sticky=tk.S, pady=250, padx=70)
    elif Regles2 == 8:
        Regles['text'] = "L'ordinateur doit prendre une carte jusqu'à 17."
        Regles.grid(row=2, column=2, columnspan=4, rowspan=3, sticky=tk.S, pady=250, padx=70)
    elif Regles2 == 9:
        Regles['text'] = "Les as vaut 1 ou 11, les figures 10 et les cartes numériques leur valeur propre."
        Regles.grid(row=2, column=2, columnspan=4, rowspan=3, sticky=tk.S, pady=250, padx=70)
    elif Regles2 == 10:
        Regles['text'] = "Si tu reçois deux cartes avec la même valeur, tu peux faire un split (Un par jeu seulement)."
        Regles.grid(row=2, column=2, columnspan=4, rowspan=3, sticky=tk.S, pady=225, padx=70)
    elif Regles2 == 11:
        Regles['text'] = "Si tu fais ceci, tu dois mettre la moitié de ton parier original dans ce split."
        Regles.grid(row=2, column=2, columnspan=4, rowspan=3, sticky=tk.S, pady=199, padx=50)
    elif Regles2 == 12:
        Regles['text'] = "Si tu ne peux pas faire ceci, tu ne peux pas faire un split."
        Regles.grid(row=2, column=2, columnspan=4, rowspan=3, sticky=tk.S, pady=180, padx=50)
    elif Regles2 == 13:
        Regles['text'] = "Si tu as 0 points, le jeu se termine."
        Regles.grid(row=2, column=2, columnspan=4, rowspan=3, sticky=tk.S, pady=160, padx=50)
    else:
        Regles['text'] = "Bonne chance!"
        Regles.grid(row=2, column=2, columnspan=4, rowspan=3, sticky=tk.S, pady=140, padx=50)
fenetre.mainloop() # Permet de faire jouer le boucle de l'interface graphique.