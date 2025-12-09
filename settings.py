class Settings:
    "Ayarların saklandığı sınıf"

    def __init__(self):
        "Ayarların başlatılması"
        # Ekran ayarları
        self.screen_width = 1920    
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)
        
        # Gemi ayarları
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Oyun ayarları
        self.ship_speed = 1.5
        self.bullet_speed = 5
        self.bullet_width = 200
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6
        
        # Güçlü mermi ayarları
        self.powerful_bullet_width = 150
        self.powerful_bullet_height = 20
        self.powerful_bullet_color = (255, 0, 0)  # Kırmızı
        
        # İlerleme çubuğu ayarları
        self.progress_bar_width = 100
        self.progress_bar_height = 8
        self.progress_bar_color = (100, 100, 100)  # Gri (boş)
        self.progress_fill_color = (255, 165, 0)  # Turuncu (dolu)
        self.progress_powerful_color = (255, 0, 0)  # Kırmızı (güçlü mermi hazır)    

        # Uzaylı ayarları
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 

        # Oyun hızlandırma 
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        # Mermi bazlı hızlanma sistemi
        self.bullet_speedup_interval = 10  # Her 10 mermide bir hızlanma
        self.bullet_speedup_scale = 1.03  # %3 artış
        self.max_speed_multiplier = 10.0  # Maksimum 2x hız (başlangıca göre)

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # Başlangıç hızlarını sakla (maksimum kontrol için)
        self.initial_ship_speed = 1.5
        self.initial_bullet_speed = 3.0
        self.initial_alien_speed = 1.0

        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Seviye atladığında hız artırma (eski sistem)"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        # Başlangıç hızlarını da güncelle
        self.initial_ship_speed = self.ship_speed
        self.initial_bullet_speed = self.bullet_speed
        self.initial_alien_speed = self.alien_speed

        self.alien_points = int(self.alien_points * self.score_scale)
    
    def increase_speed_by_bullets(self):
        """Mermi sıktıkça hız artırma (yeni sistem)"""
        # Maksimum hız kontrolü
        if self.alien_speed < self.initial_alien_speed * self.max_speed_multiplier:
            self.ship_speed *= self.bullet_speedup_scale
            self.bullet_speed *= self.bullet_speedup_scale
            self.alien_speed *= self.bullet_speedup_scale
            return True
        return False
        
