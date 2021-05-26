Project by Leonardo Rezza and Klara Folke 2021
## Specifications

### Link to repository

https://github.com/lrezza/kfolke-lrezza-project

### Link to Trello
https://trello.com/b/9dqRhgiH/kfolke-lrezza-project-tetris 

### Naming conventions

#### Issues & Commits 

Future tense example "Add new feature" for commits and example "Fix this bug" for issues. 

#### Pull requests

feature/feature-name

issue/nr-issue-name

### Project

We're creating tetris in python with help of the pygame library. 

The game will consist of a board of empty squares (20x10). When starting the game one out of six different figures (consisting of 4 blocks) will start to fall down (one row down per unit of time). When the player presses the X-button the figure will rotate 90 degrees to the right. The player can also press Y-button to move the figure to the right and the Z-button to move the figure to the right. When pressing the Q-button the figure will in the current colon drop down and place itself over the lowest non-empty square. Also, if a non-empty square is right below the figure, the figure will stop moving and place itself on the square abow the non-empty square. When the figure has been placed the player can not move it anymore and the next figure (one out of the six possible ones) will start moving down and the procedure repeats itself until the player loses and the program will end which means that one or more of the squares where a new figure is supposed to start is not empty. 

The player will gain points for every full row which will be deleted so the whole board abow the row can move down one row. The following points system has been implemented (except for the lines after the grid which we didn't understand hihi.) The player will move up one level for every 10th cleared row and level does not mean anything more than that. 

![](https://trello-attachments.s3.amazonaws.com/608bc1a49c05532826643faa/60927fa754ff8b80a1011b38/a287eeb4badf2caeb56b9ab0d3be0ef1/Sk%C3%A4rmavbild_2021-05-25_kl._21.09.33.png)

The number of lines the player currently has figures on is displayed on the right side of the board together with score and level.

The work will be divided by milestone, so each person will take on their own milestones. 

#### Execute the program

To play the game the player should be in the src folder and type "python3 game.py" followed by enter.

##### Controls
Controls: 
Press S to make the active figure go down one square.
Press W to rotate the figure.
Press A to make the active figure go one square to the left.
Press D to make the active figure go one square to the right.

### Schedule 

#### Week 18
- Fix a Trello-board and a github repo with README and start planning the project. (Both)
- Create a drawable grid: (Klara)
    This will be used for drawing empty and filled squares of different colors by passing in a matrix will integer values 
    ranging from 0 to 7 where 1-7 are the colors of figures 1-7. The grid will be shown as a checkboard looking board in order for each square to be seen easily and the board will be like the classic Tetris 20x10.

- Create class for figures, shapes and points: (Leo)
    Each one of the seven figures will have a unique color and shape. Shapes class will be used to predefine
    the 7 different shapes of figures in tetris and will be used in the figureclass instance for drawing and collisionchecking.
![](https://mindyourdecisions.com/blog/wp-content/uploads/2018/05/tetris-riddle-thumb-600.png)

#### Week 19
- Add colors based on shapes and ticktimer for gravity (Klara)
    You should be able to move a couple of times before each "gravitytick"
- Add input and collisionchecks for figures (Leo)
    Make sure that figures don't go through walls and that they stick to the ground on collision. Take input

#### Week 20
- Make score, lines and level viewable at the display/board (Klara)
- Prepare a presentation of the game for the ovning (Both)

#### Week 21
- Implement loosing condition (Leo)
- Make the board drop down on row when a row below is deleted due to being full. (Leo)
- Implement a scoring, level and lines system (Klara)
- Clean up the code and comment uncommented parts (Both)
- Test the game by playing it and fix bugs (Both)
