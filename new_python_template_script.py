import pygame
import sys

SIDEBAR_WIDTH = 300
SCREEN_WIDTH = 700 + SIDEBAR_WIDTH
SCREEN_HEIGHT = 700
SQUARES_NUMBERS_PADDING = 5
SCREEN_TITLE = "Voyage au centre de la galaxie"

pygame.init()
main_menu_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
sidebar = pygame.Surface((SIDEBAR_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font('data/fonts/MesloLGLNerdFont-Bold.ttf', 24)
sidebar_title_font = pygame.font.Font('data/fonts/MesloLGLNerdFont-Bold.ttf',20)
text_font = pygame.font.Font('data/fonts/MesloLGLNerdFont-Bold.ttf',18)

# Load images and create display surfaces here
backgrounds = {
    0: pygame.transform.scale(pygame.image.load('data/backgrounds/main_menu.PNG'),(SCREEN_WIDTH,SCREEN_HEIGHT)),
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
global world_active
world_active = 0

def draw_text_input(prompt, text):
    screen.fill((0,0,0))
    prompt_msg = font.render(prompt, True, (255,255,255))
    screen.blit(prompt_msg, (SCREEN_WIDTH // 2 - prompt_msg.get_width() // 2, SCREEN_HEIGHT // 4))
    text_msg = font.render(text, True, (255,255,255))
    screen.blit(text_msg, (SCREEN_WIDTH // 2 - text_msg.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

def get_player_name(player_number):
    name = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

        draw_text_input(f"Le nom du joueur {player_number} :", name)

def start_menu(world_active):
    main_menu_screen.blit(backgrounds[world_active], (0,0))
    menu_items = ["2 joueurs", "3 joueurs", "4 joueurs"]
    global current_item
    current_item = 0
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    current_item = (current_item - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    current_item = (current_item + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    world_active = 1
                    return world_active,current_item + 2

        for i, text in enumerate(menu_items):
            if i == current_item:
                msg = font.render(text, True, (0,153,0))
            else:
                msg = font.render(text, True, (0,0,0))
            main_menu_screen.blit(msg, (20, 10 + i * 60))
        pygame.display.update()

def world_1_active_screen(number_of_players,player_names):
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
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
        
        player_sprites = [player_1_sprite, player_2_sprite, player_3_sprite, player_4_sprite]

        for i in range(number_of_players):
            screen.blit(player_sprites[i], (0 + sprite_offset * i, 0))
        
        # Render the sidebar title
        player_stats = sidebar_title_font.render("Joueurs", True, (255, 255, 255))
        screen.blit(sidebar, (SCREEN_WIDTH - SIDEBAR_WIDTH, 0))
        sidebar.blit(player_stats, (20, 10))

        # Loop over the player names according to the number of players
        for i in range(number_of_players):
            player_name = text_font.render(player_names[i], True, (255, 255, 255))
            sidebar.blit(player_name, (20, 50 + i * 40))

        # Render the dice
        sidebar.blit(dice_1, (20, SCREEN_HEIGHT - 100))
        player_stats = sidebar_title_font.render("Joueurs", True, (255, 255, 255))
        screen.blit(sidebar, (SCREEN_WIDTH - SIDEBAR_WIDTH, 0))
        sidebar.blit(player_stats, (20, 10))
        sidebar.blit(dice_1, (20, SCREEN_HEIGHT - 100))

    pygame.display.update()

while running:
    sidebar.fill((0, 0, 0))

    # Game logic goes here

    # Render/draw your game state
    pygame.display.set_caption(SCREEN_TITLE)
    while world_active == 0:
        world_active,number_of_players = start_menu(world_active)
        if number_of_players == 2 or number_of_players == 3 or number_of_players == 4:
            player_names = []
            for i in range(1, number_of_players + 1):
                player_names.append(get_player_name(i))

    while world_active == 1:
        world_1_active_screen(number_of_players,player_names)

    pygame.display.update()
    
pygame.quit()