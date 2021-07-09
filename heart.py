import turtle
import emoji

turtle.speed(3)
turtle.bgcolor("lightblue")
turtle.pensize(3)


def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
        
turtle.color("yellow", "red")  
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)

curve()

turtle.left(120)

curve()

turtle.forward(111.65)
turtle.end_fill()

def txt1():

	turtle.up()
	turtle.setpos(-70,88)
	turtle.down()
	turtle.color('black')
	turtle.write("13-18-41-08          Happy LoVe Anniversary :)", font=("Jokerman", 18, "bold"))
        
def txt2():

	turtle.up()
	turtle.setpos(-160,-68)
	turtle.down()
	turtle.color('black')
	turtle.write("import Marakka_Mudiyatha_Naal from brain   --> 21/07/____", font=("Jokerman", 18))

def txt3():

	turtle.up()
	turtle.setpos(-160,-118)
	turtle.down()
	turtle.color('black')
	turtle.write("import Non_Erasable_Memory from Heart      --> \U0001F60D", font=("Jokerman", 18))

def txt4():

	turtle.up()
	turtle.setpos(-160,-188)
	turtle.down()
	turtle.color('black')
	turtle.write("Love You Forever \U0001F970 \U0001F618 \U0001F617 \U0001F61A \U0001F619 ", font=("Matura MT Script Capitals", 22))
	

txt1()
txt2()
txt3()
txt4()
turtle.hideturtle()

turtle.done()

