# Version mini du Monde 2 - Mausolée
# Cases réduites à 20px pour voir tout le niveau

from tkinter import *
from time import sleep
from random import *

# ---VARIABLES ET PARAMETRAGE---
clef_obtenue = 0
longueur_case = 20  # Réduit de 50 à 20
decalage = 10  # Réduit de 25 à 10

# ---CREATION BASE---
root = Tk()
root.title("Maria Peigne - Monde 2 Mini")
root.configure(bg='black')
root.bind('<Escape>', lambda e: root.destroy())

# Dimensions réduites (600x400 au lieu de 1500x1000)
GAME_WIDTH = 600
GAME_HEIGHT = 400

cnv = Canvas(root, width=GAME_WIDTH, height=GAME_HEIGHT, bg='black', highlightthickness=0)
cnv.pack()

# ---CREATION TEXTURE UTILISEES (avec subsample pour réduire)---
# Création fond
fondvert = PhotoImage(file=r"Textures\moul.png").subsample(2, 2)
fv = cnv.create_image(300, 144, image=fondvert)

# Création portail
portail_ferme = PhotoImage(file=r"Textures\portail_ferme_m2.png").subsample(2, 2)
portail_ouvert = PhotoImage(file=r"Textures\portail_ouvert_m2.png").subsample(2, 2)

# Création des murs
brique = PhotoImage(file=r"Textures\mur_pierre_m2.png").subsample(2, 2)

# Création des cristaux
clef1 = PhotoImage(file=r"Textures\cristal_violet_m2.png").subsample(2, 2)
clef2 = PhotoImage(file=r"Textures\cristal_bleu_m2.png").subsample(2, 2)
clef3 = PhotoImage(file=r"Textures\cristal_vert_m2.png").subsample(2, 2)

# Création sol
sol = PhotoImage(file=r"Textures\sol_m2.png").subsample(2, 2)
i = cnv.create_image(300, 380, image=sol)


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
            mur = cnv.create_image(decalage+(longueur_case*j), decalage+(longueur_case*i), image=brique)
        elif matrix[i][j] == -2:
            clef1_cnv = cnv.create_image(decalage+(longueur_case*j), decalage+(longueur_case*i), image=clef1)
        elif matrix[i][j] == -3:
            clef2_cnv = cnv.create_image(decalage+(longueur_case*j), decalage+(longueur_case*i), image=clef2)
        elif matrix[i][j] == -4:
            clef3_cnv = cnv.create_image(decalage+(longueur_case*j), decalage+(longueur_case*i), image=clef3)
        elif matrix[i][j] == -5:
            Porte_ferme = cnv.create_image((longueur_case*j-10), (longueur_case*i+5), image=portail_ferme)

# Affiche les clés trouvées
def comptage_clef():
    global clef_obtenue
    clef_obtenue += 1

# Détecte si le joueur à touché une clé
def clef_trouvee():
    global clef_obtenue
    if matrix[mariacoord.y][mariacoord.x] == -2:
        matrix[mariacoord.y][mariacoord.x] = 0
        cnv.delete(clef1_cnv)
        comptage_clef()
        fin_du_jeu()
    if matrix[mariacoord.y][mariacoord.x] == -3:
        matrix[mariacoord.y][mariacoord.x] = 0
        cnv.delete(clef2_cnv)
        comptage_clef()
        fin_du_jeu()
    if matrix[mariacoord.y][mariacoord.x] == -4:
        matrix[mariacoord.y][mariacoord.x] = 0
        cnv.delete(clef3_cnv)
        comptage_clef()
        fin_du_jeu()
    if matrix[mariacoord.y][mariacoord.x] == -8 and clef_obtenue == 3:
        cnv.delete(img)
        widget = Label(cnv, text='Bravo ! Monde 2 terminé !', fg='white', bg='#8B008B', width=40, height=3)
        widget.config(font=("Arial", 12))
        widget.pack()
        cnv.create_window(300, 200, window=widget)

# Vérifie le nombre de clés trouvées
def fin_du_jeu():
    if clef_obtenue == 3:
        cnv.itemconfig(Porte_ferme, image=portail_ouvert)


# ---MARIA---
# Coordonnées apparition Maria
class Coord():
    x = 1
    y = 17
mariacoord = Coord()

# Création Maria (avec subsample)
Maria = PhotoImage(file=r"Textures\Maria.png").subsample(2, 2)
Maria2 = PhotoImage(file=r"Textures\Maria2.png").subsample(2, 2)
img = cnv.create_image(0, 0, image=Maria)

def affichage_maria():
    cnv.move(img, decalage+(longueur_case*mariacoord.x), decalage+(longueur_case*mariacoord.y))
affichage_maria()

# Mouvement effectués
def move(event):
    if event.char == 'z':
        if matrix[mariacoord.y-1][mariacoord.x] <= 0:
            mariacoord.y -= 1
            cnv.move(img, 0, -longueur_case)
            clef_trouvee()
    elif event.char == 's':
        if matrix[mariacoord.y+1][mariacoord.x] <= 0:
            mariacoord.y += 1
            cnv.move(img, 0, longueur_case)
            clef_trouvee()
    elif event.char == 'q':
        if matrix[mariacoord.y][mariacoord.x-1] <= 0:
            mariacoord.x -= 1
            cnv.itemconfig(img, image=Maria2)
            cnv.move(img, -longueur_case, 0)
            clef_trouvee()
    elif event.char == 'd':
        if matrix[mariacoord.y][mariacoord.x+1] <= 0:
            mariacoord.x += 1
            cnv.itemconfig(img, image=Maria)
            cnv.move(img, longueur_case, 0)
            clef_trouvee()


root.resizable(False, False)
root.bind("<Key>", move)
root.mainloop()
