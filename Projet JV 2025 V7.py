import pygame
import random
import math
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
gris = (96,96,96)
rouge = (255, 0, 0)
vert = (0, 255, 0)
bleu = (0,0,255)
violet = (127,0,255)


# Police de caractères
police = pygame.font.Font("assets/fonts/MINDCONTROL.ttf", 35)

# Fonction pour afficher du texte centré
def afficher_texte_centre(texte, couleur, y):
    texte_surface = police.render(texte, True, couleur)
    texte_rect = texte_surface.get_rect(center=(largeur // 2, y))
    ecran.blit(texte_surface, texte_rect)

# Fonction Pygame ---> Hypnose_.gif

# Charger l'image pygame_logo.png
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

def presentation(images, duree_affichage=3000):
    """
    Affiche une séquence d'images avec un fondu enchaîné et des textes associés.

    Args:
        images (list): Liste des chemins des images à afficher.
        duree_affichage (int): Durée d'affichage de chaque image en millisecondes.
    """

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

# Transition
def transition(image_fin, gif_images, duree_transition=2000):
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
    pygame.mixer.music.load("assets/musics/More Plastic - Rewind [NCS Release].mp3")
    pygame.mixer.music.play(-1)

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



        ecran.blit((0, 0))

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
    image_credits = pygame.image.load("assets/images/Zoléni_Cyberpunk.jpg")
    image_credits = pygame.transform.scale(image_credits, (largeur // 2.5, hauteur // 2.5))

    # Liste des crédits (avec l'image intégrée)
    credits = [
        "Credits",
        "",
        "Developer : Zoléni KOKOLO ZASSI",
        "",
        "",
        image_credits,  # Ajout de l'image à la liste
        "",
        "",
        "Musics",
        "Max Brhon - AI [NCS Release]",
        "More Plastic - Rewind [NCS Release]",
        "waera - harinezumi [NCS Release].mp3",
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

        # Affichage des crédits (avec l'image)
        for i, credit in enumerate(credits):
            if isinstance(credit, pygame.Surface):  # Vérifier si c'est une image
                credit_rect = credit.get_rect(center=(largeur // 2, credits_y + i * 50))
                ecran.blit(credit, credit_rect)
            else:  # Sinon, c'est du texte
                texte_credit = police_credits.render(credit, True, blanc)
                texte_credit_rect = texte_credit.get_rect(center=(largeur // 2, credits_y + i * 50))
                ecran.blit(texte_credit, texte_credit_rect)

        # Défilement des crédits
        credits_y -= credits_vitesse

        # Réinitialisation de la position des crédits
        if credits_y < -len(credits) * 50:
            credits_y = hauteur

        pygame.display.flip()
        pygame.time.delay(30) # Ralentir le défilement



# Boucle principale

presentation(["assets/images/Zoléni_Cyberpunk.jpg","assets/images/Logo_ENSEA.jpg",
              "assets/images/pygame_logo.png"])
transition(image_fin, gif_images=gif_images)
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