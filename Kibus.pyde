porcentaje=0 #Porcentaje de obstaculos
empezar=False
obs=False
per=False
perro=False
ok=False
x=-200
terminar=False
i=10
POS=[[-1,-1,-1]]
world =[[0]*20 for _ in range(0,20)]
persona_p=[0,0]
shiba_p=[0,0]
p_i=[0,0]
proximo_p=[0,0]
iter=0
def setup():
    obs=True
    cuadros=50
    size(1401,1500)
    fill(0,0,0)
    stroke(0,0,0)
    rect(0,0,1000,1500) #CANVAS
    fill(255,255,255)
    rect(1001,0,400,1500)#JUEGO
    stroke(255,255,255)
    for i in range(0,21): #LINEEEAS!
        line(cuadros*i,0,cuadros*i,1000)
        line(0,cuadros*i,1000,cuadros*i)
    fill(10,80,230)
    titulo()
    seleccionObstaculos()

def draw():
    #frameRate(20)
    global empezar,POS,shiba,iter,ok,terminar,perrero
    shiba=loadImage("shiba.png")
    shiba.resize(50,50)
    if empezar and ok:
        if iter<len(POS)-1:
            x=int(POS[iter][0])
            y=int(POS[iter][1])
            image(shiba,x*50,y*50)
            iter+=1            
            delay(300)
            ok=False
        else:
            if not terminar:
                win=loadImage("win.png")
                win.resize(200,200)
                image(win,1100,500)
                empezar=False
            else:
                fail=loadImage("fail.png")
                image(fail,1100,500,200,200)
        
    else:
        dogc.resize(50,50)
        x=int(POS[iter-1][0])
        y=int(POS[iter-1][1])
        z=int(POS[iter-1][2])
        fill(0,0,0)
        rect((x*50)+1,(y*50)+1,48,48)
        tint(255,150)
        if z==1: image(dogc,x*50,y*50)
        tint(255,180)
        if z==2: image(dogc,x*50,y*50)
        tint(255,200)
        if z==3: image(dogc,x*50,y*50)
        tint(255,220)
        if z==4: image(dogc,x*50,y*50)
        tint(255,250)
        if z==5: image(dogc,x*50,y*50)
        ok=True
        delay(300)
        
         
def titulo():
    f=createFont("AmericanTypewriter",20)
    textFont(f)
    text("PODRÁ EL SHIBITA LLEGAR A MI ",1020,50)
    text("SIN TOPARSE CON EL PERRERO?",1020,80)

def juego():
    if per: pos_per()
    
    
def seleccionObstaculos():
    global dogc
    f=createFont("ComicSans",15)
    textFont(f)
    fill(250,1,50)
    text("Nivel de obstaculos:",1010,200)
    dogc=loadImage("dogcatcher.png")
    dogc.resize(100,100)
    image(dogc,1010,220) #iconoperrero
    dibujarPorcentajes()
    
def dibujarPorcentajes(): #PORCENTAJE BARRA
    global obs,x
    fill(255,255,255)
    stroke(255,255,255)
    rect(1120,250,300,100)#Margenes
    fill(0,0,0)
    text("20%",1150,350)
    text("80%",1330,350)
    rect(1150,250,5,50)#Margenes
    rect(1330,250,5,50)
    rect(1155,275,175,5) #Linea central
   # BOTON OK
    stroke(0,0,0)
    fill(255,255,255)
    rect(1220,350,50,30,10)
    fill(32,32,0)
    text("OK",1230,370)
    obs=True
    
    
def mouseReleased():
    global porcentaje,obs,x
    if mouseX>=1150 and mouseX<=1330 and mouseY>=250 and mouseY<=300 and obs:
        dibujarPorcentajes()
        x=mouseX
        porc=(x-1150)*60/180
        porc=int(porc)+20
        fill(200,20,20)
        rect(x,250,5,50)
        text(str(porc)+"%",x,330)
        porcentaje=porc

def mousePressed():
    global porcentaje,obs,i,world,per,perro,persona_p,shiba_p,shiba,empezar,p_i,POS
    if mouseX>=1220 and mouseX<=1270 and mouseY>=350 and mouseY<=380 and obs:
        obs=False
        perreros()
    if mouseX>=0 and mouseX<=1000 and mouseY<=1000 and mouseY>=0:
        if perro:
            x=mouseX/50
            x=int(x)
            y=mouseY/50
            y=int(y)
            if world[x][y]!=5:
                perro=False
                shiba=loadImage("shiba.png")
                shiba.resize(50,50)
                image(shiba,x*50,y*50)
                
                stroke(255,255,255)
                fill(255,255,255)
                rect(1001,400,400,300)
                shiba_p=[x,y]
                p_i=shiba_p
                POS[0]=[p_i[0],p_i[1],0]
                ruta()
        if per:
            x=mouseX/50
            x=int(x)
            y=mouseY/50
            y=int(y)
            if world[x][y]!=5:
                per=False
                cr.resize(50,50)
                image(cr,x*50,y*50)
                stroke(255,255,255)
                fill(255,255,255)
                rect(1001,300,400,300)
                persona_p[0]=x
                persona_p[1]=y
                pos_perro()
                                

    
def perreros():
    global porcentaje,world,per
    dogc=loadImage("dogcatcher.png")
    dogc.resize(50,50)
    arr=[0]*400
    stroke(255,255,255)
    fill(255,255,255)
    rect(1001,150,400,300)
    can_por=porcentaje*4
    for _ in range (0,can_por):
        randomSeed(0)
        while True:
            k=int(random(400))
            if arr[k]==0:
                y=int(k/20)
                arr[k]=1
                x=k%20
                world[x][y]=5
                image(dogc,50*x,50*y)
                break
    pos_per()
    
                 
