porcentaje=0 #Porcentaje de obstaculos
empezar=False
obs=False
per=False
perro=False
x=-200
i=10
POS=[[None,None,None]]
anterior_p=[0,0]
world =[[0]*20 for _ in range(0,20)]
persona_p=[0,0]
shiba_p=[0,0]
p_i=[0,0]
proximo_p=[0,0]
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
    global empezar,shiba_p,persona_p,POS
    if empezar:
        for i in POS:print(i)
        empezar=False
         
def titulo():
    f=createFont("AmericanTypewriter",20)
    textFont(f)
    text("PODRA EL SHIBITA LLEGAR A MI ",1020,50)
    text("A MI SIN TOPARSE CON EL PERRERO?",1020,80)

def juego():
    if per: pos_per()
    
    
def seleccionObstaculos():
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
    global porcentaje,obs,i,world,per,perro,persona_p,shiba_p,shiba,empezar,p_i
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
                shiba_p[0]=x
                shiba_p[1]=y
                p_i=shiba_p
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
    
def bresenham(x0,y0,x1,y1):
    if abs(y1-y0)<abs(x1-x0):
        if x0>x1:lineaAbajo(x1, y1, x0, y0)
        else:lineaAbajo(x0, y0, x1, y1)
    else:
        if y0>y1:lineaArriba(x1, y1, x0, y0)
        else: lineaArriba(x0, y0, x1, y1)

def lineaArriba(x0,y0,x1,y1):
    global world,shiba,POS,p_i,anterior_p,proximo_p
    dx=x1-x0
    dy=y1-y0
    x_i=1
    if dx<0:
        x_i=-1
        dx=-dx
    s=2*dx-dy
    x=x0
    anterior_x=x0
    anterior_y=y0
    for y in range(y0,y1):
        if world[x][y]!=5:
     #       image(shiba,50*x,50*y)
        else: 
            proximo_p=[x,y]
            break
        p_i[0]=x
        p_i[1]=y
        POS.append([p_i[0],p_i[1],world[x][y]])
        anterior_p=p_i
        if s>0:
            x+=x_i
            s-=2*dy
        s+=2*dx
  
  
def lineaAbajo(x0,y0,x1,y1):
    global world,shiba,POS,p_i,anterior_p,proximo_p
    dx=x1-x0
    dy=y1-y0
    y_i=1
    if dy<0:
        y_i=-1
        dy=-dy
    s=2*dy-dx
    y=y0
    anterior_x=x0
    anterior_y=y0
    for x in range(x0,x1):
        if world[x][y]!=5:
            image(shiba,50*x,50*y)
         #   print("aqui")
        else: 
            proximo_p=[x,y]
            break
        p_i[0]=x
        p_i[1]=y
        POS.append([p_i[0],p_i[1],world[x][y]])
        anterior_p=p_i 
        if s>0:
            y+=y_i
            s-=2*dx
        s+=2*dy
        
def ruta():
    global p_i,empezar,persona_p
    #while p_i[0]!=persona_p[0] or p_i[1]!=persona_p[1]:
    bresenham(p_i[0],p_i[1],persona_p[0],persona_p[1])
    cambio(p_i[0],p_i[1])

def cambio(x,y):
    arr=[[None,None]]
    global anterior_p,world,p_i
    aux=[None,None]
    aux=[x+1,y+1]
    if aux!=anterior_p and x+1<20 and y+1<20 and proximo_p!=aux and world[x+1][y+1]!=5: arr.append(aux)
    aux=[x+1,y]
    if aux!=anterior_p and x+1<20 and proximo_p!=aux and world[x+1][y]!=5: arr.append(aux)
    aux=[x+1,y-1]
    if aux!=anterior_p and x+1<20 and y-1>=0 and proximo_p!=aux and world[x+1][y-1]!=5: arr.append(aux)
    aux=[x,y+1]
    if aux!=anterior_p and y+1<20 and proximo_p!=aux and world[x][y+1]!=5: arr.append(aux)
    aux=[x,y-1]
    if aux!=anterior_p  and y-1>=0 and proximo_p!=aux and world[x][y-1]!=5: arr.append(aux)
    aux=[x-1,y+1]
    if aux!=anterior_p and x-1>=0 and y+1<20 and proximo_p!=aux and world[x-1][y+1]!=5: arr.append(aux)
    aux=[x-1,y]
    if aux!=anterior_p and x-1>=0 and proximo_p!=aux and world[x-1][y]!=5: arr.append(aux)
    aux=[x-1,y-1]
    if aux!=anterior_p and x-1<20 and y-1>=0 and proximo_p!=aux and world[x-1][y-1]!=5: arr.append(aux)
    
    l=len(arr)
    for i in arr: (i)
    if l==0:
        world[x][y]+=1
        p_i=anterior_p
    else:
        randomSeed(0)
        ran=random(l)
        ran=int(ran)
        p_i[0]=arr[ran][0]
        p_i[1]=arr[ran][1]
        
    
    
    
    
    
    
        

        
    
    
    
    
    
