import random
from PIL import Image

def generate_hidden_square_image(image_size, square_size, square_position, output_path):
    """
    Génère une image RGB avec un carré visible uniquement avec un filtre R + B.

    :param image_size: Taille de l'image (largeur, hauteur).
    :param square_size: Taille du carré (largeur, hauteur).
    :param square_position: Position du carré (x, y).
    :param output_path: Chemin pour sauvegarder l'image générée.
    """
    # Créer une image RGB avec un fond vert légèrement teinté
    image = Image.new("RGB", image_size, (0, 128, 0))
    pixels = image.load()

    # Ajouter du bruit global sur les canaux rouge et bleu
    for x in range(image_size[0]):
        for y in range(image_size[1]):
            red_noise = random.randint(0, 255)
            blue_noise = random.randint(0, 255)
            green_noise = random.randint(0, 5)
            pixels[x, y] = (red_noise, green_noise, blue_noise)

    # Dessiner un carré vert pur au centre
    for x in range(square_position[0], square_position[0] + square_size[0]):
        for y in range(square_position[1], square_position[1] + square_size[1]):
            if 0 <= x < image_size[0] and 0 <= y < image_size[1]:
                red_noise = random.randint(0, 255)
                blue_noise = random.randint(0, 255)
                green_noise = random.randint(10, 12)
                pixels[x, y] = (red_noise, green_noise, blue_noise)

    # Sauvegarder l'image
    image.save(output_path)
    print(f"Image générée et sauvegardée à : {output_path}")

# Paramètres de l'image
image_size = (500, 500)  # Taille de l'image (500x500 pixels)
square_size = (100, 100)  # Taille du carré (100x100 pixels)
square_position = (200, 200)  # Position du carré (x=200, y=200)
output_path = "../assets/images/hidden_square.png"  # Chemin de sortie

# Générer l'image
generate_hidden_square_image(image_size, square_size, square_position, output_path)