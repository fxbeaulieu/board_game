import pygame

SIDEBAR_WIDTH = 300
SCREEN_WIDTH = 700 + SIDEBAR_WIDTH
SCREEN_HEIGHT = 700
SQUARES_NUMBERS_PADDING = 5
SCREEN_TITLE = "Voyage au centre de la galaxie"

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
sidebar = pygame.Surface((SIDEBAR_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font('data/fonts/MesloLGLNerdFont-Bold.ttf', 24)
sidebar_title_font = pygame.font.Font('data/fonts/MesloLGLNerdFont-Bold.ttf',20)
text_font = pygame.font.Font('data/fonts/MesloLGLNerdFont-Bold.ttf',16)

# Load images and create display surfaces here
backgrounds = {
    1: pygame.transform.scale(pygame.image.load('data/backgrounds/world1.PNG'),(SCREEN_WIDTH - SIDEBAR_WIDTH,SCREEN_HEIGHT)),
    2: pygame.transform.scale(pygame.image.load('data/backgrounds/world2.PNG'),(SCREEN_WIDTH - SIDEBAR_WIDTH,SCREEN_HEIGHT)),
    3: pygame.transform.scale(pygame.image.load('data/backgrounds/world3.PNG'),(SCREEN_WIDTH - SIDEBAR_WIDTH,SCREEN_HEIGHT))
}
rows = {
    1: 6,
    2: 9,
    3: 10
}
columns = {
    1: 5,
    2: 5,
    3: 6
}
square_sizes = {
    1: min(SCREEN_WIDTH // columns[1], SCREEN_HEIGHT // rows[1]),
    2: min(SCREEN_WIDTH // columns[2], SCREEN_HEIGHT // rows[2]),
    3: min(SCREEN_WIDTH // columns[3], SCREEN_HEIGHT // rows[3])
}
square_colors = {
    1: {
        1: (255, 255, 255), # White
        2: (0, 153, 0),  # Green
        3: (153, 0, 0),  # Red
        4: (153, 0, 0),  # Red
        5: (0, 153, 0),  # Green
        6: (255, 255, 255), # White
        7: (153, 0, 0),  # Red
        8: (255, 255, 255), # White
        9: (255, 255, 255), # White
        10: (0, 0, 153),  # Blue
        11: (0, 153, 0),  # Green
        12: (0, 153, 0),  # Green
        13: (0, 153, 0),  # Green
        14: (255, 255, 255), # White
        15: (153, 0, 0),  # Red
        16: (0, 153, 0),  # Green
        17: (255, 255, 255), # White
        18: (0, 153, 0),  # Green
        19: (153, 0, 0),  # Red
        20: (0, 0, 153),  # Blue
        21: (0, 153, 0),  # Green
        22: (255, 255, 255), # White
        23: (153, 0, 0),  # Red
        24: (153, 0, 0),  # Red
        25: (0, 153, 0),  # Green
        26: (0, 153, 0),  # Green
        27: (153, 0, 0),  # Red
        28: (255, 255, 255), # White
        29: (0, 0, 153),  # Blue
        30: (255, 255, 255), # White
    },
    2: {
        
    },
    3: {
        
    }
}

running = True
world_active = 1

player_1_sprite = pygame.image.load('data/sprites/bleu.png')
player_2_sprite = pygame.image.load('data/sprites/mauve.png')
player_3_sprite = pygame.image.load('data/sprites/vert.png')
player_4_sprite = pygame.image.load('data/sprites/orange.png')
player_1_sprite = pygame.transform.scale(player_1_sprite, (square_sizes[world_active]/2, square_sizes[world_active]/2))
player_2_sprite = pygame.transform.scale(player_2_sprite, (square_sizes[world_active]/2, square_sizes[world_active]/2))
player_3_sprite = pygame.transform.scale(player_3_sprite, (square_sizes[world_active]/2, square_sizes[world_active]/2))
player_4_sprite = pygame.transform.scale(player_4_sprite, (square_sizes[world_active]/2, square_sizes[world_active]/2))
dice_1 = pygame.image.load('data/sprites/1.png')
dice_2 = pygame.image.load('data/sprites/2.png')
dice_3 = pygame.image.load('data/sprites/3.png')
dice_4 = pygame.image.load('data/sprites/4.png')
dice_5 = pygame.image.load('data/sprites/5.png')
dice_6 = pygame.image.load('data/sprites/6.png')

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Game logic goes here

    # Render/draw your game state
    pygame.display.set_caption(SCREEN_TITLE)
    screen.blit(backgrounds[world_active], (0,0))
    for i in range(rows[world_active]):
        y = i * SCREEN_HEIGHT // rows[world_active]
        pygame.draw.line(screen, pygame.Color('white'), (0, y), (SCREEN_WIDTH, y), 3)

    for j in range(columns[world_active]):
        x = j * (SCREEN_WIDTH - SIDEBAR_WIDTH) // columns[world_active]
        pygame.draw.line(screen, pygame.Color('white'), (x, 0), (x, SCREEN_HEIGHT), 3)
    
    for i in range(rows[world_active]):
        for j in range(columns[world_active]):
            x = j * (SCREEN_WIDTH - SIDEBAR_WIDTH) // columns[world_active]
            y = i * SCREEN_HEIGHT // rows[world_active]
            numeral_value = i * columns[world_active] + j + 1
            color = square_colors[world_active].get(numeral_value, (255, 255, 255))  # Use white as default color
            if color == (255, 255, 255):
                font_color = (0, 0, 0)
            else:
                font_color = (255, 255, 255)
            numeral = font.render(str(i * columns[world_active] + j + 1), True, font_color)
            
            # Create a rectangle surface filled with color
            text_rect = numeral.get_rect()
            numeral_bg = pygame.Surface((text_rect.width + SQUARES_NUMBERS_PADDING * 2, text_rect.height + SQUARES_NUMBERS_PADDING * 2))
            numeral_bg.fill(color)

            # Calculate the x and y coordinates for the background rectangle and numeral
            bg_x = x + square_sizes[world_active] - text_rect.width - SQUARES_NUMBERS_PADDING * 2
            bg_y = y + square_sizes[world_active] - text_rect.height - SQUARES_NUMBERS_PADDING * 2

            # Blit the background rectangle onto the screen
            screen.blit(numeral_bg, (bg_x, bg_y))

            # Blit the numeral onto the screen
            text_x = bg_x + SQUARES_NUMBERS_PADDING
            text_y = bg_y + SQUARES_NUMBERS_PADDING
            screen.blit(numeral, (text_x, text_y))
            
        sprite_offset = square_sizes[world_active] // 5  # Adjust this value as needed
        screen.blit(player_1_sprite, (0 + sprite_offset * 0, 0))
        screen.blit(player_2_sprite, (0 + sprite_offset * 1, 0))
        screen.blit(player_3_sprite, (0 + sprite_offset * 2, 0))
        screen.blit(player_4_sprite, (0 + sprite_offset * 3, 0))
        screen.blit(sidebar, (SCREEN_WIDTH - SIDEBAR_WIDTH, 0))
        player_stats = sidebar_title_font.render("Joueurs", True, (255, 255, 255))
        sidebar.blit(player_stats, (20, 10))
        sidebar.blit(dice_1, (20, SCREEN_HEIGHT - 100))

    pygame.display.update()
    
pygame.quit()