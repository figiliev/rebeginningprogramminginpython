import turtle
import tkinter
import tkinter.messagebox
turtle.hideturtle()

target_hit=0  #Credit Counter to 60ish

#Screen Setup
def setup_turtle():
    screen = turtle.Screen()
    screen.title("Lets hit the classes and get Degreed")
    screen.bgcolor("lightgrey")
    t = turtle.Turtle()
    return screen,t
#move the arrow up
def move_on():
    t.forward(10)

def turn_left():
    t.left(30)

def turn_right():
    t.right(30)
    
    
#Named Constants
beginningProgrammingX= -310
beginningProgrammingY= 10

programmingCplusplusX= -300 #1613
programmingCplusplusY= 30

linearAlgebraX=-70#1613
linearAlgebraY=200

introToStatsX=80 #2103
introToStatsY=180

discreteStructureX=-140#1621
discreteStructureY=-120

fundamentalDataStructuresX=-226#2613
fundamentalDataStructuresY=-223

computerOrganizationArchitectureX=70#2621 
computerOrganizationArchitectureY=60

objectOrientedDesignPatternsX=-290#2833
objectOrientedDesignPatternsY=199

algorithmsAdvancedDataStructuresX=168#3103
algorithmsAdvancedDataStructuresY=-140

computerOrganizationArchitectureTwoX=-160#3621
computerOrganizationArchitectureTwoY=40

applicationsDatabaseManagementSystemsX= -100
applicationsDatabaseManagementSystemY=80

programmingLanguagesX=185  #or Translator Design(40234173))
programmingLanguagesY= 190

cyberSecurityX= -165#4083
cyberSecurityY= 290

operatingSystemsX= 10 #4153
operatingSystemsY= 15

theoryOfComputingX= 300 #4273
theoryOfComputingY=-178

cEX= 125 #4273
cEY= 150

softWareEngineeringOneX=-330 #4283
softWareEngineeringOneY=-265

ethicsInComputingX=-300 #4401
ethicsInComputingY=275

softwareDesignDevelopmentX=226 #4513
softWareDesignDevelopmentY=133  


#Function to draw the classes and the locations on the grid

def beginningProgramming():
    turtle.penup()
    turtle.goto(beginningProgrammingX,beginningProgrammingY)
    turtle.dot(10,"grey")
    turtle.write("We Start Here in Python")   
beginningProgramming()
    
def programmingCplusplus():
    turtle.penup()
    turtle.goto(programmingCplusplusX,programmingCplusplusY)
    turtle.dot(10,"green")
    turtle.write("We Go Here in next C++ welcome")

programmingCplusplus()
def linearAlgebra():
    turtle.penup()
    turtle.goto(linearAlgebraX,linearAlgebraY)
    turtle.dot(10,"yellow")
    turtle.write("Welcome to Linear Algebra you made it")

linearAlgebra()

def introToStats():
    turtle.penup()
    turtle.goto(introToStatsX,introToStatsY)
    turtle.dot(10,"blue")
    turtle.write("Welcome to intro to Statistics")
introToStats()

def discreteStructures():
    turtle.penup()
    turtle.goto(discreteStructureX,discreteStructureY)
    turtle.dot(10,"grey")
    turtle.write("Welcome to discrete structures")
discreteStructures()

def fundamentalDataStructures():
    turtle.goto(fundamentalDataStructuresX,fundamentalDataStructuresY)
    turtle.dot(10,"pink")
    turtle.write("Welcome to Fundamental Data Structures ")
fundamentalDataStructures()

def computerOrganizationalArchitecture():
    turtle.goto(computerOrganizationArchitectureX,computerOrganizationArchitectureY)
    turtle.dot(10,"purple")
    turtle.write("Welcome to Computer Organizational Architecture ")
computerOrganizationalArchitecture()

def oODP(): 
    turtle.goto(objectOrientedDesignPatternsX,objectOrientedDesignPatternsY)
    turtle.dot(10,"green")
    turtle.write("Welcome to Objected Oriented Design Patterns")
oODP()

def algorithmsAdvancedDataStruct():
    turtle.goto(algorithmsAdvancedDataStructuresX,algorithmsAdvancedDataStructuresY)
    turtle.dot(10,"red")
    turtle.write("Welcome to Algoriths and Advanced Data Structures")
algorithmsAdvancedDataStruct()

def computerOrganizationArchTwo():
    turtle.goto(computerOrganizationArchitectureTwoX,computerOrganizationArchitectureTwoY)
    turtle.dot(10,"orange")
    turtle.write("Welcome to Computer Organizations Architecture 2")
computerOrganizationalArchitecture()

def applicationsDatabaseManagementSystems():
    turtle.goto(applicationsDatabaseManagementSystemsX,applicationsDatabaseManagementSystemY)#4003
    turtle.dot(10,"violet")
    turtle.write("Welcome to Applications & Database Management Systems")
applicationsDatabaseManagementSystems()

def programmingLanguages():
    turtle.goto(programmingLanguagesX,programmingLanguagesY) 
    turtle.dot(10,"blue")
    turtle.write("Welcome to Programming Languages or Translator Design(40234173)")
programmingLanguages()

def cyberSecurity():
    turtle.goto(cyberSecurityX,cyberSecurityY)
    turtle.dot(10,"indigo")
    turtle.write("Welcome to Cybersecurity")
cyberSecurity()

def operatingSystems():
    turtle.goto(operatingSystemsX,operatingSystemsY)
    turtle.dot(10,"pink")
    turtle.write("Welcome to OS systems")
operatingSystems()

def theoryOfComputing():
    turtle.goto(theoryOfComputingX,theoryOfComputingY)
    turtle.dot(10,"green")
    turtle.write("Welcome to Theory of Computing")
theoryOfComputing()

def cE():
    turtle.goto(cEX,cEY)
    turtle.dot(10,"red")
    turtle.write("Welcome to c")
cE()

def softWareEngineeringOne():
    turtle.goto(softwareDesignDevelopmentX,softWareEngineeringOneY)
    turtle.dot(10,"blue")
    turtle.write("Welcome to Software Engineering I") 
softWareEngineeringOne()

def ethicsInComputing():
    turtle.goto(ethicsInComputingX,ethicsInComputingY)
    turtle.dot(10,"yellow")
    turtle.write("Welcome to Ethics in Computing ")
ethicsInComputing()

def softWareDesignDevelopment():
    turtle.goto(softwareDesignDevelopmentX,softWareDesignDevelopmentY)
    turtle.dot(10,"green")
    turtle.write("Welcome to Software Design and Development")
softWareDesignDevelopment()

#Defining a hit
#def beginningProgrammingHit():
  
def reset_drawing():
    t.clear()
    t.penup()
    t.goto(beginningProgrammingX,beginningProgrammingY)
    t.pendown()
#Run the Game
screen,t = setup_turtle()
screen.listen()
screen.onkey(move_on,"Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(reset_drawing, "space")

#hitting the target
def target_hit(x,y):
    
    pass
#Keeping the score
def scoring_turtle():
    pass

screen.mainloop()
turtle.done()

