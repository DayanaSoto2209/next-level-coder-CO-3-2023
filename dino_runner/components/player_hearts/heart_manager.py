from dino_runner.components.player_hearts.heart import Heart


class HeartManager:
    def __init__(self):
        self.heart_count = 4
        
    
    def reduce_heart(self):
        self.heart_count -= 1
    
    def draw(self, screen):
        pos_x = 10
        pos_y = 20
        
        for heart in range(self.heart_count):
            heart = Heart(pos_x, pos_y)
            heart.draw(screen)
            pos_x += 30