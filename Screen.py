from Play import *
from Textbox import *

pygame.init()

white = (255, 255, 255)

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Adventure Game')

game_over = False

text_boxes = []
text_boxes.append(TextBox(40, 100, 200, 50))

while not game_over:
    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in text_boxes:
                box.check_click(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            for box in text_boxes:
                if box.active:
                    box.add_text(event.key)
    # UPDATE


    #DRAW
    screen.fill((0, 0, 0))

    for box in text_boxes:
        box.draw(screen)

    pygame.display.update()
