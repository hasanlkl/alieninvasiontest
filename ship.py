import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    "Gemi"
    
    def __init__(self, ai_game):
        "Gemiyi oluştur ve başlangıç konumuna yerleştir"
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x    


    def blitme(self):
        "Gemiyi belirtilen konumda çiz"
        self.screen.blit(self.image, self.rect)
    
    def draw_power_bar(self, bullet_counter):
        """Güçlü mermi ilerleme çubuğunu çiz"""
        # Çubuğun konumu - geminin üstünde
        bar_x = self.rect.centerx - self.settings.progress_bar_width // 2
        bar_y = self.rect.top - 15
        
        # Arka plan (boş çubuk)
        background_rect = pygame.Rect(bar_x, bar_y, 
                                     self.settings.progress_bar_width, 
                                     self.settings.progress_bar_height)
        pygame.draw.rect(self.screen, self.settings.progress_bar_color, background_rect)
        
        # İlerleme yüzdesi (0-10 arası -> 0-100%)
        progress = (bullet_counter % 10) / 10
        fill_width = int(self.settings.progress_bar_width * progress)
        
        # Dolu kısım - 10. mermide kırmızı, diğerlerinde turuncu
        if bullet_counter % 10 == 0 and bullet_counter > 0:
            fill_color = self.settings.progress_powerful_color
        else:
            fill_color = self.settings.progress_fill_color
        
        if fill_width > 0:
            fill_rect = pygame.Rect(bar_x, bar_y, fill_width, 
                                   self.settings.progress_bar_height)
            pygame.draw.rect(self.screen, fill_color, fill_rect)
        
        # Çerçeve
        pygame.draw.rect(self.screen, (0, 0, 0), background_rect, 1)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x) 