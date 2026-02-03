"""
Visualiseur de matrice - Maria Peigne
Permet de voir les niveaux en miniature
"""

from tkinter import *

# Taille des cases (petites pour vue d'ensemble)
TAILLE_CASE = 20

# Couleurs pour chaque type d'élément
COULEURS = {
    0: "#2d2d2d",      # Sol vide - gris foncé
    1: "#8B4513",      # Mur - marron
    5: "#F4A460",      # Sol affiché - sable
    -2: "#FF0000",     # Clé 1 - rouge (rubis)
    -3: "#00FF00",     # Clé 2 - vert (émeraude)
    -4: "#0000FF",     # Clé 3 - bleu (saphir)
    -5: "#800080",     # Portail fermé - violet
    -6: "#FF00FF",     # Portail ouvert - magenta
    -7: "#228B22",     # Cactus bas - vert forêt
    -8: "#FFD700",     # Zone portail - or
    -9: "#32CD32",     # Cactus haut - lime
    -10: "#90EE90",    # Lierre - vert clair
}

# Matrices des mondes
MONDE_1 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
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
    [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
]

MONDE_2 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
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
    [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
]

def afficher_monde(matrix, titre):
    """Affiche une matrice dans une fenêtre"""
    root = Tk()
    root.title(titre)
    root.configure(bg='black')
    
    # Calcul des dimensions
    lignes = len(matrix)
    colonnes = len(matrix[0])
    width = colonnes * TAILLE_CASE
    height = lignes * TAILLE_CASE
    
    # Canvas
    cnv = Canvas(root, width=width, height=height, bg='black', highlightthickness=0)
    cnv.pack(padx=10, pady=10)
    
    # Dessin de la matrice
    for i in range(lignes):
        for j in range(colonnes):
            valeur = matrix[i][j]
            couleur = COULEURS.get(valeur, "#FFFFFF")
            
            x1 = j * TAILLE_CASE
            y1 = i * TAILLE_CASE
            x2 = x1 + TAILLE_CASE
            y2 = y1 + TAILLE_CASE
            
            cnv.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="#1a1a1a")
    
    # Légende
    legende = Frame(root, bg='black')
    legende.pack(pady=10)
    
    Label(legende, text="Légende:", fg='white', bg='black', font=('Arial', 10, 'bold')).pack()
    
    legendes = [
        ("Mur", "#8B4513"),
        ("Sol", "#2d2d2d"),
        ("Clé 1", "#FF0000"),
        ("Clé 2", "#00FF00"),
        ("Clé 3", "#0000FF"),
        ("Portail", "#FFD700"),
        ("Cactus", "#228B22"),
        ("Lierre", "#90EE90"),
    ]
    
    frame_leg = Frame(legende, bg='black')
    frame_leg.pack()
    
    for idx, (nom, couleur) in enumerate(legendes):
        f = Frame(frame_leg, bg='black')
        f.grid(row=idx//4, column=idx%4, padx=5, pady=2)
        Canvas(f, width=15, height=15, bg=couleur, highlightthickness=1).pack(side=LEFT, padx=2)
        Label(f, text=nom, fg='white', bg='black', font=('Arial', 8)).pack(side=LEFT)
    
    # Position spawn Maria
    Label(legende, text="🔵 Spawn Maria: (1, 17)", fg='cyan', bg='black', font=('Arial', 9)).pack(pady=5)
    
    root.mainloop()

def menu_principal():
    """Menu pour choisir quel monde afficher"""
    root = Tk()
    root.title("Visualiseur de Matrice - Maria Peigne")
    root.configure(bg='#1a1a1a')
    root.geometry("300x200")
    
    Label(root, text="🗺️ Visualiseur de Matrice", fg='white', bg='#1a1a1a', 
          font=('Arial', 14, 'bold')).pack(pady=20)
    
    def ouvrir_monde1():
        root.destroy()
        afficher_monde(MONDE_1, "Monde 1 - Désert")
    
    def ouvrir_monde2():
        root.destroy()
        afficher_monde(MONDE_2, "Monde 2 - Mausolée")
    
    Button(root, text="🏜️ Monde 1 - Désert", command=ouvrir_monde1,
           font=('Arial', 11), width=20, bg='#F4A460').pack(pady=10)
    
    Button(root, text="🏛️ Monde 2 - Mausolée", command=ouvrir_monde2,
           font=('Arial', 11), width=20, bg='#708090').pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    menu_principal()
