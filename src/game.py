import pygame as pg
import tetris_classes as tc

fps = 10
square_size = 30
count_sqr_x = 10
count_sqr_y = 20
display_x, display_y = (count_sqr_x*square_size), (count_sqr_y*square_size)
events = []  
#Array of RGB-colors for the figures in order: L, S, J, I, T, Z, O
fig_color = [[249, 166, 0], [0, 255, 0], [0, 0, 255], [0, 255, 255], [162, 0, 255], [255, 0, 0], [255, 255, 0]]

#The main program
def main():
    global events
    display, clock = setup()                                
    counter_tick = 0

    figure = tc.Figure(tc.shapes[0], tc.Point(0, 0))
    
    while True:                                             # Main gameloop
        events = pg.event.get()                             # Fetch events such as input
        grid = [[0 for x in range(count_sqr_x)]
            for y in range(count_sqr_y)]                    #2d grid

        gravityApplied = False
        if counter_tick % 5 == 0:                           # Drop down the active figure one square 
            figure.pos.y+=1
            gravityApplied = True

        if key_pressed(pg.K_w):
            figure.shape.rotate()

        if key_pressed(pg.K_a):
            figure.pos.x -= 1
        elif key_pressed(pg.K_d):
            figure.pos.x += 1
        elif key_pressed(pg.K_s) and not gravityApplied:
            figure.pos.y += 1

        figure.draw_shape(grid)
        draw_grid(grid,display)
        pg.display.update()                                 # Update changes made to display
        clock.tick(fps)                                     # Tick
        counter_tick+=1

# Check if given key is pressed
def key_pressed(key):
    global events
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == key:
                return True
    return False

# Setup window etc
def setup():                                                
    pg.display.init()
    pg.event.get()
    display = pg.display.set_mode((display_x, display_y))
    display.fill((10, 10, 10))
    pg.display.set_caption('Tetris')
    clock = pg.time.Clock()
    return display, clock

# Function to draw grid to display
# Param: grid, dis
# Return -
def draw_grid(grid, dis):
    counter = 1
    #Loop through the grid to draw every square
    for x in range(count_sqr_x):
        for y in range(count_sqr_y):
            if grid[y][x] == 0: # Empty square
                if (x+y)%2==0: 
                    pg.draw.rect(dis, (50, 50, 50), [ x * square_size, y * square_size, square_size, square_size])
                else:
                    pg.draw.rect(dis, (60, 60, 60), [ x * square_size, y * square_size, square_size, square_size])
            else : # Draw figure in correct color according to which figure it is
                fig_num = grid[y][x] - 1
                pg.draw.rect(dis, (fig_color[fig_num][0], fig_color[fig_num][1], fig_color[fig_num][2]), [ x * square_size, y * square_size, square_size, square_size])
            counter = counter +1
            
if __name__ == "__main__":
    main()
