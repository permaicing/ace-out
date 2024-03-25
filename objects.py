from primitives import Triangle


class Ship(Triangle):

    def __init__(self, coords, color, length, speed):
        super().__init__(coords, color, length)
        self.speed = speed
    
    def move_left(self, displacement):
        self.coords[0] = max(self.coords[0]-displacement, -1+self.length/2)
    
    def move_up(self, displacement):
        self.coords[1] = min(self.coords[1]+displacement, -0.25)
    
    def move_down(self, displacement):
        self.coords[1] = max(self.coords[1]-displacement, -1+self.length/2)

    def move_right(self, displacement):
        self.coords[0] = min(self.coords[0]+displacement, 1-self.length/2)