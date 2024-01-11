import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, BLACK, WHITE
from checkers.game import Game
from minmax.algorithm import minMax

FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_mouse_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

run = True
clock = pygame.time.Clock()
game = Game(WIN)
started = False
set_leveled = False
level = None

# Load the font
h_font = pygame.font.Font(None, 72)
h_font.set_bold(True)
font = pygame.font.Font(None, 36)

# Create the menu options
game_header1_text = h_font.render("Checkers Game", True, (255, 255, 255))
start_text = font.render("Start Game", True, (255, 255, 255))
quit_text = font.render("Quit", True, (255, 255, 255))

game_header2_text = font.render("Set the depth level of your AI opponent", True, (255, 255, 255))
easy_text = font.render("Easy", True, (255, 255, 255))
normal_text = font.render("Normal", True, (255, 255, 255))
hard_text = font.render("Hard", True, (255, 255, 255))
legend_text = font.render("Legend", True, (255, 255, 255))

White_text = font.render("White Won The Game!", True, (255, 255, 255))
Black_text = font.render("Black Won The Game!", True, (255, 255, 255))
play_again_text = font.render("Paly Again", True, (255, 255, 255))

# Set the position of the menu options
game_header1_pos = (WIDTH // 2 - game_header1_text.get_width() // 2, HEIGHT//2.5)
start_pos = (WIDTH // 2 - start_text.get_width() // 2, HEIGHT//2)
quit_pos = (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT//2 + HEIGHT//18)

game_header2_pos = (WIDTH // 2 - game_header2_text.get_width() // 2, HEIGHT//2.5)
easy_pos = (1*SQUARE_SIZE - easy_text.get_width()//2, HEIGHT//2 - easy_text.get_height()//2)
normal_pos = (3*SQUARE_SIZE - normal_text.get_width()//2, HEIGHT//2 - normal_text.get_height()//2)
hard_pos = (5*SQUARE_SIZE - hard_text.get_width()//2, HEIGHT//2 - hard_text.get_height()//2)
legend_pos = (7*SQUARE_SIZE - legend_text.get_width()//2, HEIGHT//2 - legend_text.get_height()//2)

White_pos = (WIDTH // 2 - White_text.get_width() // 2, HEIGHT//2.5)
Black_pos = (WIDTH // 2 - Black_text.get_width() // 2, HEIGHT//2.5)
play_again_pos = (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT//2)


while run:
    background = pygame.transform.scale(pygame.image.load('items/background.jpg'), (WIDTH, HEIGHT))
    clock.tick(FPS)
    
    if game.turn == WHITE:
        value, new_board = minMax(game.get_board(), level, WHITE, game)
        game.ai_move(new_board)


    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is on the "Start Game" option
            if 'start_rect' in locals() or 'start_rect' in globals():
                if start_rect.collidepoint(event.pos):
                    # Start the game
                    started = True

            # Check if the mouse click is on the "Play Again" option
            if 'play_again_rect' in locals() or 'play_again_rect' in globals():
                if play_again_rect.collidepoint(event.pos):
                    # restart the game
                    game.reset()
                    started = True
                    set_leveled = False
                    level = None

            # Check if the mouse click is on the "Quit" option
            if 'quit_rect' in locals() or 'quit_rect' in globals():
                if quit_rect.collidepoint(event.pos):
                    # Quit the game
                    run = False

            if 'Easy_rect' in locals() or 'Easy_rect' in globals():
                if Easy_rect.collidepoint(event.pos):
                    # set the level depth of min-max
                    level = 1
                    set_leveled = True

            if 'Normal_rect' in locals() or 'Normal_rect' in globals():
                if Normal_rect.collidepoint(event.pos):
                    # set the level depth of min-max
                    level = 2
                    set_leveled = True

            if 'Hard_rect' in locals() or 'Hard_rect' in globals():
                if Hard_rect.collidepoint(event.pos):
                    # set the level depth of min-max
                    level = 3
                    set_leveled = True

            if 'legend_rect' in locals() or 'legend_rect' in globals():
                if legend_rect.collidepoint(event.pos):
                    # set the level depth of min-max
                    level = 4
                    set_leveled = True

            # Starting the game
            if started and set_leveled:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos)
                game.select(row, col)


    if game.winner() != None:
        # Blit the background image
        WIN.blit(background, (0, 0))
        # Blit the menu options
        if game.winner() == WHITE:
            WIN.blit(White_text, White_pos)
        else:
            WIN.blit(Black_text, Black_pos)
        play_again_rect = WIN.blit(play_again_text, play_again_pos)
        quit_rect = WIN.blit(quit_text, quit_pos)

    if not started:
        # Blit the background image
        WIN.blit(background, (0, 0))
        # Blit the menu options
        WIN.blit(game_header1_text, game_header1_pos)
        start_rect = WIN.blit(start_text, start_pos)
        quit_rect = WIN.blit(quit_text, quit_pos)

    if started and not set_leveled:
        # Blit the background image
        WIN.blit(background, (0, 0))
        # Blit the menu options
        WIN.blit(game_header2_text, game_header2_pos)
        Easy_rect = WIN.blit(easy_text, easy_pos)
        Normal_rect = WIN.blit(normal_text, normal_pos)
        Hard_rect = WIN.blit(hard_text, hard_pos)
        legend_rect = WIN.blit(legend_text, legend_pos)

    # Update the screen
    if (not started) or (not set_leveled and started) or (game.winner() != None):
        pygame.display.flip()
    else:
        game.update()

pygame.quit()