import turtle as t       #turtle 모듈을 불러온다
import random            #random 모듈을 불러온다
def right_wall():        #오른쪽에 튕겼을 때   
    ang=t.heading()       
    if ang<90:        
        t.lt(180-2*ang)
    else:        
        t.rt((180-ang)*2)

def left_wall():          #왼쪽에 튕겼을 때   
    ang=t.heading()
    if ang<180:       
        t.rt(2*(ang-90))
    else:        
        t.lt(2*(270-ang))

def top_wall():           #위쪽에 튕겼을 때    
    ang=t.heading()
    if ang<90:       
        t.rt(2*ang)
    else:        
        t.lt(2*(180-ang))

def bottom_wall():       #아래쪽에 튕겼을 때    
    ang=t.heading()
    if ang<270:       
        t.rt(2*ang)
    else:        
        t.lt(2*(360-ang))        
def make_r(x,y,d):       #상자 만드는 함수       
    t.up()       
    t.goto(x,y)      
    t.down()       
    for x in range(4):              
        t.fd(d)             
        t.lt(90)
t.pensize(5)make_r(-250,-250,500)     #상자 만들기
t.up()
t.home()
t.shape("turtle")
t.speed(0)
t.setheading(random.randint(0,360))      #거북이 방향 랜덤하게 지정
ang=t.towards(0,0)
d=500
for x in range(200):       #반복함수 통해 거북이가 움직이는 경로 지정    ang=t.heading()
    while True:
        t.fd(3)        
        x=t.xcor()       
        y=t.ycor()
        
        if y >= 250:           
            top_wall()           
            break
        
        if y <= -250:            
            bottom_wall()           
            break
            
        if x <= -250:  
            left_wall()           
            break
            
        if x >= 250:          
            right_wall()          
            break
