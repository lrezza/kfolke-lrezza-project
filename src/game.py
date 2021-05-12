import pygame as pg

fps = 5 
square_size = 15
count_sqr_x = 10
count_sqr_y = 20
display_x, display_y = (count_sqr_x*square_size), (count_sqr_y*square_size)
events = []  

#The main program
def main():
    global events
    display, clock = setup()                                
    #2d grid o
    grid  = [[0 for x in range(count_sqr_x)]for y in range(count_sqr_y)]

    while True:                                             # Main gameloop
        events = pg.event.get()                             # Fetch events such as input
        draw_grid(grid,display)
        pg.display.update()                                 # Update changes made to display
        clock.tick(fps)                                     # Tick

# Setup window etc
def setup():                                                
    pg.display.init()
    pg.event.get()
    #display = pg.display.set_mode((display_x, display_y))
    display = pg.display.set_mode((display_x, display_y))
    #display.fill((50, 50, 50))
    display.fill((10, 10, 10))
    pg.display.set_caption('Tetris')
    clock = pg.time.Clock()
    return display, clock

# Function to draw grid to display
# Param: 
def draw_grid(grid, dis):
    counter = 1
    for x in range(count_sqr_x):
        for y in range(count_sqr_y):
            if (x+y)%2==0: 
                pg.draw.rect(dis, (50, 50, 50), [ x * square_size, y * square_size, square_size, square_size])
            else:
                pg.draw.rect(dis, (60, 60, 60), [ x * square_size, y * square_size, square_size, square_size])
            counter = counter +1

if __name__ == "__main__":
    main()
