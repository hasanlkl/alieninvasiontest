import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self, ai_game, is_powerful=False):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.is_powerful = is_powerful
        
        # Güçlü mermi farklı renk ve boyutta
        if self.is_powerful:
            self.color = self.settings.powerful_bullet_color
            self.rect = pygame.Rect(0, 0, self.settings.powerful_bullet_width, 
                                   self.settings.powerful_bullet_height)
        else:
            self.color = self.settings.bullet_color
            self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                                   self.settings.bullet_height)
        
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

