import pymunk 
import pygame 
import math 
import pymunk.pygame_util

pygame.init()

WIDTH, HEIGHT = 800, 600 
window = pygame.display.set_mode((WIDTH, HEIGHT))



def draw(space, window, draw_options): 
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()



def run(window, dimensions): 
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps

    space = pymunk.Space() 
    space.gravity = (0, -9.82)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False
                break
        draw(space, window, draw_options)
        space.step(dt)
        clock.tick(fps)
    
    pygame.quit()

if __name__ == "__main__": 
    run(window,(WIDTH, HEIGHT))