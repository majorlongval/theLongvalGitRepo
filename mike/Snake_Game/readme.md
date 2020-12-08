#### Notes on SnakeGame for Udemy 100 days of Python:
( https://www.udemy.com/course/100-days-of-code/learn/lecture/20356939#questions)
- Game starts automatically
- Game board border drawn in blue  
- Snake heading East (0)
- Snake length = 4 
- Snake color = white
- Collision with walls implemented
- Collision with self implemented (although
  there seems to be bugs, where collision
  does not register.)

#### Keyboard movement:
  - 'q' - Quits game
  - 'r' - Reset game
- left cursor - rotate left
- right cursor - rotate right 

#### To do:
- implement place_food()
- implement detect_collision_with_food()
- implement grow_snake()
- implement scoreboard()

#### Mechanism of game:
- snake is implemented a list of turtles.
- "movement" is accomplished by adding a 
  new turtle at one end and removing one at 
  the other.
- collisions are detected by comparing "head" of
snake position with positions of other parts 
  of snake. 
- collision with wall by checking position
of head with border (after new head added)
  

