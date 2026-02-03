import Maria_Peigne_monde_2
from tkinter import *
from time import sleep
from random import *
import pygame
import time

# ---VARIABLES ET PARAMETRAGE---
# Version miniature - cases de 20px au lieu de 50px
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
longueur_case = 20  # Réduit de 50 à 20
decalage = 10       # Réduit de 25 à 10
pygame.mixer.init()
pygame.mixer.Channel(3).play(pygame.mixer.Sound('Sons/vent_m1.mp3'))

# ---CREATION BASE---
# Création de la fenêtre maîtresse
COLOR = "black"
root = Tk()
root.title("Maria Peigne - Vue Mini")
root.configure(bg='black')

# Dimensions du jeu (réduites proportionnellement)
GAME_WIDTH = 600   # 30 cases * 20px
GAME_HEIGHT = 400  # 20 cases * 20px

# Centrer la fenêtre
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - GAME_WIDTH) // 2
y = (screen_height - GAME_HEIGHT) // 2
root.geometry(f"{GAME_WIDTH + 20}x{GAME_HEIGHT + 20}+{x}+{y}")

# Création d'un canevas
cnv = Canvas(root, width = GAME_WIDTH, height = GAME_HEIGHT, bg='black', highlightthickness=0)
cnv.pack(padx=10, pady=10)

# Bind Escape pour quitter
root.bind('<Escape>', lambda e: root.destroy())


# ---CREATION TEXTURE UTILISEES---
# Création fond
fondvert = PhotoImage(file=r"Textures\monde1.png").subsample(2, 2)  # Réduit par 2
fv = cnv.create_image(300, 144, image=fondvert)

# Création portail
portail_ferme = PhotoImage(file = r"Textures\portail_ferme_m1.png").subsample(2, 2)
portail_ouvert = PhotoImage(file = r"Textures\portail_ouvert_m1.png").subsample(2, 2)

# Création des murs
brique = PhotoImage(file = r"Textures\mur_brique_m1.png").subsample(2, 2)

# Création des clés
clef1 = PhotoImage(file = r"Textures\clé_rubis_m1.png").subsample(2, 2)
clef2 = PhotoImage(file = r"Textures\clé_emeraude_m1.png").subsample(2, 2)
clef3 = PhotoImage(file = r"Textures\clé_saphir_m1.png").subsample(2, 2)

# Création sol
sol = PhotoImage(file = r"Textures\sable_m1.png").subsample(2, 2)
i = cnv.create_image(300, 380, image = sol)

# Création cactus
cactus_haut = PhotoImage(file = r"Textures\Cactus_haut_m1.png").subsample(2, 2)
cactus_bas = PhotoImage(file = r"Textures\Cactus_bas_m1.png").subsample(2, 2)

# Création lierre
feuille = PhotoImage(file = r"Textures\lierre_m1.png").subsample(2, 2)

