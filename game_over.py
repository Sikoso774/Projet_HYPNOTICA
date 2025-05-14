import pygame

# Initialisation de Pygame

pygame.init()       # ----> On initialise seulement pour les tests
pygame.mixer.init() # ----> Même chose ici

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
gris = (96, 96, 96)
rouge = (255, 0, 0)
vert = (0, 255, 0)

# Dimensions de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("HYPNOTICA")

# Écran Game Over
def Game_Over():
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

if __name__ == "__main__":
    Game_Over()