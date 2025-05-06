import numpy as np
import cv2

def generate_hidden_code_image(output_path="hidden_code.png"):
    """
    Génère une image contenant un code caché et la sauvegarde dans un fichier.

    Args:
        output_path (str): Chemin où l'image générée sera sauvegardée. Par défaut, "hidden_code.png".

    La fonction crée une image en niveaux de gris avec un texte (code) au centre.
    Le texte est légèrement plus clair que l'arrière-plan pour créer un effet de code caché.
    """
    # Dimensions de l'image
    width, height = 500, 500

    # Créer une image en niveaux de gris uniforme
    image = np.full((height, width), 0, dtype=np.uint8)  # Niveau de gris moyen

    # Définir les paramètres pour le texte
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    thickness = 5
    text = "0022"

    # Obtenir la taille du texte
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2

    # Ajouter le texte avec une légère différence de luminosité
    cv2.putText(image, text, (text_x, text_y), font, font_scale, 5, thickness)  # Légèrement plus clair

    # Sauvegarder l'image
    cv2.imwrite(output_path, image)
    print(f"Image générée et sauvegardée sous {output_path}")

# Générer l'image
generate_hidden_code_image()