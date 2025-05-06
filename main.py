from GUI.gui import GUI
from problems.problem1 import Problem1
from problems.problem2 import Problem2
from problems.histoire import Histoire

if __name__ == '__main__':
    """
    Point d'entrée principal de l'application. Initialise l'interface graphique (GUI),
    configure les différentes étapes du scénario (histoires et problèmes) et lance l'application.
    """

    # Créer une instance de la classe GUI
    gui = GUI()

    # Ajouter les différentes étapes du scénario
    intro = Histoire(
        gui=gui,
        texte="""Vous vous réveillez dans une pièce sombre, sans souvenir de comment vous y êtes arrivé.\n\n"""
    )
    histoire1 = Histoire(
        gui=gui,
        texte="""En tâtonnant, vous découvrez un coffre avec un code à 4 chiffres.\n\nDerrière vous, un écran s'allume, avec quelques boutons en dessous.\n\n"""
    )
    problem1 = Problem1(gui=gui)
    histoire2 = Histoire(
        gui=gui,
        texte="""Le coffre s'ouvre et vous trouvez une clé carrée. Sur l'écran, vous voyez une nouvelle image apparaître.\n\n"""
    )
    problem2 = Problem2(gui=gui)
    histoire3 = Histoire(
        gui=gui,
        texte="""L'écran laisse place à une serrure. Après quelques essais, vous parvenez finalement à ouvrir la porte !\n\n"""
    )
    fin = Histoire(
        gui=gui,
        texte="""Vous sortez de la pièce, content d'avoir résolu l'énigme.\n\n"""
    )

    # Ajouter les problèmes et histoires à la liste
    gui.problems = [intro, histoire1, problem1, histoire2, problem2, histoire3, fin]

    # Associer chaque problème ou histoire à un frame dans l'interface graphique
    for problem in gui.problems:
        gui.add_problem(problem)

    # Lancer l'application
    gui.run()

