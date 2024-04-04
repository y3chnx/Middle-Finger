#법규 그리고 Fuck You! 출력하기
import turtle as t

# 창 설정
win = t.Screen()
win.title("fuck fuck fuck fuck fuck fuck fuck")
win.bgcolor("white")

# 거북이 속도 설정
t.speed(1) 

# 손 본체 그리기
t.penup()
t.goto(0, -100)
t.pendown()
t.fillcolor("#FBCEB1") 
t.begin_fill()
t.circle(100)  
t.end_fill()

# 손가락 그리기
t.penup()
t.goto(-50, -85)  
t.setheading(90) 
t.pendown()
t.fillcolor("#FBCEB1")
t.begin_fill()
for _ in range(1):
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(300)
t.end_fill()

#손톱 만들기
t.penup()
t.goto(-50, 150)
t.pendown()
t.left(45)
t.forward(70)
t.left(90)
t.forward(70)
t.left(45)
t.fillcolor("#87CEEB")
t.begin_fill()
t.forward(80)
t.left(90)
t.forward(100)
t.left(90)
t.forward(80)
t.end_fill()
t.penup()

#Fuck You! 출력하기
t.goto(0, -200)
t.write("Fuck You!" , True , font = ("comic sans" , 50 , "bold"))
t.done()

# 창 유지
win.mainloop()
