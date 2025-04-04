import pygame
import random
import os

# Initialisation de Pygame
pygame.init()

# Initialisation du module de musique
pygame.mixer.init()

# Dimensions de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("HYPNOTICA")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
vert = (0, 255, 0)

# Police de caractères
police = pygame.font.Font("assets/fonts/MINDCONTROL.ttf", 35)

# Fonction pour afficher du texte centré
def afficher_texte_centre(texte, couleur, y):
    texte_surface = police.render(texte, True, couleur)
    texte_rect = texte_surface.get_rect(center=(largeur // 2, y))
    ecran.blit(texte_surface, texte_rect)

# Écran-titre
def ecran_titre():
    # Chargement des images du GIF
    gif_images = []
    image_folder = "images_gif" # Remplacez par votre dossier
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (largeur, hauteur))
            gif_images.append(image)

    animation_frame = 0
    animation_speed = 20    # Vitesse de l'animation

    # Chargement et lecture de la musique
    pygame.mixer.music.load("assets/musics/Max Brhon - AI [NCS Release].mp3") #Remplacer par le nom de votre fichier audio
    pygame.mixer.music.play(-1)  # Lecture en boucle

    # Bouton de démarrage
    bouton_largeur = 400
    bouton_hauteur = 50
    bouton_x = largeur // 2 - bouton_largeur // 2
    bouton_y = hauteur // 3 + 100
    bouton_rect = pygame.Rect(bouton_x, bouton_y, bouton_largeur, bouton_hauteur)

    # Bouton des crédits
    credit_largeur= 400
    credit_hauteur = 50
    credit_x = largeur // 2 - credit_largeur // 2
    credit_y = hauteur // 2 + 100
    credit_rect = pygame.Rect(credit_x, credit_y, credit_largeur,credit_hauteur)

    # Bouton des instructions :
    instruction_largeur = 400
    instruction_hauteur = 50
    instruction_x = largeur // 2 - instruction_largeur // 2
    instruction_y = hauteur // 1.5 + 100
    instruction_rect = pygame.Rect(instruction_x, instruction_y, instruction_largeur, instruction_hauteur)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_rect.collidepoint(event.pos):
                    return "démarrer"  # Commencer le jeu
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
        afficher_texte_centre("Les dangers de l'addiction.", blanc, hauteur // 4)
        afficher_texte_centre("Zoléni KOKOLO ZASSI - 2025", blanc, hauteur // 4 + 50)
        pygame.draw.rect(ecran, vert, bouton_rect)
        pygame.draw.rect(ecran, rouge, credit_rect)
        pygame.draw.rect(ecran, blanc, instruction_rect)
        afficher_texte_centre("Start - SPACE", noir, bouton_y + bouton_hauteur // 2)
        afficher_texte_centre("Credits - C", noir, credit_y + credit_hauteur // 2)
        afficher_texte_centre("Instructions - I", noir, instruction_y + instruction_hauteur // 2)
        pygame.display.flip()

        # Mettre à jour l'image de l'animation
        animation_frame += 1
        if animation_frame >= len(gif_images):
            animation_frame = 0
        pygame.time.delay(1000 // animation_speed)  # Delai pour la vitesse de l'animation.

def instructions_jeu():

        police_instructions = pygame.font.Font("assets/fonts/MINDCONTROL.ttf", 20)

        texte_instructions = [
            "Bienvenue dans HYPNOTICA",
            "",
            "Objectif : Maintenir la satiété du joueur en collectant des téléphones.",
            "Utilisez les flèches LEFT et RIGHT pour déplacer le joueur.",
            "Si la satiété tombe à zéro, c'est Game Over !",
            "",
            "Appuyez sur ESPACE pour revenir au menu principal."
        ]

        instruction_largeur = 200
        instruction_hauteur = 50
        instruction_x = largeur // 2 - instruction_largeur // 2
        instruction_y = hauteur // 2 + 100
        #instruction_rect = pygame.Rect(instruction_x, instruction_y, instruction_largeur, instruction_hauteur)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return "démarrer"  # Retourne au menu principal

            ecran.fill(noir)  # Fond noir pour plus de clarté

            # Affichage du texte
            for i, ligne in enumerate(texte_instructions):
                texte_surface = police_instructions.render(ligne, True, vert)
                texte_rect = texte_surface.get_rect(center=(largeur // 2, hauteur // 4 + i * 30))
                ecran.blit(texte_surface, texte_rect)


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

# Game Over

# Écran Game Over
def ecran_game_over():
    # Arrêt de la musique
    pygame.mixer.music.stop()

    police_go = pygame.font.Font("assets/fonts/MINDCONTROL.ttf", 24)

    arriere_plan_game_over = pygame.image.load("assets/images/Game-Over-Wallpaper-48909.jpg")
    arriere_plan_game_over = pygame.transform.scale(arriere_plan_game_over, (largeur, hauteur))

    list_GO = [
        "Press to R pour restart or Q to quit or A for credits",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "Don't hesitate to RATE this prototype",
        "",
        "Zoléni KOKOLO ZASSI -- 2025"
    ]

    # Position de départ des crédits
    GO_x = largeur

    # Vitesse de défilement
    GO_vitesse = 2

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
                elif event.key == pygame.K_a:
                    return "crédits"

        ecran.blit(arriere_plan_game_over, (0, 0))

        # Affichage du texte Game Over:
        for i, GO in enumerate(list_GO):
            texte_go = police_go.render(GO, True, vert)
            texte_go_rect = texte_go.get_rect(y=hauteur // 9.5 + i * 30)  # Position verticale fixe
            texte_go_rect.x = GO_x  # Position horizontale défilante
            ecran.blit(texte_go, texte_go_rect)

        # Défilement des mots game_over :
        GO_x -= GO_vitesse

        # Réinitialisation de la position des crédits
        if GO_x < -texte_go_rect.width:  # Vérifier si le texte est complètement sorti de l'écran
            GO_x = largeur

        pygame.display.flip()
        pygame.time.delay(30)
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
                elif event.key == pygame.K_a:
                    return "crédits"



        ecran.blit(arriere_plan_game_over, (0, 0))

        #afficher_texteGO("Press R to Restart or Q to quit or A for credits ", vert, hauteur //12)
        #afficher_texteGO("Merci d'avoir participé !", blanc, hauteur//1.2)
        #afficher_texteGO("Zoléni KOKOLO ZASSI", blanc, hauteur//1.11)
        pygame.display.flip()



# Écran crédits
def ecran_credits():
    # Arrêt de la musique et nouvelle musique
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/musics/waera - harinezumi [NCS Release].mp3")
    pygame.mixer.music.play(-1)

    # Chargement de la police
    police_credits = pygame.font.Font("assets/fonts/MINDCONTROL.ttf", 32)

    # Chargement de l'image
    image_credits = pygame.image.load("assets/images/BOSS.jpg")
    image_credits = pygame.transform.scale(image_credits, (largeur // 2, hauteur // 2))
    image_credits_rect = image_credits.get_rect(center=(largeur // 2, hauteur // 4))

    # Liste des crédits
    credits = [
        "Credits",
        "",
        "Developer : Zoléni KOKOLO ZASSI",
        "",
        "Musics",
        "Max Brhon - AI [NCS Release]",
        "waera - harinezumi [NCS Release]",
        "",
        "Images : [Nom des images]",
        "",
        "Thanks for you playing ! !",
        "",
        "Press on SPACE",

        "to return to the main menu",
        "",
        "or",
        "",
        "Press on Q to quit this game",
        "",
        "To my mother, my sister",
        "and my father",
        "All rights reserved 2025",

    ]

    # Position de départ des crédits
    credits_y = hauteur

    # Vitesse de défilement
    credits_vitesse = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Modification ici
                    return  # Retourne à l'écran-titre
                if event.key == pygame.K_q:
                    return pygame.quit()

        ecran.fill(noir)
        ecran.blit(image_credits, image_credits_rect)

        # Affichage des crédits
        for i, credit in enumerate(credits):
            texte_credit = police_credits.render(credit, True, blanc)
            texte_credit_rect = texte_credit.get_rect(center=(largeur // 2, credits_y + i * 50))
            ecran.blit(texte_credit, texte_credit_rect)

        # Défilement des crédits
        credits_y -= credits_vitesse

        # Réinitialisation de la position des crédits
        if credits_y < -len(credits) * 50:
            credits_y = hauteur

        pygame.display.flip()
        pygame.time.delay(30)  # Ralentir le défilement



# Boucle principale
while True:
    choix = ecran_titre()
    if choix == "démarrer":
        if boucle_jeu():
            break
        choix_game_over = ecran_game_over()
        if choix_game_over == True:
            continue
        elif choix_game_over == "crédits":
            ecran_credits()
        else:
            break
    elif choix == "crédits":
        ecran_credits()
    elif choix == "instructions": #Ajout de la condition pour les instructions
        instructions_jeu()
    else:
        break

pygame.quit()