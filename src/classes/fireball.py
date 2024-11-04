from src.classes.entity import Entity

class Fireball(Entity):
    def __init__(self, target, screen, position, size):
        super().__init__(screen, position, "fireball", size)
        self.target = target

    def move(self):
        direction = self.target.position - self.position
        movement = direction.normalize() * 0.5
        self.move_without_collision(movement)
        pass