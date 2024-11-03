import pgzrun,random
from time import time
TITLE="Connecting Satellites"
HEIGHT=600
WIDTH=800

satellites=[]
linecor=[]

numberofsatellites=15
countsatellites=0
starttime=0
totaltime=0
def createsatellites():
    global starttime
    for i in range(0,15):
        satellite=Actor("satellite")
        satellite.pos=random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
        satellites.append(satellite)
    
    starttime=time()
def draw():
    global starttime,totaltime
    screen.blit("space",(0,0))
    number=1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+30))
        number+=1
    for line in linecor:
        screen.draw.line(line[0],line[1],"white")
    if countsatellites < numberofsatellites:
        totaltime=time()-starttime
        screen.draw.text(str(round(totaltime)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(totaltime)),(10,10),fontsize=30)

def on_mouse_down(pos):
    global countsatellites,linecor,satellites,numberofsatellites
    if countsatellites < numberofsatellites:
        if satellites[countsatellites].collidepoint(pos):
            if countsatellites:
                linecor.append((satellites[countsatellites-1].pos,satellites[countsatellites].pos))
            countsatellites+=1
        else:
            linecor=[]
            countsatellites=0
                     

def update():
    pass
createsatellites()
pgzrun.go()