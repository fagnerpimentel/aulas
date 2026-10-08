# Gera images/mapa-ocupacao-ros.png: grade de ocupação construída por varredura laser simulada,
# com a convenção do map_saver do ROS (.pgm): 0 = ocupado, 254 = livre, 205 = desconhecido.
import math, random
from PIL import Image
random.seed(4)
RES=0.05                 # m/célula (padrão do TurtleBot3/Cartographer)
W,H=10.0,7.0             # planta em metros
MARG=0.8
NX,NY=int((W+2*MARG)/RES),int((H+2*MARG)/RES)
# paredes: segmentos (x1,y1,x2,y2) em metros, com portas (vãos)
walls=[(0,0,W,0),(W,0,W,H),(W,H,0,H),(0,H,0,0)]
# corredor horizontal em y=3.0..4.0, com salas em cima e embaixo
walls+= [(0,3.0,2.0,3.0),(2.8,3.0,6.2,3.0),(7.0,3.0,W,3.0),
         (0,4.0,1.2,4.0),(2.0,4.0,5.0,4.0),(5.8,4.0,8.6,4.0),(9.4,4.0,W,4.0),
         (3.4,0,3.4,1.8),(3.4,2.6,3.4,3.0),(6.6,0,6.6,1.8),(6.6,2.6,6.6,3.0),
         (3.0,4.0,3.0,5.4),(3.0,6.2,3.0,H),(6.4,4.0,6.4,5.4),(6.4,6.2,6.4,H)]
# móveis (caixas): retângulos como 4 segmentos
def box(x,y,w,h): return [(x,y,x+w,y),(x+w,y,x+w,y+h),(x+w,y+h,x,y+h),(x,y+h,x,y)]
for b in [(0.6,0.6,0.7,0.5),(4.4,1.0,0.6,0.9),(8.0,0.7,0.8,0.6),(1.0,5.0,0.8,0.8),(4.2,5.2,0.7,0.6),(7.6,5.4,0.9,0.7)]:
    walls+=box(*b)
def ray(x,y,a,rmax):
    dx,dy=math.cos(a),math.sin(a); best=rmax; hit=False
    for x1,y1,x2,y2 in walls:
        ex,ey=x2-x1,y2-y1; den=dx*ey-dy*ex
        if abs(den)<1e-9: continue
        t=((x1-x)*ey-(y1-y)*ex)/den; u=((x1-x)*dy-(y1-y)*dx)/den
        if t>0.02 and 0<=u<=1 and t<best: best=t; hit=True
    return best,hit
UNK,FREE,OCC=205,254,0
g=[[UNK]*NX for _ in range(NY)]       # g[j][i], j de baixo para cima
def cell(x,y): return int((x+MARG)/RES),int((y+MARG)/RES)
def mark_free(x0,y0,x1,y1):
    n=int(max(abs(x1-x0),abs(y1-y0))/RES*2)+1
    for k in range(n):
        x=x0+(x1-x0)*k/n; y=y0+(y1-y0)*k/n; i,j=cell(x,y)
        if 0<=i<NX and 0<=j<NY and g[j][i]!=OCC: g[j][i]=FREE
# trajetória do robô: corredor e entradas de algumas salas
path=[(0.6,3.5),(2.4,3.5),(4.0,3.5),(5.5,3.5),(7.4,3.5),(8.6,3.5),(7.4,3.5),(6.9,3.5),(6.9,2.2),(6.9,1.2),(6.9,2.2),(6.9,3.5),(5.4,3.5),(2.4,3.5),(2.4,4.6),(2.4,3.5)]
# interpola
poses=[]
for (x0,y0),(x1,y1) in zip(path,path[1:]):
    n=int(math.hypot(x1-x0,y1-y0)/0.25)+1
    for k in range(n): poses.append((x0+(x1-x0)*k/n,y0+(y1-y0)*k/n))
RMAX=3.0
for (px,py) in poses:
    for r in range(360):
        a=math.radians(r+random.uniform(-0.3,0.3))
        d,hit=ray(px,py,a,RMAX)
        d+=random.gauss(0,0.012)
        mark_free(px,py,px+(d-0.03)*math.cos(a),py+(d-0.03)*math.sin(a))
        if hit:
            i,j=cell(px+d*math.cos(a)+random.gauss(0,0.01),py+d*math.sin(a)+random.gauss(0,0.01))
            if 0<=i<NX and 0<=j<NY: g[j][i]=OCC
# imagem (origem em cima) e ampliação sem suavização
im=Image.new("L",(NX,NY))
im.putdata([g[NY-1-j][i] for j in range(NY) for i in range(NX)])
im=im.resize((NX*5,NY*5),Image.NEAREST)
im.save("images/mapa-ocupacao-ros.png")
print(NX,NY,"->",im.size)
