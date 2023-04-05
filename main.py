import pygame
from shapes import shapes, colors

# 1 initialisation de pygame !
pygame.init()

#declaration de variable utilisée
width = 600
height = 300
block = 30 #600//30 = 30 300//30 = 10 ce qui fait 30 px pour les formes
screen_w = 600
screen_h = 650
#variable qui stocke le noir
black = (0, 0, 0)
#topleft en x et y placement de grille de jeu
tlx = 50
tly = 50

class Pieces():
    def __init__(self, x , y , shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = [shapes.index(shape)]
        self.rotate = 0 



# création de la grille de forme posées
# tableau de 20 index, qui comprend un tableau qui comprend 
# 10 fois la couleurs noir
# cette grille represente notre jeu
def make_grid(static):
    grid = [[black for _ in range(10)]for _ in range(20)]
    #  parcour du premier tableau et on recupere l'index
    for i in range(len(grid)):
        # ensuite parcour de grid de i 
        for j in range (len(grid[i])):
            # on verifie les coordonnées de i et y sont dans notre dictionnaire
            if (j, i) in static:
                grid[i][j] = static[(j, i)]
    return grid

# recuperer le tableau en x et y
def draw_grid(screen, grid):
    for i in range(len(grid)):
        # axe y coordonnée de départ et d'arriver couleur
        # draw line dessine directement sur la fenetre
        # surface, couleur (coordonnée de départ => fixe) (coordonnée d'arrivée) 
        pygame.draw.line(screen, (255, 255, 255), (tlx, tly+i*block), (tlx+width,  tly+i*block))
        
# boucle de jeu
def main(screen):
    static = {}
    run = True
    grid = make_grid(static)
    while run:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False

#appel fonction draw_grid pour dessiner les ligne doit etre dans la bouCle ?
    draw_grid(screen, grid)
        # maj fenetre
    pygame.display.flip()


#definition de notre fenetre doit rester en bas
screen = pygame.display.set_mode((screen_h, screen_w))
#appelle de la fonction main pour que la fenetre reste ouverte
main(screen)
# quitter la fenetre
pygame.quit()