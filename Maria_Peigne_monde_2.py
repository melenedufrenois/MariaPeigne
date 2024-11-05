from tkinter import *
from time import sleep
from random import *
# import pygame

def lancer_monde():
    # ---VARIABLES ET PARAMETRAGE---
    #1 = mur
    #5 = sol
    #-8 = collision pour la porte
    #-7 = bas cactus
    #-9 = haut cactus
    #-2 = clef1
    #-3 = clef2
    #-4 = clef3
    #-5 ou 10 = portail
    #-6 ou 11 = portail ouvert
    #-10 = lierre
    clef_obtenue = 0
    longueur_case = 50
    decalage = 25
    # pygame.mixer.init()
    # pygame.mixer.Channel(3).play(pygame.mixer.Sound('Sons/vent.mp3'))

    # ---CREATION BASE---
    # Création de la fenêtre maîtresse
    COLOR = "black"
    root = Tk()
    root.title("Maria Peigne")

    # Création d'un canevas (=widget permettant d'effectuer du graphisme, des animations, etc)
    cnv = Canvas(root, width = 1500, height = 1000)
    cnv.pack()


    # ---CREATION TEXTURE UTILISEES---
    # Création fond
    fondvert = PhotoImage(file="Textures\moul.png") #convertir pr Tkinter
    fv = cnv.create_image(750, 360, image=fondvert)

    # Création portail
    portail_ferme = PhotoImage(file = "Textures\portail_ferme_m2.png")
    portail_ouvert = PhotoImage(file = "Textures\portail_ouvert_m2.png")

    # Création des murs
    brique = PhotoImage(file = "Textures\mur_pierre_m2.png")  #Utilisation PhotoImage (= Format propre à Tkinter) pour convertir l'image en précisant son adresse sur le disque

    # Création des cristaux
    clef1 = PhotoImage(file = "Textures\cristal_violet_m2.png")
    clef2 = PhotoImage(file = "Textures\cristal_bleu_m2.png")
    clef3 = PhotoImage(file = "Textures\cristal_vert_m2.png")

    # Création sol
    sol = PhotoImage(file = "Textures\sol_m2.png")
    i = cnv.create_image(750, 950, image = sol)


    # ---CREATION, CLASSE ET FONCTIONS---
    matrix = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,-4,0,0,0,0,0,0,1],
              [1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1],
              [1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
              [1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1],
              [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1],
              [1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
              [1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
              [1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1],
              [1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1],
              [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,-2,0,1,0,0,0,0,1,0,0,0,0,0,1],
              [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0,0,1],
              [1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1],
              [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1],
              [1,0,-8,-5,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1],
              [1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1],
              [1,0,0,0,0,0,0,0,0,1,0,-3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
              [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]

    # Placement texture selon matrice
    for i in range(20):
        for j in range(30):
            if matrix[i][j] == 1:
                mur = cnv.create_image(decalage+(longueur_case*j), decalage+(longueur_case*i), image = brique)
            elif matrix[i][j] == -2:
                clef1_cnv = cnv.create_image(decalage+(longueur_case*j), decalage+(longueur_case*i), image = clef1)
            elif matrix[i][j] == -3:
                clef2_cnv = cnv.create_image(decalage+(longueur_case*j), decalage+(longueur_case*i), image = clef2)
            elif matrix[i][j] == -4:
                clef3_cnv = cnv.create_image(decalage+(longueur_case*j), decalage+(longueur_case*i), image = clef3)
            elif matrix[i][j] == -5:
                Porte_ferme = cnv.create_image((longueur_case*j-25),(longueur_case*i+12), image = portail_ferme)

    # Affiche les clés trouvées
    def comptage_clef():
        global clef_obtenue
        clef_obtenue += 1
        
    # Détecte si le joueur à touché une clé
    def clef_trouvee():
        if matrix[mariacoord.y][mariacoord.x] == -2:
            matrix[mariacoord.y][mariacoord.x] = 0
            #sons_clef()
            cnv.delete(clef1_cnv)
            comptage_clef()
            fin_du_jeu()
        if matrix[mariacoord.y][mariacoord.x] == -3:
            matrix[mariacoord.y][mariacoord.x] = 0
            #sons_clef()
            cnv.delete(clef2_cnv)
            comptage_clef()
            fin_du_jeu()
        if matrix[mariacoord.y][mariacoord.x] == -4:
            matrix[mariacoord.y][mariacoord.x] = 0
            #sons_clef()
            cnv.delete(clef3_cnv)
            comptage_clef()
            fin_du_jeu()
        if matrix[mariacoord.y][mariacoord.x] == -8 and clef_obtenue == 3:
            cnv.delete(img)
            widget = Label(cnv, text='Fin de la démo, payer 59.99€ pour la partie 2 ! \n Jeu réalisé par Mélène, Eva et Ethan', fg='black', bg='#FF7F00', width = 100, height = 5)
            widget.config(font=("Arial", 20))
            widget.pack()
            cnv.create_window(750, 370, window=widget)

    # # Son pour l'ouverture de porte
    # def son_portail():
    #     pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sons/ouverture_portail.mp3"))
    # 
    # # Sons pour les pas
    # def sons_pas():
    #     num = randint(0,2)
    #     if num == 0:
    #         pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sons/pas1.mp3'))
    #     if num == 1:
    #         pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sons/pas2.mp3'))
    #     if num == 2:
    #         pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sons/pas3.mp3'))
    #         
    # def sons_clef():
    #     num = randint(0,2)
    #     if num == 0:
    #         pygame.mixer.Channel(2).play(pygame.mixer.Sound('Sons/clef1.mp3'))
    #     if num == 1:
    #         pygame.mixer.Channel(2).play(pygame.mixer.Sound('Sons/clef2.mp3'))
    #     if num == 2:
    #         pygame.mixer.Channel(2).play(pygame.mixer.Sound('Sons/clef3.mp3'))

    # Vérifie le nombre de clés trouvées
    def fin_du_jeu():
        if clef_obtenue == 3:
            #son_portail()
            cnv.itemconfig(Porte_ferme, image = portail_ouvert)


    # ---MARIA---
    # Coordonnées apparition Maria
    class Coord():
        x = 1
        y = 17
    mariacoord = Coord()

    # Création Maria
    Maria = PhotoImage(file = "Textures\Maria.png")
    Maria2 = PhotoImage(file = "Textures\Maria2.png") 
    img = cnv.create_image(0,0, image = Maria)

    def affichage_maria():
        cnv.move(img, 25+(50*mariacoord.x), 25+(50*mariacoord.y))
    affichage_maria()

    # Mouvement effectués
    def move(event):
        if event.char == 'z': #si touche 'avancer' appuyée
            if matrix[mariacoord.y-1][mariacoord.x] <=0 : #si pas de mur
                #sons_pas()
                mariacoord.y -= 1
                cnv.move(img, 0, -50)
                clef_trouvee() #test si clé
        elif event.char == 's': #si touche 'reculer' appuyée
            if matrix[mariacoord.y+1][mariacoord.x] <=0 : #si pas de mur
                #sons_pas()
                mariacoord.y += 1 
                cnv.move(img, 0, 50)
                clef_trouvee() #test si clé
        elif event.char == 'q': #si touche 'gauche' appuyée
            if matrix[mariacoord.y][mariacoord.x-1] <=0 : #si pas de mur
                #sons_pas()
                mariacoord.x -= 1
                cnv.itemconfig(img, image = Maria2)
                cnv.move(img, -50, 0)
                clef_trouvee() #test si clé
        elif event.char == 'd': #si touche 'droite' appuyée
            if matrix[mariacoord.y][mariacoord.x+1] <=0 : #si pas de mur
                #sons_pas()
                mariacoord.x += 1
                cnv.itemconfig(img, image = Maria)
                cnv.move(img, 50, 0)
                clef_trouvee() #test si clé
              
              
    root.resizable(False, False)
    root.bind("<Key>", move) #bind pour associe événement à fonction
    root.mainloop() #lance fenêtre