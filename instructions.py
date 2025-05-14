import pygame

pygame.init()

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Dimensions de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("HYPNOTICA")

# Instructions
def instructions_jeu():
    police_instructions = pygame.font.Font("assets/fonts/MINDCONTROL.ttf", 20)
    # image_intruction = pygame.image.load("assets/images/Instructions.jpg")
    texte_instructions = [
        "Welcome to HYPNOTICA",
        "",
        "Objective : Keep the player satiated by",
        "collecting phones.",
        "Use the LEFT and RIGHT arrows to move the player",
        "If satiety drops to zero, it's Game Over!",
        "",
        "Press SPACE to return to the main menu."
    ]

    # instruction_largeur = 200
    # instruction_hauteur = 50
    # instruction_x = largeur // 2 - instruction_largeur // 2
    # instruction_y = hauteur // 2 + 100
    # instruction_rect = pygame.Rect(instruction_x, instruction_y, instruction_largeur, instruction_hauteur)

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
            texte_surface = police_instructions.render(ligne, True, blanc)
            texte_rect = texte_surface.get_rect(center=(largeur // 2, hauteur // 4 + i * 30))
            ecran.blit(texte_surface, texte_rect)

        pygame.display.flip()

if __name__ == "__main__":
    instructions_jeu() # ----> Test de la function