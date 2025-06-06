import pygame

pygame.init()
pygame.mixer.init()

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Taille de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("HYPNOTICA")

def Ecran_Credits():
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
        "Image generated by AI",
        "",
        "",
        "Musics",
        "Max Brhon - AI [NCS Release]",
        "More Plastic - Rewind [NCS Release]",
        "waera - harinezumi [NCS Release]",
        "",
        "",
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
        "",
        "All rights reserved 2025",
        "",
        "ENSEA Cergy-Pontoise",

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
                    return                       # Returner à l'écran-titre
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

if __name__ == "__main__":
    Ecran_Credits()           # ----> Test de la function crédits
