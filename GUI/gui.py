import tkinter as tk

class GUI:
    """
    Classe représentant l'interface graphique principale de l'application.
    Gère les frames des différents problèmes et la navigation entre eux.
    """

    def __init__(self):
        """
        Initialise l'interface graphique.

        Attributs :
            root (tk.Tk) : Fenêtre principale de l'application.
            frames (dict) : Dictionnaire associant les frames aux problèmes.
            current_frame (tk.Frame) : Frame actuellement affichée.
            problems (list) : Liste des problèmes ajoutés à l'application.
            current_problem : Problème actuellement affiché.
        """
        self.root = tk.Tk()
        self.root.title("Jeu d'Énigmes")
        self.frames = {}  # Dictionnaire pour stocker les frames des problèmes
        self.current_frame = None
        self.problems = []
        self.current_problem = None

    def add_problem(self, problem):
        """
        Ajoute un problème à l'application et crée son frame.

        Args :
            problem : Instance du problème à ajouter.
        """
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True)
        frame.pack_forget()  # Masque le frame au départ
        self.frames[id(problem)] = frame  # Utiliser l'ID unique de l'objet comme clé
        problem.create_gui(frame)

    def show_problem(self, problem):
        """
        Affiche le frame correspondant au problème donné.

        Args :
            problem : Instance du problème à afficher.
        """
        if self.current_frame:
            self.current_frame.pack_forget()  # Masque le frame actuel
        self.current_frame = self.frames[id(problem)]  # Utiliser l'ID unique
        self.current_frame.pack(fill="both", expand=True)

    def next_problem(self):
        """
        Passe au problème suivant dans la liste ou termine l'application
        si tous les problèmes ont été résolus.
        """
        current_index = self.problems.index(self.current_problem)
        if current_index + 1 < len(self.problems):
            self.current_problem = self.problems[current_index + 1]
            self.show_problem(self.current_problem)
        else:
            self.root.destroy()  # Ferme la fenêtre principale

    def run(self):
        """
        Démarre l'application en affichant le premier problème
        et en lançant la boucle principale de Tkinter.
        """
        if self.problems:
            self.current_problem = self.problems[0]
            self.show_problem(self.current_problem)
        self.root.mainloop()