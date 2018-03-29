from Creatures import*
from random import randint

class Grid:
    def __init__(self):
        self.new_grid()
        self.grid_size = 800;

    def new_grid(self):
        self.rect_arr = [[Creatures(i,j) for j in range(100)] for i in range(100)]
        for x in range(0,1000):
            t1 = randint(0, 99)
            t2 = randint(0, 99)
            if not self.rect_arr[t1][t2].alive:
                self.rect_arr[t1][t2] = Plant(t1,t2)

    def draw_grid(self, screen, pos_x = 0, pos_y = 0,drag = False):
        size = self.grid_size/100
        border = 1
        if size > 10:
            border = size/10
        for x in range(0, 101):
            color = (0,0,0)
            pygame.draw.line(screen, color, (pos_x, x*size+pos_y), (self.grid_size+pos_x, x*size+pos_y), int(border))
            pygame.draw.line(screen, color, (x*size+pos_x, pos_y), (x*size+pos_x, self.grid_size+pos_y), int(border))
        for i in self.rect_arr:
            for j in i:
                if j.alive:
                    pygame.draw.rect(screen,j.color,(pos_x+j.x*size+border, pos_y+j.y*size+border,size-border,size-border),0)
        pygame.display.flip()

carl = Grid()
carl.new_grid()
