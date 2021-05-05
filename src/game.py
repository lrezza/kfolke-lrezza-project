import pygame as pg

### SETTINGS ###
display_x, display_y = 400, 600                             
fps = 5

events = []     

def main():
    global events
    display, clock = setup()                                

    while True:                                             # Main gameloop
        events = pg.event.get()                             # Fetch events such as input

        pg.display.update()                                 # Update changes made to display
        clock.tick(fps)                                     # Tick

def setup():                                                # Setup window etc
    pg.display.init()
    pg.event.get()
    display = pg.display.set_mode((display_x, display_y))
    display.fill((50, 50, 50))
    pg.display.set_caption('Tetris')
    clock = pg.time.Clock()
    return display, clock

if __name__ == "__main__":
    main()