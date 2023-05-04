import pygame

from dino_runner.utils.constants import (
    BG, 
    ICON, 
    SCREEN_HEIGHT,
    SCREEN_WIDTH, 
    TITLE, 
    FPS,
    FONT_ARIAL,
    MOON,
    SUN,
    STAR
    )
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.player_hearts.heart_manager import HeartManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.colors = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.heart_manager = HeartManager()
        
    
    def increase_score(self):
        self.points += 1
        if self.points / 100 == 0:
            self.game_speed += 1
  
        self.player.check_invisibility()
        
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        
    def play(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(1000)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.increase_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.black_While() 
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.heart_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        
        
    def black_While(self):
        self.colors += 1
        if self.colors >= 200:
            self.screen.fill((0, 0, 0))
            self.screen.blit(MOON, (150, 20)) 
            self.star()
            if self.colors >= 400:
                self.colors = 0
        else:
            self.screen.fill((255,255,255))
            self.screen.blit(SUN, (500,10))
            
    def star(self):
        image_width = STAR.get_width() 
        self.screen.blit(STAR, (image_width + self.x_pos_bg +1520, self.y_pos_bg -250))
        self.screen.blit(STAR, (image_width + self.x_pos_bg +1870, self.y_pos_bg -350))
        self.screen.blit(STAR, (image_width + self.x_pos_bg +2400 , self.y_pos_bg -300))        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def draw_score(self):
        font = pygame.font.Font(FONT_ARIAL, 30)
        surface = font.render(str(self.points), True, (0, 0, 0))
        rect = surface.get_rect()
        rect.x = 1000
        rect.y = 10
        self.screen.blit(surface, rect)
    