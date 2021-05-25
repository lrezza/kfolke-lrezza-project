import pygame as pg
import tetris_classes as tc
import copy
import random

fps = 10
square_size = 30
count_sqr_x = 10
count_sqr_y = 20
dis_board_x, dis_board_y = (count_sqr_x*square_size), (count_sqr_y*square_size) # Dimension of grid-board
display_x, display_y = (dis_board_x + 300), (dis_board_y)                       #Dimension of display
events = []  

# Properties of players playing
score = 0
level = 0
lines = 0

# Total number of lines the player has clear, determines the level
tot_lines_cleared = 0

#Array of RGB-colors for the figures in order: L, S, J, I, T, Z, O
fig_color = [[249, 166, 0], [0, 255, 0], [0, 0, 255], [0, 255, 255], [162, 0, 255], [255, 0, 0], [255, 255, 0]]

#The main program
def main():
    display, clock = setup()

    counter_tick = 0
    figure = new_figure()
    static_grid = [[0 for x in range(count_sqr_x)]              #2d grid used for drawing 
        for y in range(count_sqr_y)]                            #static figures                  
    
    while True:                                             
        spawn_new_figure = game_loop(display, clock, counter_tick, figure, static_grid)
        counter_tick += 1
        if spawn_new_figure:
            figure = new_figure()
             
# Main gameloop
def game_loop(display, clock, counter_tick, figure, static_grid):
    global events
    grid = copy.deepcopy(static_grid)                   # Copy the static_grid so we don't modify it
    events = pg.event.get()                             # Fetch events such as input
    
    spawn_new_figure = move_figure(figure, counter_tick, grid)

    figure.draw_shape(grid)
    draw_grid(grid,display)
    update_prop(display)
    pg.display.update()                                 # Update changes made to display
   
    clock.tick(fps)                                     # Tick
    counter_tick+=1
    if spawn_new_figure:
        figure.draw_shape(static_grid)                  # Makes sure the old figure sticks to
        check_rows(static_grid)                         # Check if rows should be deleted
    return spawn_new_figure                             # the static grid on collision with ground

#Checks the grid for full rows, if full row found it gets deleted and the pieces above 
#get moved down a step. It then calls itself again recursively until no full rows found
def check_rows(grid):
    global level
    global tot_lines_cleared 
    global score

    height = len(grid)
    width = len(grid[0])
    count_rows_deleted = 0

    full_row = False
    for y in reversed(range(height)):
        for x in range(width):
            if not full_row:
                if grid[y][x] == 0:
                    break
                elif x == width - 1:
                    full_row = True
                    count_rows_deleted = count_rows_deleted + 1
                    tot_lines_cleared = tot_lines_cleared + 1
                    for n in range(width):              #Delete row
                        grid[y][n] = 0                  
            else:
                grid[y+1][x] = grid[y][x]
    if full_row:
        check_rows(grid)
    

    #Update score according to number of cleared lines and level
    if count_rows_deleted == 1:
        score = score + 40*(level+1)
    if count_rows_deleted == 2:
        score = score + 100*(level+1)
    if count_rows_deleted == 3:
        score = score + 300*(level+1)
    if count_rows_deleted == 4:
        score = score + 1200*(level+1)

    #Update level every 10th cleared row
    if tot_lines_cleared % 5 == 0 and tot_lines_cleared != 0:
        level = level + 1
            
#Handles input and gravity to move the figure, returns whether or not to spawn a new figure
def move_figure(figure, counter_tick, grid):
    spawn_new_figure = False
    gravityApplied = False
    
    if counter_tick % 5 == 0:                           # Drop down the active figure one square 
        figure.pos.y += 1
        if figure.colliding(grid):
            figure.pos.y -= 1
            spawn_new_figure = True
        else:
            gravityApplied = True

    # Check if key is pressed by player and if so move in correct direction 
    if key_pressed(pg.K_w):
        figure.shape.rotate()
        if figure.colliding(grid):
            figure.shape.rotate_back()
    if key_pressed(pg.K_a):
        figure.pos.x -= 1
        if figure.colliding(grid):
            figure.pos.x += 1
    elif key_pressed(pg.K_d):
        figure.pos.x += 1
        if figure.colliding(grid):
            figure.pos.x -= 1
    elif key_pressed(pg.K_s) and not gravityApplied:
        figure.pos.y += 1
        if figure.colliding(grid):
            figure.pos.y -= 1
            spawn_new_figure = True

    return spawn_new_figure

# Returns a new random figure
def new_figure():
    random_index = random.randrange(7)
    return tc.Figure(tc.shapes[random_index], tc.Point(2, 0))     

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
    pg.font.init()          #initializes the font module
    pg.event.get()
    display = pg.display.set_mode((display_x, display_y))
    display.fill((10, 10, 10))
    pg.display.set_caption('Tetris')
    clock = pg.time.Clock()

    #Setup text for the display
    font_color_game_name = (0,150,250)
    font_obj_game_name = pg.font.Font('freesansbold.ttf',25)
    text_obj_game_name = font_obj_game_name.render("TETRIS",True,font_color_game_name )
    display.blit(text_obj_game_name , (dis_board_x + 10, 10))

    #Setup headlines for properties
    font_color_headlines = (0,150,250)
    font_obj_headlines = pg.font.Font('freesansbold.ttf',14)
    #Score
    text_obj_score = font_obj_headlines.render("Score",True,font_color_headlines)
    display.blit(text_obj_score, (dis_board_x + 10, 10+70))
    #Lines
    text_obj_lines = font_obj_headlines.render("Lines",True,font_color_headlines)
    display.blit(text_obj_lines , (dis_board_x + 10, 10+70+30))
    #Level
    text_obj_level = font_obj_headlines.render("Level",True,font_color_headlines)
    display.blit(text_obj_level, (dis_board_x + 10, 10+70+30+30))
    return display, clock

def update_prop(display):
        font_color_prop = (255,255,255)
        font_obj_prop = pg.font.Font('freesansbold.ttf',14)

        #Show players score
        text_obj_score_p = font_obj_prop.render(str(score),True,font_color_prop)
        display.blit(text_obj_score_p, (dis_board_x + 10+100, 10+70))
        #Show players lines
        text_obj_lines_p = font_obj_prop.render(str(lines),True,font_color_prop)
        display.blit(text_obj_lines_p, (dis_board_x + 10+100, 10+70+30))
        #Show players level
        text_obj_level_p = font_obj_prop.render(str(level),True,font_color_prop)
        display.blit(text_obj_level_p, (dis_board_x + 10+100, 10+70+30+30))

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
