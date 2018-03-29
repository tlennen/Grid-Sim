from Grid import pygame
from pygame.locals import *
from Grid import Grid


class Board():
    def __init__(self):
        self.grid = Grid()
        self.drag = False
        self.drag_x = self.drag_y = self.origin_x = self.origin_y = 0
        self.screen_width = 800
        self.screen_height = 600
        self.count = 0
        self.elapsed_time = 0
        self.speed = 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption('Test')
        pygame.init()
        self.screen.fill((255, 255, 255))
        self.grid.draw_grid(self.screen)
        pygame.display.flip()
        self.clock = pygame.time.Clock()

    def draw_board(self):
        done = True

        while done:
            pygame.event.pump()
            event = pygame.event.poll()
            if event.type == QUIT:
                pygame.display.quit()
                break
            elif event.type == VIDEORESIZE:
                width, height = event.size
                if width < 100:
                    width = 100
                if height < 100:
                    height = 100
                self.screen = pygame.display.set_mode((width, height), HWSURFACE | DOUBLEBUF | RESIZABLE)
            self.screen.fill((255, 255, 255))
            self.grid.draw_grid(self.screen, self.drag_x, self.drag_y)
            self.mouse_events(event)
            self.key_events(event)
            self.elapsed_time += self.clock.tick()
            if self.elapsed_time > self.speed:
                self.elapsed_time = 0
                self.grid.new_grid()
            pygame.display.flip()

    def mouse_events(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.origin_x = mouse_x - self.drag_x
                self.origin_y = mouse_y - self.drag_y
                self.drag = True

        if self.drag:
            self.drag_x = mouse_x - self.origin_x
            self.drag_y = mouse_y - self.origin_y

        if event.type == pygame.MOUSEBUTTONUP:
            self.drag = False
        # do other stuff"""

    def key_events(self,event):
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_x]:
            if self.grid.grid_size > 600:
                self.grid.grid_size -= 100
            print(self.grid.grid_size)
        if keys[pygame.K_z]:
            if self.grid.grid_size < 5000:
                self.grid.grid_size += 100
            print(self.grid.grid_size)
        """if keys[pygame.K_v]:
            self.speed+=250
        if keys[pygame.K_c]:
            self.speed-=250"""


game = Board()
game.draw_board()
