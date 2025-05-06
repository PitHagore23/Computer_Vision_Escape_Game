class BaseProblem:
    """
    Classe de base pour représenter un problème générique.
    Cette classe sert de modèle pour les problèmes spécifiques et doit être étendue.
    """

    def __init__(self, image_path):
        """
        Initialise un problème avec une image et un état non résolu.

        Args:
            image_path (str): Chemin vers l'image associée au problème.
        """
        self.image_path = image_path  # Chemin de l'image associée au problème
        self.is_solved = False  # Indique si le problème est résolu

    def create_gui(self, parent):
        """
        Crée une interface graphique spécifique au problème.

        Args:
            parent: Widget parent (par exemple, une fenêtre ou un cadre).

        Raises:
            NotImplementedError: Cette méthode doit être implémentée dans les sous-classes.
        """
        raise NotImplementedError("Cette méthode doit être implémentée dans les sous-classes.")

    def perform_action(self, action):
        """
        Effectue une action spécifique pour résoudre le problème.

        Args:
            action: Action à effectuer.

        Raises:
            NotImplementedError: Cette méthode doit être implémentée dans les sous-classes.
        """
        raise NotImplementedError("Cette méthode doit être implémentée dans les sous-classes.")

    def check_completion(self):
        """
        Évalue si le problème est résolu.

        Returns:
            bool: True si le problème est résolu, sinon False.
        """
        return self.is_solved