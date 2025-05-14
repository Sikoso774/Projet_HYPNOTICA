import pygame
import os
import random

pygame.init()  # ----> Test de la fonction

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
gris = (96,96,96)
rouge = (255, 0, 0)
vert = (0, 255, 0)

# Dimensions de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("HYPNOTICA")

# Police
police = pygame.font.Font("assets/fonts/MINDCONTROL.ttf",size=35)

# Boucle principale du jeu
def boucle_jeu_HYPNOTICA():
    joueur_taille = 50
    joueur_x = largeur // 2 - joueur_taille // 2
    joueur_y = hauteur - joueur_taille - 20
    joueur_vitesse = 5

    telephone_taille = 30
    telephone_x = random.randint(0, largeur - telephone_taille)
    telephone_y = 0
    telephone_vitesse = 3

    satiete = 100
    satiete_diminution = 0.1
    satiete_augmentation = 10

    clock = pygame.time.Clock()

        # Chargement des images du GIF ("images_gif")
    gif_images = []
    image_folder = "images_gif" # Le fichier des frames d'images
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (largeur, hauteur))
            gif_images.append(image)

    animation_frame = 0
    animation_speed = 60  # Vitesse de l'animation

    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False

        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and joueur_x > 0:
            joueur_x -= joueur_vitesse
        if touches[pygame.K_RIGHT] and joueur_x < largeur - joueur_taille:
            joueur_x += joueur_vitesse

        telephone_y += telephone_vitesse
        if telephone_y > hauteur:
            telephone_x = random.randint(0, largeur - telephone_taille)
            telephone_y = 0

        joueur_rect = pygame.Rect(joueur_x, joueur_y, joueur_taille, joueur_taille)
        telephone_rect = pygame.Rect(telephone_x, telephone_y, telephone_taille, telephone_taille)
        if joueur_rect.colliderect(telephone_rect):
            satiete += satiete_augmentation
            telephone_x = random.randint(0, largeur - telephone_taille)
            telephone_y = 0

        satiete -= satiete_diminution
        if satiete < 0:
            return False  # Game Over

        ecran.blit(gif_images[animation_frame], (0, 0))
        pygame.draw.rect(ecran, blanc, (joueur_x, joueur_y, joueur_taille, joueur_taille))
        pygame.draw.rect(ecran, vert, (telephone_x, telephone_y, telephone_taille, telephone_taille))

        pygame.draw.rect(ecran, rouge, (10, 10, 200, 20))
        pygame.draw.rect(ecran, vert, (10, 10, satiete * 2, 20))

        texte_satiete = police.render(f"Satiété: {int(satiete)}", True, blanc)
        ecran.blit(texte_satiete, (10, 40))

        pygame.display.flip()
        clock.tick(60)

        # Mettre à jour l'image de l'animation
        animation_frame += 1
        if animation_frame >= len(gif_images):
            animation_frame = 0
        pygame.time.delay(1000 // animation_speed) #Delai pour la vitesse de l'animation.

    return True  # Jeu quitté normalement


# Test de la fonction
if __name__ == "__main__":
    boucle_jeu_HYPNOTICA() #  ----> Le jeu fonctionne t-il ?
