import pygame
import sys

# Pygame Start
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 512, 512
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Teste")

# Cores
white = (255, 255, 255)

# Carregue as imagens de background das fases
backgrounds = [pygame.image.load('background.jfif'), pygame.image.load('background2.jpg')]
current_background = 0  # Índice do cenário atual

# Carregue a imagem do personagem
character_imagelist = [pygame.image.load('Gohan/tile000.png'), pygame.image.load('Gohan/tile004.png'), pygame.image.load('Gohan/tile013.png'), pygame.image.load('Gohan/tile017.png'), pygame.image.load('Gohan/tile015.png')]
character_hitlist = [pygame.image.load('Gohan/tile074.png'), pygame.image.load('Gohan/tile076.png'), pygame.image.load('Gohan/tile067.png'), pygame.image.load('Gohan/tile066.png')]
character_image = character_imagelist[0]
character_width, character_height = 100, 100
character_image = pygame.transform.scale(character_image, (character_width, character_height))

# Posição inicial do personagem
character_x = WIDTH // 2
character_y = HEIGHT - character_height

# Velocidade do personagem
character_speed = 0.3

# Função para desenhar o personagem
def draw_character(x, y):
    screen.blit(character_image, (x, y))

# Loop do jogo
running = True
while running:
    character_image = character_imagelist[0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character_x > 0:
        character_x -= character_speed
        character_image = character_imagelist[3]
    if keys[pygame.K_RIGHT] and character_x < WIDTH - character_width:
        character_x += character_speed
        character_image = character_imagelist[1]
    if keys[pygame.K_DOWN] and character_y < HEIGHT - character_height:
        character_y += character_speed
        character_image = character_imagelist[4]
    if keys[pygame.K_UP] and character_y > 0:
        character_y -= character_speed
        character_image = character_imagelist[2]
        

    

    # Verifique se o personagem chegou ao fim da tela (mudança de fase)
    if character_x >= (WIDTH - character_width):
        current_background = (current_background + 1) % len(backgrounds)
        character_x = 0  # Reinicie o personagem na posição inicial da nova fase

    # Desenhe o cenário de background da fase atual
    screen.blit(backgrounds[current_background], (0, 0))

    # Desenhe o personagem
    draw_character(character_x, character_y)

    pygame.display.update()

# Encerre o Pygame
pygame.quit()
sys.exit()
