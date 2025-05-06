import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
from problems.base_problem import BaseProblem

class Problem2(BaseProblem):
    """
    Classe représentant le problème 2, où l'utilisateur peut manipuler les canaux de couleur
    et ajuster la luminosité d'une image pour remplir des conditions spécifiques.
    """

    def __init__(self, gui, image_path="./assets/images/hidden_square.png"):
        """
        Initialise une instance de Problem2.

        Args:
            gui: Instance de l'interface graphique principale (GUI) pour gérer les interactions.
            image_path (str): Chemin vers l'image utilisée dans le problème. Par défaut, "./assets/images/hidden_square.png".
        """
        super().__init__(image_path)
        self.gui = gui  # Référence à l'interface graphique principale.
        self.image = Image.open(image_path)  # Charge l'image spécifiée.
        self.filtered_image = self.image.copy()  # Copie de l'image pour appliquer des filtres.
        self.tk_image = None  # Image convertie pour l'affichage dans Tkinter.
        self.channel_states = {"red": True, "green": True, "blue": True}  # État des canaux de couleur (tous activés par défaut).
        self.current_brightness = 1.0  # Niveau de luminosité initial.
        self.next_button = None  # Bouton pour passer au problème suivant.

    def create_gui(self, parent):
        """
        Crée l'interface graphique spécifique au problème.

        Args:
            parent: Widget parent dans lequel l'interface sera créée.
        """
        # Initialiser l'image pour l'affichage
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(parent, image=self.tk_image)
        self.image_label.image = self.tk_image
        self.image_label.pack(pady=10)

        # Boutons pour activer/désactiver les canaux
        button_frame = tk.Frame(parent)
        button_frame.pack(pady=10)

        red_button = tk.Button(button_frame, text="Activer/Désactiver Rouge",
                               command=lambda: self.toggle_channel("red"))
        red_button.grid(row=0, column=0, padx=5)

        green_button = tk.Button(button_frame, text="Activer/Désactiver Vert",
                                 command=lambda: self.toggle_channel("green"))
        green_button.grid(row=0, column=1, padx=5)

        blue_button = tk.Button(button_frame, text="Activer/Désactiver Bleu",
                                command=lambda: self.toggle_channel("blue"))
        blue_button.grid(row=0, column=2, padx=5)

        # Slider pour ajuster la luminosité
        brightness_slider = tk.Scale(parent, from_=0.1, to=5.0, resolution=0.1, orient="horizontal", label="Luminosité",
                                     command=self.on_brightness_change)
        brightness_slider.set(self.current_brightness)
        brightness_slider.pack(pady=10)

        # Binding pour vérifier la complétion lors du relâchement du slider
        brightness_slider.bind("<ButtonRelease-1>", lambda event: self.check_completion())

    def toggle_channel(self, channel):
        """
        Bascule l'état d'un canal (actif/inactif) et met à jour l'image.

        Args:
            channel (str): Nom du canal à basculer ("red", "green" ou "blue").
        """
        self.channel_states[channel] = not self.channel_states[channel]  # Inverser l'état du canal
        self.apply_filters()

    def on_brightness_change(self, value):
        """
        Ajuste la luminosité sans vérifier la complétion.

        Args:
            value (float): Nouvelle valeur de luminosité.
        """
        self.current_brightness = float(value)
        self.apply_filters()

    def check_completion(self):
        """
        Vérifie les conditions de complétion lorsque le slider est relâché.
        Les conditions sont :
        - Les canaux rouge et bleu doivent être désactivés.
        - Le canal vert doit être activé.
        - La luminosité doit être supérieure à 1.5.
        """
        if not self.channel_states["red"] and not self.channel_states["blue"] and self.channel_states["green"] and self.current_brightness > 1.5:
            self.complete_problem()

    def apply_filters(self):
        """
        Applique les filtres en fonction des canaux actifs/inactifs et de la luminosité.
        Met à jour l'image affichée avec les modifications.
        """
        self.filtered_image = self.image.copy()
        pixels = self.filtered_image.load()

        for x in range(self.filtered_image.width):
            for y in range(self.filtered_image.height):
                r, g, b = pixels[x, y]
                r = r if self.channel_states["red"] else 0
                g = g if self.channel_states["green"] else 0
                b = b if self.channel_states["blue"] else 0
                pixels[x, y] = (r, g, b)

        # Appliquer la luminosité
        enhancer = ImageEnhance.Brightness(self.filtered_image)
        self.filtered_image = enhancer.enhance(self.current_brightness)

        self.update_image()

    def complete_problem(self):
        """
        Indique la complétion du problème et affiche un bouton "Suivant" pour passer au problème suivant.
        """
        print("Problème complété !")
        if not self.next_button:  # Crée le bouton uniquement s'il n'existe pas déjà
            self.next_button = tk.Button(self.image_label.master, text="Suivant", command=self.gui.next_problem)
            self.next_button.pack(pady=10)

    def update_image(self):
        """
        Met à jour l'image affichée dans l'interface graphique avec les filtres appliqués.
        """
        self.tk_image = ImageTk.PhotoImage(self.filtered_image)
        self.image_label.configure(image=self.tk_image)
        self.image_label.image = self.tk_image