# Projet d'Évasion - Jeu d'Énigmes Interactif

Ce projet est une application Python interactive basée sur une interface graphique utilisant `tkinter`. Le but est de résoudre une série d'énigmes pour progresser dans une histoire immersive.

## Fonctionnalités

- **Interface graphique** : Utilisation de `tkinter` pour une expérience utilisateur interactive.
- **Gestion des problèmes** : Chaque étape du jeu est un problème ou une partie de l'histoire.
- **Filtres d'image** : Manipulation d'images avec `Pillow` pour résoudre certaines énigmes.
- **Progression scénarisée** : Une histoire immersive avec des étapes successives.

## Structure du Projet

- `main.py` : Point d'entrée principal de l'application.
- `GUI/gui.py` : Gestion de l'interface graphique principale.
- `problems/` : Contient les différents problèmes et étapes du jeu.
  - `base_problem.py` : Classe de base pour les problèmes.
  - `problem1.py`, `problem2.py` : Problèmes spécifiques.
  - `histoire.py` : Étapes narratives de l'histoire.
- `assets/` : Contient les ressources comme les images utilisées dans le jeu.

## Prérequis

- Python 3.8 ou supérieur
- Bibliothèques Python :
  - `tkinter` (inclus avec Python)
  - `Pillow`

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/PitHagore23/Computer_Vision_Escape_Game.git
   cd Computer_Vision_Escape_Game
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez le jeu avec la commande suivante :
   ```bash
   python main.py
   ```

2. Suivez les instructions à l'écran pour résoudre les énigmes et progresser dans l'histoire.

## Développement

### Ajouter un nouveau problème

1. Créez un nouveau fichier dans le dossier `problems/` en héritant de `BaseProblem`.
2. Implémentez la méthode `create_gui` pour définir l'interface graphique spécifique au problème.
3. Ajoutez le nouveau problème dans la liste `gui.problems` dans `main.py`.

### Exemple de problème

Voici un exemple de structure pour un nouveau problème :
```python
from problems.base_problem import BaseProblem

class NouveauProbleme(BaseProblem):
    def create_gui(self, parent):
        # Implémentez l'interface graphique ici
        pass
```

