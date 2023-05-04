import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import DEFAULT_TYPE

class PowerUpManager:
    
    def __init__(self):
        self.power_ups = []
        self.points = 0
        self.when_appears = 0
    
    def generate_power_up(self, points, player):
        self.points = points
        
        if len(self.power_ups) == 0 and player.type == DEFAULT_TYPE:
            self.when_appears = random.randint(1,50)
            if self.when_appears == 5:
                print("Generating power up")
                #self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                self.power_ups.append(Shield())
        
            elif self.when_appears == 2:
                print("Generating power up")
                #self.when_hammers = random.randint(self.when_hammers + 200, 500 + self.when_hammers)
                self.power_ups.append(Hammer())
    
    def update(self, points, game_speed, player):
        self.generate_power_up(points, player)
        
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                player.shield = True
                player.type = power_up.type
                
                
                start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.shield_time_up = start_time + (time_random * 1000)
                
                self.power_ups.remove(power_up)
                
                             
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)