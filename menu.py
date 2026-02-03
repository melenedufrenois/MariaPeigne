# Menu Principal - Maria Peigne
# Lance le jeu ou accède au mode admin (visualisation des niveaux)

from tkinter import *
import subprocess
import sys
import os

class BoutonArrondi(Canvas):
    """Bouton avec coins arrondis"""
    def __init__(self, parent, text, command, width=220, height=50, radius=25, 
                 bg_color="#45475a", hover_color="#585b70", text_color="#cdd6f4",
                 font=("Segoe UI", 14, "bold"), **kwargs):
        super().__init__(parent, width=width, height=height, 
                        bg=parent.cget('bg'), highlightthickness=0, **kwargs)
        
        self.command = command
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.radius = radius
        self.btn_width = width
        self.btn_height = height
        self.text = text
        self.font = font
        
        self.dessiner(bg_color)
        
        # Events
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Button-1>', self.on_click)
        self.config(cursor='hand2')
        
    def dessiner(self, color):
        """Dessine le bouton arrondi"""
        self.delete('all')
        r = self.radius
        w = self.btn_width
        h = self.btn_height
        
        # Rectangle arrondi (avec des arcs aux coins)
        self.create_arc(0, 0, r*2, r*2, start=90, extent=90, fill=color, outline=color)
        self.create_arc(w-r*2, 0, w, r*2, start=0, extent=90, fill=color, outline=color)
        self.create_arc(0, h-r*2, r*2, h, start=180, extent=90, fill=color, outline=color)
        self.create_arc(w-r*2, h-r*2, w, h, start=270, extent=90, fill=color, outline=color)
        
        # Rectangles pour remplir le centre
        self.create_rectangle(r, 0, w-r, h, fill=color, outline=color)
        self.create_rectangle(0, r, w, h-r, fill=color, outline=color)
        
        # Texte centré
        self.create_text(w/2, h/2, text=self.text, fill=self.text_color, font=self.font)
        
    def on_enter(self, event):
        self.dessiner(self.hover_color)
        
    def on_leave(self, event):
        self.dessiner(self.bg_color)
        
    def on_click(self, event):
        if self.command:
            self.command()


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
        
        # Bouton Jouer (accent)
        btn_jouer = BoutonArrondi(
            frame_boutons,
            text="Jouer",
            command=self.lancer_jeu,
            width=220, height=50, radius=25,
            bg_color=self.accent_color,
            hover_color="#7ba3e8",
            text_color="#1e1e2e",
            font=("Segoe UI", 16, "bold")
        )
        btn_jouer.pack(pady=10)
        
        # Crédits en bas de l'écran
        credits = Label(
            self.root, 
            text="© 2026 M.E.E. Tous droits réservés.", 
            font=("Segoe UI", 11),
            fg="#6c7086",
            bg=self.bg_color
        )
        credits.pack(side='bottom', pady=30)
        
        # Frame pour les boutons icônes - juste au-dessus des crédits
        frame_icones = Frame(self.root, bg=self.bg_color)
        frame_icones.pack(side='bottom', pady=10)
        
        # Bouton Quitter (porte avec flèche)
        btn_quitter = BoutonArrondi(
            frame_icones,
            text="🚪",
            command=self.root.destroy,
            width=60, height=60, radius=30,
            bg_color="#313244",
            hover_color="#3d3d52",
            text_color=self.secondary_color,
            font=("Segoe UI", 24)
        )
        btn_quitter.pack(side='left', padx=15)

        # Bouton Paramètres (engrenage)
        btn_admin = BoutonArrondi(
            frame_icones,
            text="⚙",
            command=self.ouvrir_menu_admin,
            width=60, height=60, radius=30,
            bg_color=self.btn_color,
            hover_color=self.btn_hover,
            text_color=self.text_color,
            font=("Segoe UI", 24)
        )
        btn_admin.pack(side='left', padx=15)
        
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
            btn = BoutonArrondi(
                frame,
                text=texte,
                command=lambda f=fichier: self.lancer_outil(f),
                width=280, height=45, radius=22,
                bg_color=self.btn_color,
                hover_color=self.btn_hover,
                text_color=self.text_color,
                font=("Segoe UI", 13)
            )
            btn.pack(pady=8)
        
        # Bouton Retour
        btn_retour = BoutonArrondi(
            frame,
            text="Retour",
            command=admin_window.destroy,
            width=280, height=45, radius=22,
            bg_color="#313244",
            hover_color="#3d3d52",
            text_color=self.secondary_color,
            font=("Segoe UI", 13)
        )
        btn_retour.pack(pady=25)
        
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
