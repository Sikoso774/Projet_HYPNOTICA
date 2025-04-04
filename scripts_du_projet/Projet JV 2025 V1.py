import pygame
import random

# Initialisation de Pygame
pygame.init()

# Initialisation du module de musique
pygame.mixer.init()

# Dimensions de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Les dangers de l'addiction.")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
vert = (0, 255, 0)

# Police de caractères
police = pygame.font.Font(None, 36)

# Fonction pour afficher du texte centré
def afficher_texte_centre(texte, couleur, y):
    texte_surface = police.render(texte, True, couleur)
    texte_rect = texte_surface.get_rect(center=(largeur // 2, y))
    ecran.blit(texte_surface, texte_rect)

# Écran-titre
def ecran_titre():
    arriere_plan = pygame.image.load("assets/images/danger.jpg")
    arriere_plan = pygame.transform.scale(arriere_plan, (largeur, hauteur))

    # Chargement et lecture de la musique
    pygame.mixer.music.load("assets/musics/DEAF KEV - Invincible [NCS Release].mp3") #Remplacer par le nom de votre fichier audio
    pygame.mixer.music.play(-1)  # Lecture en boucle

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

        ecran.blit(arriere_plan, (0, 0))
        afficher_texte_centre("Les dangers de l'addiction.", blanc, hauteur // 4)
        afficher_texte_centre("Appuyez sur ESPACE pour commencer", vert, hauteur // 2)
        pygame.display.flip()

# Boucle principale du jeu
def boucle_jeu():
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

    arriere_plan = pygame.image.load("assets/images/danger.jpg")
    arriere_plan = pygame.transform.scale(arriere_plan, (largeur, hauteur))

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

        ecran.blit(arriere_plan, (0, 0))
        pygame.draw.rect(ecran, blanc, (joueur_x, joueur_y, joueur_taille, joueur_taille))
        pygame.draw.rect(ecran, vert, (telephone_x, telephone_y, telephone_taille, telephone_taille))

        pygame.draw.rect(ecran, rouge, (10, 10, 200, 20))
        pygame.draw.rect(ecran, vert, (10, 10, satiete * 2, 20))

        texte_satiete = police.render(f"Satiété: {int(satiete)}", True, blanc)
        ecran.blit(texte_satiete, (10, 40))

        pygame.display.flip()
        clock.tick(60)

    return True  # Jeu quitté normalement

# Écran Game Over
def ecran_game_over():
    # Arrêt de la musique
    pygame.mixer.music.stop()

    arriere_plan_game_over = pygame.image.load("Game_Over.jpg")
    arriere_plan_game_over = pygame.transform.scale(arriere_plan_game_over, (largeur, hauteur))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Relancer le jeu
                elif event.key == pygame.K_q:
                    return False  # Quitter le jeu

        ecran.blit(arriere_plan_game_over, (0, 0))

        afficher_texte_centre("Game Over", rouge, hauteur // 4)
        afficher_texte_centre("Appuyez sur R pour relancer ou Q pour quitter", vert, hauteur // 2)
        pygame.display.flip()

# Boucle principale
while True:
    ecran_titre()
    if boucle_jeu():
        pygame.quit()
        break
    if not ecran_game_over():
        break

pygame.quit()