import pygame
import os

pygame.init()

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
gris = (96,96,96)
rouge = (255, 0, 0)
vert = (0, 255, 0)
bleu = (0,0,255)
violet = (127,0,255)

# Taille de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("HYPNOTICA")

# Police de caractères
police = pygame.font.Font("assets/fonts/MINDCONTROL.ttf",size=35)

# Fonction pour afficher du texte centré
def afficher_texte_centre(texte, couleur, y):
    texte_surface = police.render(texte, True, couleur)
    texte_rect = texte_surface.get_rect(center=(largeur // 2, y))
    ecran.blit(texte_surface, texte_rect)



# Écran-titre
def ecran_titre():
    # Chargement des images du GIF
    gif_images = []
    image_folder = "images_gif"
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (largeur, hauteur))
            gif_images.append(image)

    animation_frame = 0
    animation_speed = 60

    # Chargement et lecture de la musique
    pygame.mixer.music.load("assets/musics/Max Brhon - AI [NCS Release].mp3")
    pygame.mixer.music.play(-1)

    # Bouton de démarrage (ellipse)
    bouton_largeur = 400
    bouton_hauteur = 100
    bouton_x = largeur // 2 - bouton_largeur // 2
    bouton_y = hauteur // 3.0 + 50
    bouton_rect = pygame.Rect(bouton_x, bouton_y, bouton_largeur, bouton_hauteur)

    # Bouton des crédits (ellipse)
    credit_largeur = 400
    credit_hauteur = 100
    credit_x = largeur // 2 - credit_largeur // 2
    credit_y = hauteur // 2.01 + 50
    credit_rect = pygame.Rect(credit_x, credit_y, credit_largeur, credit_hauteur)

    # Bouton des instructions (ellipse)
    instruction_largeur = 400
    instruction_hauteur = 100
    instruction_x = largeur // 2 - instruction_largeur // 2
    instruction_y = hauteur // 1.514 + 50
    instruction_rect = pygame.Rect(instruction_x, instruction_y, instruction_largeur, instruction_hauteur)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_rect.collidepoint(event.pos):
                    return "démarrer"
                if credit_rect.collidepoint(event.pos):
                    return "crédits"
                if instruction_rect.collidepoint(event.pos):
                    return "instructions"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "démarrer"
                if event.key == pygame.K_c:
                    return "crédits"
                if event.key == pygame.K_i:
                    return "instructions"

        ecran.blit(gif_images[animation_frame], (0, 0))
        afficher_texte_centre("HYPNOTICA", blanc, hauteur // 4)
        afficher_texte_centre("Zoléni KOKOLO ZASSI - 2025", blanc, hauteur // 4 + 50)

        # Création des masques pour les ellipses
        masque_bouton = pygame.Surface((bouton_largeur, bouton_hauteur), pygame.SRCALPHA)
        pygame.draw.ellipse(masque_bouton, (0, 255, 13, 100), (0, 0, bouton_largeur, bouton_hauteur))

        masque_credit = pygame.Surface((credit_largeur, credit_hauteur), pygame.SRCALPHA)
        pygame.draw.ellipse(masque_credit, (245, 189, 31, 255), (0, 0, credit_largeur, credit_hauteur))

        masque_instruction = pygame.Surface((instruction_largeur, instruction_hauteur), pygame.SRCALPHA)
        pygame.draw.ellipse(masque_instruction, (255, 0, 0, 255), (0, 0, instruction_largeur, instruction_hauteur))

        # Utilisation des masques pour découper les textures
        texture_bouton = pygame.transform.scale(gif_images[animation_frame], (bouton_largeur, bouton_hauteur))
        texture_bouton.blit(masque_bouton, (0, 0),
                            special_flags=pygame.BLEND_RGBA_MULT)  # Utilisation de BLEND_RGBA_MULT
        texture_bouton_rect = texture_bouton.get_rect(center=bouton_rect.center)
        ecran.blit(texture_bouton, texture_bouton_rect)

        texture_credit = pygame.transform.scale(gif_images[animation_frame], (credit_largeur, credit_hauteur))
        texture_credit.blit(masque_credit, (0, 0),
                            special_flags=pygame.BLEND_RGBA_MULT)  # Utilisation de BLEND_RGBA_MULT
        texture_credit_rect = texture_credit.get_rect(center=credit_rect.center)
        ecran.blit(texture_credit, texture_credit_rect)

        texture_instruction = pygame.transform.scale(gif_images[animation_frame],
                                                     (instruction_largeur, instruction_hauteur))
        texture_instruction.blit(masque_instruction, (0, 0),
                                 special_flags=pygame.BLEND_RGBA_MULT)  # Utilisation de BLEND_RGBA_MULT
        texture_instruction_rect = texture_instruction.get_rect(center=instruction_rect.center)
        ecran.blit(texture_instruction, texture_instruction_rect)

        # Dessin des bordures des ellipses
        pygame.draw.ellipse(ecran, (0, 0, 0, 0), bouton_rect, 1)
        pygame.draw.ellipse(ecran, (0, 0, 0, 0), credit_rect, 1)
        pygame.draw.ellipse(ecran, (0, 0, 0, 0), instruction_rect, 1)

        afficher_texte_centre("Start - SPACE", blanc, bouton_y + bouton_hauteur // 2)
        afficher_texte_centre("Credits - C", blanc, credit_y + credit_hauteur // 2)
        afficher_texte_centre("Instructions - I", blanc, instruction_y + instruction_hauteur // 2)

        pygame.display.flip()

        animation_frame += 1
        if animation_frame >= len(gif_images):
            animation_frame = 0
        pygame.time.delay(1000 // animation_speed)

if __name__ == "__main__": # ----> Fonction magique permettent de vérifier si le programme fonctionne
    ecran_titre()