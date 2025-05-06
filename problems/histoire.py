import tkinter as tk
from problems.base_problem import BaseProblem

class Histoire(BaseProblem):
    """
    Classe représentant une histoire ou une étape narrative dans l'application.
    Hérite de BaseProblem mais n'a pas d'image associée.
    """

    def __init__(self, gui, texte=""):
        """
        Initialise une instance de Histoire.

        Args:
            gui: Instance de l'interface graphique principale (GUI) pour gérer les interactions.
            texte (str): Texte narratif à afficher dans cette étape.
        """
        super().__init__(image_path=None)  # Pas d'image associée
        self.gui = gui  # Référence à l'interface graphique principale
        self.texte = texte  # Texte narratif de l'histoire

    def create_gui(self, parent):
        """
        Crée l'interface graphique pour afficher le texte narratif.

        Args:
            parent: Widget parent dans lequel l'interface sera créée.
        """
        # Afficher le texte
        texte_label = tk.Label(parent, text=self.texte, font=("Arial", 14), wraplength=500, justify="center")
        texte_label.pack(pady=20)

        # Bouton "Suivant"
        suivant_button = tk.Button(parent, text="Suivant", font=("Arial", 12), command=self.suivant)
        suivant_button.pack(pady=10)

    def suivant(self):
        """
        Passe à l'étape ou au problème suivant dans l'application.
        """
        self.gui.next_problem()