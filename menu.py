# Menu Principal - Maria Peigne
# Lance le jeu ou accède au mode admin (visualisation des niveaux)

from tkinter import *
import subprocess
import sys
import os

class MenuPrincipal:
    def __init__(self):
        self.root = Tk()
        self.root.title("Maria Peigne - Menu Principal")
        
        # Couleurs sobres
        self.bg_color = "#1e1e2e"
        self.text_color = "#cdd6f4"
        self.accent_color = "#89b4fa"
        self.secondary_color = "#a6adc8"
        self.btn_color = "#45475a"
        self.btn_hover = "#585b70"
        
        self.root.configure(bg=self.bg_color)
        
        # Mode plein écran
        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', lambda e: self.root.destroy())
        
        # Frame conteneur centré
        self.container = Frame(self.root, bg=self.bg_color)
        self.container.place(relx=0.5, rely=0.5, anchor='center')
        
        self.creer_interface()
        
    def creer_interface(self):
        # Titre du jeu
        titre = Label(
            self.container, 
            text="Maria Peigne", 
            font=("Segoe UI", 48, "bold"),
            fg=self.text_color,
            bg=self.bg_color
        )
        titre.pack(pady=(0, 10))
        
        # Sous-titre
        sous_titre = Label(
            self.container, 
            text="Collecte les 3 clés pour ouvrir le portail", 
            font=("Segoe UI", 14),
            fg=self.secondary_color,
            bg=self.bg_color
        )
        sous_titre.pack(pady=(0, 40))
        
        # Frame pour les boutons
        frame_boutons = Frame(self.container, bg=self.bg_color)
        frame_boutons.pack(pady=10)
        
        # Bouton Jouer
        btn_jouer = Label(
            frame_boutons,
            text="Jouer",
            font=("Segoe UI", 16, "bold"),
            fg="#1e1e2e",
            bg=self.accent_color,
            width=18,
            height=2,
            cursor='hand2'
        )
        btn_jouer.pack(pady=10)
        btn_jouer.bind('<Button-1>', lambda e: self.lancer_jeu())
        btn_jouer.bind('<Enter>', lambda e: btn_jouer.config(bg="#7ba3e8"))
        btn_jouer.bind('<Leave>', lambda e: btn_jouer.config(bg=self.accent_color))
        
        # Bouton Paramètres
        btn_admin = Label(
            frame_boutons,
            text="Paramètres",
            font=("Segoe UI", 14),
            fg=self.text_color,
            bg=self.btn_color,
            width=18,
            height=2,
            cursor='hand2'
        )
        btn_admin.pack(pady=10)
        btn_admin.bind('<Button-1>', lambda e: self.ouvrir_menu_admin())
        btn_admin.bind('<Enter>', lambda e: btn_admin.config(bg=self.btn_hover))
        btn_admin.bind('<Leave>', lambda e: btn_admin.config(bg=self.btn_color))
        
        # Bouton Quitter
        btn_quitter = Label(
            frame_boutons,
            text="Quitter",
            font=("Segoe UI", 14),
            fg=self.secondary_color,
            bg="#313244",
            width=18,
            height=2,
            cursor='hand2'
        )
        btn_quitter.pack(pady=10)
        btn_quitter.bind('<Button-1>', lambda e: self.root.destroy())
        btn_quitter.bind('<Enter>', lambda e: btn_quitter.config(bg="#3d3d52"))
        btn_quitter.bind('<Leave>', lambda e: btn_quitter.config(bg="#313244"))
        
        # Crédits en bas de l'écran
        credits = Label(
            self.root, 
            text="© 2026 M.E.E. Tous droits réservés.", 
            font=("Segoe UI", 11),
            fg="#6c7086",
            bg=self.bg_color
        )
        credits.pack(side='bottom', pady=30)
        
    def lancer_jeu(self):
        """Lance le jeu principal (Monde 1)"""
        self.root.destroy()
        python_path = sys.executable
        script_path = os.path.join(os.path.dirname(__file__), "Maria_Peigne_monde_1.py")
        subprocess.Popen([python_path, script_path])
        
    def ouvrir_menu_admin(self):
        """Ouvre le menu admin pour visualiser les niveaux"""
        admin_window = Toplevel(self.root)
        admin_window.title("Paramètres")
        admin_window.configure(bg=self.bg_color)
        admin_window.attributes('-fullscreen', True)
        admin_window.bind('<Escape>', lambda e: admin_window.destroy())
        
        # Container centré
        container = Frame(admin_window, bg=self.bg_color)
        container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Titre
        titre = Label(
            container, 
            text="Mode Développeur", 
            font=("Segoe UI", 24, "bold"),
            fg=self.text_color,
            bg=self.bg_color
        )
        titre.pack(pady=(30, 10))
        
        # Description
        desc = Label(
            container, 
            text="Visualisez les niveaux en version réduite", 
            font=("Segoe UI", 12),
            fg=self.secondary_color,
            bg=self.bg_color
        )
        desc.pack(pady=(0, 30))
        
        # Frame pour les boutons
        frame = Frame(container, bg=self.bg_color)
        frame.pack(pady=10)
        
        # Liste des boutons admin
        boutons = [
            ("Visualiseur Matrice", "visualiseur_matrice.py"),
            ("Monde 1 Mini (Désert)", "Maria_Peigne_monde_1_mini.py"),
            ("Monde 2 Mini (Mausolée)", "Maria_Peigne_monde_2_mini.py"),
        ]
        
        for texte, fichier in boutons:
            btn = Label(
                frame,
                text=texte,
                font=("Segoe UI", 13),
                fg=self.text_color,
                bg=self.btn_color,
                width=25,
                height=2,
                cursor='hand2'
            )
            btn.pack(pady=8)
            btn.bind('<Button-1>', lambda e, f=fichier: self.lancer_outil(f))
            btn.bind('<Enter>', lambda e, b=btn: b.config(bg=self.btn_hover))
            btn.bind('<Leave>', lambda e, b=btn: b.config(bg=self.btn_color))
        
        # Bouton Retour
        btn_retour = Label(
            frame,
            text="Retour",
            font=("Segoe UI", 13),
            fg=self.secondary_color,
            bg="#313244",
            width=25,
            height=2,
            cursor='hand2'
        )
        btn_retour.pack(pady=25)
        btn_retour.bind('<Button-1>', lambda e: admin_window.destroy())
        btn_retour.bind('<Enter>', lambda e: btn_retour.config(bg="#3d3d52"))
        btn_retour.bind('<Leave>', lambda e: btn_retour.config(bg="#313244"))
        
    def lancer_outil(self, nom_fichier):
        """Lance un outil admin dans une nouvelle fenêtre"""
        python_path = sys.executable
        script_path = os.path.join(os.path.dirname(__file__), nom_fichier)
        subprocess.Popen([python_path, script_path])
        
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.run()
