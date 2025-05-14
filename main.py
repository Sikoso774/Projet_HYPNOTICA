# Zoléni KOKOLO ZASSI
# Date: 14/05/2025

# Mes bibliothèques
import pygame
import os



# Mes programmes
from demarrage_jeu import ecran_demmarage
from chargement    import loading
from ecran_titre   import ecran_titre
from instructions  import instructions_jeu
from gameplay      import boucle_jeu_HYPNOTICA
from game_over     import Game_Over
from credits_jeu   import Ecran_Credits

# Initialisation de Pygame
pygame.init()

# Initialisation du module de musique
pygame.mixer.init()

# Dimensions de écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("HYPNOTICA")


# Charger image pygame_logo.png
image_fin = pygame.image.load("assets/images/pygame_logo.png")

# Charger les images du GIF Hypnose
gif_images = []
image_folder = "images_gif"
for filename in sorted(os.listdir(image_folder)):
    if filename.endswith(".png"):
        image_path = os.path.join(image_folder, filename)
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (largeur, hauteur))
        gif_images.append(image)


# Boucle principale

ecran_demmarage(["assets/images/Zoléni_Cyberpunk.jpg", "assets/images/Logo_ENSEA.jpg",
              "assets/images/pygame_logo.png"])

loading(image_fin, gif_images=gif_images)

while True:
    choix = ecran_titre()
    if choix == "démarrer":

        game_result = boucle_jeu_HYPNOTICA()  # ----> Appelle la boucle de jeu

        if not game_result:                   # ----> Si le joueur a perdu (Game Over)
            choix_game_over = Game_Over()     # ----> Appelle l'écran Game Over
            if not choix_game_over == False:
                if choix_game_over == "crédits":
                    Ecran_Credits()
                else:
                    continue  # Relance le jeu

            else:
                break  # Quitte le jeu
        else:
            continue                         # Si le joueur a quitté normalement, retour à l'écran titre
    elif choix == "crédits":
        Ecran_Credits()
    elif choix == "instructions":
        instructions_jeu()
    else:
        break

pygame.quit()