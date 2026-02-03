# 🎮 Maria Peigne - Jeu 2D

Un jeu d'aventure en 2D où vous incarnez **Maria**, une exploratrice qui doit collecter trois clés pour accéder au portail et progresser vers le monde suivant.

## 📋 Description

Maria Peigne est un dungeon crawler minimaliste développé en **Python** avec **Tkinter** pour l'interface graphique et **Pygame** pour la gestion audio.

### Gameplay
- 🕹️ Contrôlez Maria à travers deux mondes distincts
- 🔑 Récupérez les 3 clés cachées dans chaque niveau
- 🚪 Ouvrez le portail une fois toutes les clés collectées
- 🌍 Progressez vers le monde suivant

## 🎯 Contrôles

| Touche | Action |
|--------|--------|
| **Z** | Avancer (haut) |
| **S** | Reculer (bas) |
| **Q** | Gauche |
| **D** | Droite |
| **A** | Passer le portail (si 3 clés obtenues) |
| **Échap** | Quitter le jeu |

## 🌍 Mondes

### Monde 1 - Désert
- **Textures** : Sable, murs en brique, cactus, lierre
- **Clés** : Rubis 💎, Émeraude 💚, Saphir 💙
- Ambiance : vent du désert

### Monde 2 - Mausolée Souterrain
- **Textures** : Pierre, sol gris, cristaux de couleur
- **Clés** : Cristal violet, Cristal bleu, Cristal vert
- Ambiance : cavernes souterraines

## 📁 Structure du projet

```
MariaPeigne/
├── Maria_Peigne_monde_1.py     # Niveau 1 - Point d'entrée du jeu
├── Maria_Peigne_monde_2.py     # Niveau 2 (fonction lancer_monde())
├── README.md
├── .gitignore
│
├── Textures/                   # Assets graphiques (PNG)
│   ├── Maria.png               # Sprite personnage (droite)
│   ├── Maria2.png              # Sprite personnage (gauche)
│   ├── monde1.png              # Fond monde 1
│   ├── moul.png                # Fond monde 2
│   ├── mur_brique_m1.png       # Mur monde 1
│   ├── mur_pierre_m2.png       # Mur monde 2
│   ├── sable_m1.png            # Sol monde 1
│   ├── sol_m2.png              # Sol monde 2
│   ├── Clé_*.png               # Clés monde 1 (rubis, emeraude, saphir)
│   ├── cristal_*.png           # Cristaux monde 2 (violet, bleu, vert)
│   ├── Cactus_*.png            # Obstacles monde 1
│   ├── lierre_m1.png           # Décoration monde 1
│   ├── portail_*.png           # Portails (fermé/ouvert, m1/m2)
│   └── ...
│
├── Sons/                       # Assets audio (MP3)
│   ├── vent_m1.mp3             # Ambiance monde 1
│   ├── pas1_m1.mp3             # Sons de pas (3 variantes)
│   ├── pas2_m1.mp3
│   ├── pas3_m1.mp3
│   ├── clef1_m1.mp3            # Sons collecte clé (3 variantes)
│   ├── clef2_m1.mp3
│   ├── clef3_m1.mp3
│   └── ouverture_portail_m1.mp3
│
└── Autres/                     # Fichiers additionnels
    ├── Cahier des charges.docx
    └── Maria_Peigne_monde_1_sans_son.py
```

## 🔧 Installation

### Prérequis
- Python 3.x
- Tkinter (inclus avec Python)
- Pygame

### Installation des dépendances

```bash
pip install pygame
```

## ▶️ Démarrage

Lancez le monde 1 :

```bash
python menu.py
```

Le monde 2 se lance automatiquement quand vous passez le portail du monde 1.

## 🎨 Système de Collision

La collision est gérée par une **matrice 20×30** où chaque nombre représente un élément :

| Code | Élément |
|------|---------|
| 1 | Mur (bloque le passage) |
| 0 | Sol vide (accessible) |
| 5 | Sol (zone d'affichage) |
| -2 | Clé 1 |
| -3 | Clé 2 |
| -4 | Clé 3 |
| -5 | Portail (ferme) |
| -6 / 11 | Portail (ouvert) |
| -7 | Cactus bas / Obstacle |
| -8 | Point d'entrée/sortie portail |
| -9 | Cactus haut / Obstacle |
| -10 | Lierre / Décoration |

## 🎵 Audio

- **Canaux Pygame** :
  - Canal 0 : Sons de pas (3 variantes)
  - Canal 1 : Ouverture du portail
  - Canal 2 : Collecte de clés (3 variantes)
  - Canal 3 : Ambiance (vent)

## 👥 Crédits

Jeu réalisé par **Mélène, Eva et Ethan**

## 🚀 Améliorations futures possibles

- [ ] Menu principal
- [ ] Système de sauvegarde
- [ ] Plus de niveaux
- [ ] Ennemis/IA
- [ ] Animations améliorées
- [ ] Effets de particules
- [ ] Musique de fond

---

**Amusez-vous bien dans les mondes de Maria Peigne ! 🎮**
