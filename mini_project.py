import turtle
list1=["red","blue","Khaki","purple","grey"]
def fig():
    window = turtle.Screen()
    window.bgcolor("Black")
    t=turtle.Turtle()
    
    for i in range(1,364):
         t.forward(100+i)
         t.right(90)
         t.speed(0)
         t.color(list1[i%5])
         t.right(1)
    window.exitonclick()
fig()