# ---CREATION, CLASSE ET FONCTIONS---
matrix = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,0,-10,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,-10,1],
          [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,-10,1],
          [1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,-10,1],
          [1,0,0,1,0,-9,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,-10,1],
          [1,0,0,1,1,1,1,0,0,1,0,-9,0,0,0,1,1,1,1,0,0,0,0,0,-9,0,1,0,0,1],
          [1,0,0,0,0,0,1,0,0,1,0,-7,0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1],
          [1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
          [1,0,0,1,0,0,1,0,0,-10,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
          [1,0,0,1,0,0,1,0,0,-10,0,0,0,0,0,0,0,-9,0,0,0,1,1,1,1,0,0,1,1,1],
          [1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,-10,0,1],
          [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,-10,0,1],
          [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0,0,1],
          [1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1],
          [1,0,0,0,0,0,-10,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1],
          [1,0,-8,-5,0,0,-10,0,0,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1],
          [1,1,1,1,1,1,1,-4,-9,1,0,0,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,0,-9,1],
          [1,0,0,0,0,0,-2,-3,-7,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-9,-7,1],
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
            Porte_ferme = cnv.create_image((longueur_case*j-10),(longueur_case*i+5), image = portail_ferme)
        elif matrix[i][j] == -9:
            Cactus_haut = cnv.create_image(decalage+(longueur_case*j), decalage+(longueur_case*i), image = cactus_haut)
        elif matrix[i][j] == -7:
            Cactus_bas = cnv.create_image(decalage+(longueur_case*j), decalage+(longueur_case*i), image = cactus_bas)
        elif matrix[i][j] == -10:
            lierre = cnv.create_image(decalage+(longueur_case*j), decalage+(longueur_case*i), image = feuille)

# Affiche les clés trouvées
def comptage_clef():
    global clef_obtenue
    clef_obtenue += 1
    
# Détecte si le joueur à touché une clé
def clef_trouvee():
    if matrix[mariacoord.y][mariacoord.x] == -2:
        matrix[mariacoord.y][mariacoord.x] = 0
        sons_clef()
        cnv.delete(clef1_cnv)
        comptage_clef()
        fin_du_jeu()
    if matrix[mariacoord.y][mariacoord.x] == -3:
        matrix[mariacoord.y][mariacoord.x] = 0
        sons_clef()
        cnv.delete(clef2_cnv)
        comptage_clef()
        fin_du_jeu()
    if matrix[mariacoord.y][mariacoord.x] == -4:
        matrix[mariacoord.y][mariacoord.x] = 0
        sons_clef()
        cnv.delete(clef3_cnv)
        comptage_clef()
        fin_du_jeu()

# Son pour l'ouverture de porte
def son_portail():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sons/ouverture_portail_m1.mp3"))

# Sons pour les pas
def sons_pas():
    num = randint(0,2)
    if num == 0:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sons/pas1_m1.mp3'))
    if num == 1:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sons/pas2_m1.mp3'))
    if num == 2:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sons/pas3_m1.mp3'))
        
def sons_clef():
    num = randint(0,2)
    if num == 0:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('Sons/clef1_m1.mp3'))
    if num == 1:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('Sons/clef2_m1.mp3'))
    if num == 2:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('Sons/clef3_m1.mp3'))

# Vérifie le nombre de clés trouvées
def fin_du_jeu():
    if clef_obtenue == 3:
        son_portail()
        cnv.itemconfig(Porte_ferme, image = portail_ouvert)
    
# Ouvrir monde 1 sur monde 2
def fermer_fenetre():
    root.destroy()

# ---MARIA---
# Coordonnées apparition Maria
class Coord():
    x = 1
    y = 17
mariacoord = Coord()

# Création Maria
Maria = PhotoImage(file = r"Textures\Maria.png").subsample(2, 2)
Maria2 = PhotoImage(file = r"Textures\Maria2.png").subsample(2, 2)
img = cnv.create_image(0,0, image = Maria)

def affichage_maria():
    cnv.move(img, decalage+(longueur_case*mariacoord.x), decalage+(longueur_case*mariacoord.y))
affichage_maria()

# Mouvement effectués
def move(event):
    if event.char == 'z': #si touche 'avancer' appuyée
        if matrix[mariacoord.y-1][mariacoord.x] <=0 : #si pas de mur
            sons_pas()
            mariacoord.y -= 1
            cnv.move(img, 0, -longueur_case)
            clef_trouvee() #test si clé
    elif event.char == 's': #si touche 'reculer' appuyée
        if matrix[mariacoord.y+1][mariacoord.x] <=0 : #si pas de mur
            sons_pas()
            mariacoord.y += 1 
            cnv.move(img, 0, longueur_case)
            clef_trouvee() #test si clé
    elif event.char == 'q': #si touche 'gauche' appuyée
        if matrix[mariacoord.y][mariacoord.x-1] <=0 : #si pas de mur
            sons_pas()
            mariacoord.x -= 1
            cnv.itemconfig(img, image = Maria2)
            cnv.move(img, -longueur_case, 0)
            clef_trouvee() #test si clé
    elif event.char == 'd': #si touche 'droite' appuyée
        if matrix[mariacoord.y][mariacoord.x+1] <=0 : #si pas de mur
            sons_pas()
            mariacoord.x += 1
            cnv.itemconfig(img, image = Maria)
            cnv.move(img, longueur_case, 0)
            clef_trouvee() #test si clé
    elif event.char == 'a': #si espace appuyé
        if matrix[mariacoord.y][mariacoord.x] == -8 and clef_obtenue == 3: #si sur porte et toutes clés obtenues
            root.destroy()
            Maria_Peigne_monde_2.lancer_monde()
          
          
root.resizable(False, False)
root.bind("<Key>", move) #bind pour associe événement à fonction
root.mainloop() #lance fenêtre
