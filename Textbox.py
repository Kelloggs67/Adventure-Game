import pygame

vec = pygame.math.Vector2

class TextBox:
    def __init__(self, x, y, width, height, bg_color=(124,124,124), active_color=(255,255,255), text_size=18, text_color=(0,0,0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = vec(x, y)
        self.size = vec(width, height)
        self.image = pygame.Surface((width, height))
        self.bg_color = bg_color
        self.active_color = active_color
        self.active = False
        self.text = ""
        self.text_size = text_size
        self.text_color = text_color
        self.font = pygame.font.SysFont("arial", self.text_size)

    def update(self):
        pass

    def draw(self, window):
        if not self.active:
            self.image.fill(self.bg_color)
            #Rendering text to image
            text = self.font.render(self.text, False, self.text_color)
            self.image.blit(text, (0,0))
        else:
            self.image.fill(self.active_color)
            # Rendering text to image
            text = self.font.render(self.text, False, self.text_color)
            self.image.blit(text, (0, 0))
        window.blit(self.image, self.pos)

    def add_text(self, key):
        text = list(self.text)
        text.append(chr(key))
        self.text = "".join(text)
        print(self.text)

    def check_click(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y+self.height:
                self.active = True
            else:
                self.active = False
        else:
            self.active = False

