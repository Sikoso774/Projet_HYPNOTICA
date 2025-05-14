# Démarrage du jeu

import pygame

pygame.init()
pygame.mixer.init()

def ecran_demmarage(images, duree_affichage=3000):
    """
    Affiche une séquence d'images avec un fondu enchaîné et des textes associés.

    Args:
        images (list): Liste des chemins des images à afficher.
        duree_affichage (int): Durée d'affichage de chaque image en millisecondes.
    """
    # Redimensionnement de l'écran
    blanc = (255, 255, 255)
    noir = (0, 0, 0)
    largeur = 800
    hauteur = 600
    ecran = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("HYPNOTICA")

    # Chargement de la musique:
    pygame.mixer.music.load("assets/musics/Max Brhon - AI [NCS Release].mp3")
    pygame.mixer.music.play(-1)

    # Police pour les textes
    police_nom = pygame.font.Font("assets/fonts/MINDCONTROL.ttf", 36)
    police_ENSEA = pygame.font.Font("assets/fonts/MINDCONTROL.ttf", 36)

    texte_nom = police_nom.render("Zoléni KOKOLO ZASSI", True, blanc)
    texte_nom_rect = texte_nom.get_rect(topleft=(0,0))

    texte_ENSEA = police_ENSEA.render("Projet HYPNOTICA", True, blanc)
    texte_ENSEA_rect = texte_ENSEA.get_rect(center=(largeur // 1.5, hauteur // 1.5 + 100))

    for image_path in images:
        # Vérification des dimensions de l'image
        image = pygame.image.load(image_path)
        if image.get_width() == 1561 and image.get_height() == 438:
            image = pygame.transform.scale(image, (largeur / 1.5, hauteur // 3))
            image_rect = image.get_rect(center=(largeur // 2, hauteur // 2))
        else:
            image = pygame.transform.scale(image, (largeur // 2, hauteur // 2))
            image_rect = image.get_rect(center=(largeur // 2, hauteur // 2))

        # Temps de début de l'affichage
        temps_debut = pygame.time.get_ticks()

        # Variables pour l'alpha (transparence)
        alpha_image = 0
        alpha_texte_nom = 0
        alpha_texte_ENSEA = 0
        alpha_vitesse = 255 / 1000  # Vitesse de changement de l'alpha

        while pygame.time.get_ticks() - temps_debut < duree_affichage:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            ecran.fill(noir)  # Fond noir

            # Calcul de l'alpha
            temps_ecoule = pygame.time.get_ticks() - temps_debut
            if temps_ecoule < duree_affichage / 3:
                alpha_image = int(temps_ecoule * alpha_vitesse)
            elif temps_ecoule < 2 * duree_affichage / 3:
                alpha_image = 255
                alpha_texte_nom = int((temps_ecoule - duree_affichage / 3) * alpha_vitesse)
            else:
                alpha_image = 255
                alpha_texte_nom = 255
                alpha_texte_ENSEA = int((temps_ecoule - 2 * duree_affichage / 3) * alpha_vitesse)

            # Application de l'alpha à l'image et au texte
            image.set_alpha(alpha_image)
            texte_nom.set_alpha(alpha_texte_nom)
            texte_ENSEA.set_alpha(alpha_texte_ENSEA)

            # Affichage de l'image et du texte
            ecran.blit(image, image_rect)
            ecran.blit(texte_nom, texte_nom_rect)
            ecran.blit(texte_ENSEA, texte_ENSEA_rect)

            pygame.display.flip()
            pygame.time.delay(10)


# Test de la function
if __name__ == "__main__":
    ecran_demmarage(["assets/images/Zoléni_Cyberpunk.jpg",
                  "assets/images/Logo_ENSEA.jpg","assets/images/pygame_logo.png"])