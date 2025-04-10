import turtle
import tkinter
import tkinter.messagebox

# ===Globals===
target_hit=0  #Credit Counter to 60ish
  
#===Course Data===
courses = [ 
    {"name":"beginningProgramming", "x": -310 ,"y": 10, "color": "grey"},#1621
    {"name":"C++ Programming", "x": -300 ,"y": 300, "color": "green"},#1613
    {"name":"Discrete Structures ", "x":-140 ,"y":-120 , "color": "purple"}, #2123
    {"name":"linear Algebra ", "x":-70 ,"y":200 , "color": "pink"}, #3143
    {"name":"intro To Statistics ", "x":80 ,"y":180 , "color": "blue"}, #2103
    {"name":"Fundamental Data Structures ", "x":-226 ,"y": -223, "color": "pink"},#2613
    {"name":"Computer Organizational Architecture ", "x":-70 ,"y": 60, "color": "purple"},#2621
    {"name":"Object Oriented Design Patterns ", "x":-290 ,"y":-199, "color": "green"}, #2833
    {"name":"Algorithms Advanced Data Structures ", "x": 168,"y":-140 , "color": "red"},#3103
    {"name":"Computer Organizational Architecture II ", "x":-160 ,"y": 40, "color": "orange"},#3621
    {"name":"Applications Database Management Systems ", "x":-100 ,"y": 80, "color": "violet"},
    {"name":"Programming Languages ", "x": 185 ,"y": 190, "color": "blue"},#or Translator Design(40234173))
    {"name":"Cyber Security ", "x": -165,"y": 290 , "color": "indigo"}, #4083
    {"name":"Operating Systems ", "x": 10 ,"y": 15 , "color": "pink"}, #4153
    {"name":"Theory of Computing  ", "x": 300,"y":-178 , "color": "green"},#4273
    {"name":"C", "x":125 ,"y":150 , "color": "red"},
    {"name":"SoftWare Engineering I", "x":330 ,"y":265 , "color": "blue"}, #4283
    {"name":"Ethics In Computing", "x":300 ,"y":275 , "color": "yellow"}, #4401
    {"name":"SoftWare Design and Development", "x":226 ,"y":133 , "color": "Pink"}, #4513]
]

# ===Turtle Setup ===
def setup_turtle():
    """Sets up the screen and returns the screen and main turtle."""
    screen = turtle.Screen()
    screen.title("Lets hit the classes and get Degreed")
    screen.bgcolor("lightgrey")
    player_turtle = turtle.Turtle()
    return screen,player_turtle

# ===Drawing===
def draw_courses(player_turtle):
    """Draws all course nodes on the screen."""
    for course in courses:
        player_turtle.penup()
        player_turtle.goto(course["x"], course["y"])
        player_turtle.dot(10, course ["color"])
        player_turtle.write(f"{course['name']}", font =("Arial",10,"normal"))

#===Score display===
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-350, 270)


def update_score():
    """Updates the score display with current credit count"""
    score_display.clear()
    score_display.write(f"Credits: {target_hit}", font =("Arial", 14, "bold"))
    
# ===Player Movement ===
    
def move_on():
    """Moves the turtle forward and checks for course hits"""
    player_turtle.forward(10)
    check_for_hit()  
     
def turn_left():
    player_turtle.left(30)

def turn_right():
    player_turtle.right(30)

def reset_drawing():
    """Clears the screen and resets the turtle to the start course"""
    player_turtle.clear()
    start_course = courses[0] #First Course as starting point
    player_turtle.penup()
    player_turtle.goto(start_course["x"],start_course["y"])
    player_turtle.pendown()
    draw_courses(player_turtle) #Redraw the course after clearing the dots
    update_score()
    
    # ===Collison Detection===
def check_for_hit():
    """Checks if the turtle has collided with a course node."""
    global target_hit
    pos = player_turtle.pos()
    for course in courses:
        if "hit" not in course and abs(pos[0] - course["x"]) < 15 and abs(pos[1] - course["y"]) < 15:
            course["hit"]= True
            print(f"Hit: {course['name']}")
            target_hit += 3  # example: 3 credits per hit
            update_score()
            
#Main Game Loop ===
screen,player_turtle = setup_turtle()
draw_courses(player_turtle)
update_score()

screen.listen()
screen.onkey(move_on,"Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(reset_drawing, "space")

screen.mainloop()