def pos_per():
    global per
    per=True
    global cr
    f=createFont("ComicSans",15)
    textFont(f)
    fill(250,1,50)
    cr=loadImage("cr.png")
    cr.resize(100,100)
    image(cr,1010,350)
    text("Destino de shibita",1010,330)
    
def pos_perro():
    global shibi,perro
    perro=True
    f=createFont("ComicSans",15)
    textFont(f)
    fill(250,1,50)
    shibi=loadImage("shibi.png")
    shibi.resize(100,100)
    image(shibi,1010,450)
    text("Shibita",1010,430)
        
def ruta():
    global p_i,empezar,persona_p,ok,terminar
    while p_i[0]!=persona_p[0] or p_i[1]!=persona_p[1]:
        bresenham(p_i[0],p_i[1],persona_p[0],persona_p[1])
        if p_i!=persona_p: cambio(p_i[0],p_i[1])
        if terminar: break
    empezar=True
    ok=True

def cambio(x,y):
    arr=[[None,None]]
    global world,p_i,proximo_p,POS,terminar
    l=len(POS)
    back=[POS[l-2][0],POS[l-2][1]]
    aux=[x+1,y+1]
    if aux!=back and x+1<20 and y+1<20 and proximo_p!=aux and world[x+1][y+1]!=5: arr.append(aux)
    aux=[x+1,y]
    if aux!=back and x+1<20 and proximo_p!=aux and world[x+1][y]!=5: arr.append(aux)
    aux=[x+1,y-1]
    if aux!=back and x+1<20 and y-1>=0 and proximo_p!=aux and world[x+1][y-1]!=5: arr.append(aux)
    aux=[x,y+1]
    if aux!=back and y+1<20 and proximo_p!=aux and world[x][y+1]!=5: arr.append(aux)
    aux=[x,y-1]
    if aux!=back and y-1>=0 and proximo_p!=aux and world[x][y-1]!=5: arr.append(aux)
    aux=[x-1,y+1]
    if aux!=back and x-1>=0 and y+1<20 and proximo_p!=aux and world[x-1][y+1]!=5: arr.append(aux)
    aux=[x-1,y]
    if aux!=back and x-1>=0 and proximo_p!=aux and world[x-1][y]!=5: arr.append(aux)
    aux=[x-1,y-1]
    if aux!=back and x-1>=0 and y-1>=0 and proximo_p!=aux and world[x-1][y-1]!=5: arr.append(aux)
    world[x][y]+=1
    POS[l-1][2]+=1
    arr.pop(0)
    l=len(arr)
    print(l)
    if l==0:
        #world[x][y]+=1
        p_i=back
        if world[back[0]][back[1]]==5:terminar=True
        print(world[x][y])
    else:
        randomSeed(0)
        ran=random(l)
        ran=int(ran)
        p_i[0]=arr[ran][0]
        p_i[1]=arr[ran][1]
        print("a")
        print(p_i[0],p_i[1])
        
def bresenham(x0,y0,x1,y1):
    if abs(x1-x0)>abs(y1-y0):
        if x1>=x0: b1(x0,y0,x1,y1)
        else:b2(x0,y0,x1,y1)
    else:
        if y1>=y0: b4(x0,y0,x1,y1)
        else: b3(x0,y0,x1,y1)
    
def b1(x0,y0,x1,y1): #X1>X0 
    global proximo_p,POS,p_i
    dx=x1-x0
    dy=y1-y0
    y=y0
    y_i=1
    if y0>y1:
        dy=-dy
        y_i=-1
    s=2*dy-dx

    for x in range(x0,x1+1):
        if world[x][y]==5:
            proximo_p=[x,y]
            print("aqui1")
            print(x,y)
            break
        p_i=[x,y]
        POS.append([x,y,world[x][y]])
        if s>0:
            s-=2*dx
            y+=y_i
        s+=2*dy

def b2(x0,y0,x1,y1): #X0>X1
    global proximo_p,POS,p_i
    dx=x0-x1
    dy=y1-y0
    y=y0
    y_i=1
    if y0>y1:
        dy=-dy
        y_i=-1
    s=2*dy-dx

    for x in range(x0,x1-1,-1):
        if world[x][y]==5:
            proximo_p=[x,y]
            print("aqui2")
            print(x,y)
            break
        p_i=[x,y]
        POS.append([x,y,world[x][y]])
        if s>0:
            s-=2*dx
            y+=y_i
        s+=2*dy
            

def b3(x0,y0,x1,y1): #Y1>Y0 
    global proximo_p,POS,p_i
    dx=x1-x0
    dy=y0-y1
    x=x0
    x_i=1
    if x0>x1:
        dx=-dx
        x_i=-1
    s=2*dx-dy

    for y in range(y0,y1-1,-1):
        if world[x][y]==5:
            proximo_p=[x,y]
            print("aqui3")
            print(x,y)
            break
        p_i=[x,y]
        POS.append([x,y,world[x][y]])
        if s>0:
            s-=2*dy
            x+=x_i
        s+=2*dx

def b4(x0,y0,x1,y1): #Y0>Y1
    global proximo_p,POS,p_i
    dx=x1-x0
    dy=y1-y0
    x=x0
    x_i=1
    if x0>x1:
        dx=-dx
        x_i=-1
    s=2*dx-dy
    for y in range(y0,y1+1):
        if world[x][y]==5:
            proximo_p=[x,y]
            print("aqui4")
            print(x,y)
            break
        p_i=[x,y]
        POS.append([x,y,world[x][y]])
        if s>0:
            s-=2*dy
            x+=x_i
        s+=2*dx
    

    
    
    
        

        
    
    
    
    
    
