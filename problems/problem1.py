import tkinter as tk
from tkinter import Scale
from PIL import Image, ImageTk, ImageEnhance
from problems.base_problem import BaseProblem

class Problem1(BaseProblem):
    """
    Classe représentant le problème 1, où l'utilisateur doit ajuster la luminosité
    d'une image et entrer un code secret pour résoudre le problème.
    """

    def __init__(self, gui, image_path="./assets/images/hidden_code.png", secret_code="0022"):
        """
        Initialise une instance de Problem1.

        Args:
            gui: Instance de l'interface graphique principale (GUI) pour gérer les interactions.
            image_path (str): Chemin vers l'image utilisée dans le problème. Par défaut, "./assets/images/hidden_code.png".
            secret_code (str): Code secret à entrer pour résoudre le problème. Par défaut, "0022".
        """
        super().__init__(image_path)
        self.secret_code = secret_code  # Code secret requis pour résoudre le problème
        self.gui = gui  # Référence à l'interface graphique principale
        self.current_brightness = 1.0  # Luminosité par défaut
        self.image = Image.open(image_path)  # Charge l'image spécifiée
        self.tk_image = None  # Image convertie pour l'affichage dans Tkinter

    def create_gui(self, parent):
        """
        Crée l'interface graphique spécifique au problème.

        Args:
            parent: Widget parent dans lequel l'interface sera créée.
        """
        # Afficher l'image
        self.update_image()
        self.image_label = tk.Label(parent, image=self.tk_image)  # Stocker le label dans un attribut
        self.image_label.image = self.tk_image
        self.image_label.pack(pady=10)

        # Slider pour ajuster la luminosité
        brightness_label = tk.Label(parent, text="Ajustez la luminosité :", font=("Arial", 12))
        brightness_label.pack()
        brightness_slider = Scale(parent, from_=0.5, to=5.0, resolution=0.1, orient="horizontal", command=self.adjust_brightness)
        brightness_slider.set(self.current_brightness)
        brightness_slider.pack(pady=10)

        # Zone pour entrer le code
        code_label = tk.Label(parent, text="Entrez le code :", font=("Arial", 12))
        code_label.pack()
        self.code_entry = tk.Entry(parent, font=("Arial", 12))
        self.code_entry.pack(pady=10)

        # Bouton de validation
        validate_button = tk.Button(parent, text="Valider", font=("Arial", 12), command=self.validate_code)
        validate_button.pack(pady=10)

    def adjust_brightness(self, value):
        """
        Ajuste la luminosité de l'image et met à jour l'affichage.

        Args:
            value (float): Nouvelle valeur de luminosité.
        """
        self.current_brightness = float(value)
        enhancer = ImageEnhance.Brightness(self.image)
        brightened_image = enhancer.enhance(self.current_brightness)
        self.tk_image = ImageTk.PhotoImage(brightened_image)

        # Met à jour l'image affichée dans le label
        self.image_label.configure(image=self.tk_image)
        self.image_label.image = self.tk_image

    def update_image(self):
        """
        Met à jour l'image pour l'affichage en appliquant la luminosité actuelle.
        """
        enhancer = ImageEnhance.Brightness(self.image)
        brightened_image = enhancer.enhance(self.current_brightness)
        self.tk_image = ImageTk.PhotoImage(brightened_image)

    def perform_action(self, action=None):
        """
        Effectue une action (vérification du code).

        Args:
            action: Action à effectuer (non utilisé dans cette implémentation).
        """
        entered_code = self.code_entry.get()
        if entered_code == self.secret_code:
            self.is_solved = True

    def validate_code(self):
        """
        Valide le code entré par l'utilisateur. Si le code est correct, passe au problème suivant.
        Sinon, affiche un message d'erreur.
        """
        self.perform_action()
        if self.is_solved:
            self.gui.next_problem()
        else:
            tk.messagebox.showwarning("Erreur", "Code incorrect. Essayez encore.")