
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

The game will consist of a board of empty squares (20x10). When starting the game one out of six different figures (consisting of 4 blocks) will start to fall down (one row down per unit of time). When the player presses the X-button the figure will rotate 90 degrees to the right. The player can also press Y-button to move the figure to the right and the Z-button to move the figure to the right. When pressing the Q-button the figure will in the current colon drop down and place itself over the lowest non-empty square. Also, if a non-empty square is right below the figure, the figure will stop moving and place itself on the square abow the non-empty square. When the figure has been placed the player can not move it anymore and the next figure (one out of the six possible ones) will start moving down and the procedure repeats itself until the player loses which means that one or more of the squares where a new figure is supposed to start is not empty. When the buttom row is completely filled the player will gain points and the row empties and the whole board will move down all of the figures in place one row.

The work will be divided by milestone, so each person will take on their own milestones. 
    
### Schedule 

#### Week 18

- Create a drawable grid:
    This will be used for drawing empty and filled squares of different colors by passing in a matrix will integer values 
    ranging from 0 to 7 where 1-7 are the colors of figures 1-7.

- Create class for figures, shapes and points:
    Each one of the seven figures will have a unique color and shape.
![](https://mindyourdecisions.com/blog/wp-content/uploads/2018/05/tetris-riddle-thumb-600.png)
    
