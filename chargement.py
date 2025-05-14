# Animation de transition


# Importation des bibliothèques
import pygame
import math
import os

# Initialisation de Pygame
pygame.init()

# Taille de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("HYPNOTICA")

gif_images = []
image_folder = "images_gif"
for filename in sorted(os.listdir(image_folder)):
    if filename.endswith(".png"):
        image_path = os.path.join(image_folder, filename)
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (largeur, hauteur))
        gif_images.append(image)

# Charger l'image pygame_logo.png
image_fin = pygame.image.load("assets/images/pygame_logo.png")

# Transition
def loading(image_fin, gif_images, duree_transition=2000):
    """
    Effectue une transition en spirale entre une image et un GIF.

    Args:
        image_fin (pygame.Surface): La dernière image de la présentation.
        gif_images (list): Liste des images du GIF Hypnose.
        duree_transition (int): Durée de la transition en millisecondes.
    """

    temps_debut = pygame.time.get_ticks()
    centre_x, centre_y = largeur // 2, hauteur // 2
    rayon_max = min(largeur, hauteur) // 2

    while pygame.time.get_ticks() - temps_debut < duree_transition:
        temps_ecoule = pygame.time.get_ticks() - temps_debut
        pourcentage = temps_ecoule / duree_transition
        angle = pourcentage * 10 * math.pi  # Ajustez pour la vitesse de rotation
        rayon = rayon_max * pourcentage

        # Calcul des coordonnées de la spirale
        x = centre_x + rayon * math.cos(angle)
        y = centre_y + rayon * math.sin(angle)

        # Redimensionnement et rotation de l'image
        taille = int((1 - pourcentage) * min(largeur, hauteur))
        if taille > 0:
            image_transformee = pygame.transform.scale(image_fin, (taille, taille))
            image_transformee = pygame.transform.rotate(image_transformee, angle * 180 / math.pi)
            rect_transforme = image_transformee.get_rect(center=(x, y))
            ecran.blit(image_transformee, rect_transforme)

        # Affichage du GIF Hypnose en arrière-plan
        frame = int(pourcentage * len(gif_images)) % len(gif_images)
        ecran.blit(gif_images[frame], (0, 0))

        pygame.display.flip()
        pygame.time.delay(10)


if __name__ == "__main__":
    loading(image_fin,gif_images=gif_images) # ----> Test de la function