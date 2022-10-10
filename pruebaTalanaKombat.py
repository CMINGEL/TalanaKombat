from time import sleep
import json

##------------Iniciales---------------------------------------------------
Stallone_especiales={'DSD+P':[3,'Taladoken'],'SD+K':[2,'Remuyuken'],'P':[1,'Puño'],'K':[1,'Patada']}
Shuatseneguer_especiales={'SA+K':[3,'Remuyuquen'],'ASA+P':[2,'Taladoken'],'P':[1,'Puño'],'K':['Patada']}
movimientos_generales={'D':'Avanza','A':'retrocede','W':'se levanta','S':'se agacha','P':[1,'Puño'],'K':[1,'Patada']}


def nombreAtaque(jugador,movimiento,golpe):
    '''Devuelve narracion y vida que pierde oponente'''

    if jugador=='Stallone':
        print("entro Stallone")
        try:
            variable=(Stallone_especiales[movimiento+'+'+golpe])
        except:
            
            try:
                variable=movimientos_generales[golpe]
            except:
                variable=[0,'']
        finally:
            
            return variable
        
    if jugador=='Shuatseneguer':
        print("entro Shuatseneguer")
        try:
            variable=(Shuatseneguer_especiales[movimiento+'+'+golpe])
        except:
            
            try:
                variable=movimientos_generales[golpe]
            except:
                variable=[0,'']
        finally:
            
            return variable

def quienInicia(Stallone_movimientos,Stallone_golpes,Shuatseneguer_movimientos,Shuatseneguer_golpes):
    movimientos_Stallone=0
    movimientos_Shuatseneguer=0
    golpes_Stallone=0
    golpes_Shuatseneguer=0

    for x in Stallone_movimientos:
        movimientos_Stallone+=len(x)
    for x in Stallone_golpes:
        golpes_Stallone+=len(x)

    for x in Shuatseneguer_movimientos:
        movimientos_Shuatseneguer+=len(x)
    for x in Stallone_golpes:
        golpes_Shuatseneguer+=len(x)

    if (movimientos_Shuatseneguer+golpes_Shuatseneguer)==(movimientos_Stallone+golpes_Stallone):
        print("empate golpes + movimientos")
        if(movimientos_Shuatseneguer==movimientos_Stallone):
            print("empate movimientos")
            if(golpes_Shuatseneguer==golpes_Stallone):
                print("empate golpes")
                return ('Stallone')
            elif(golpes_Shuatseneguer>golpes_Stallone):
                return ('Stallone')
            else:
                return ('Shuatseneguer')

        elif(movimientos_Shuatseneguer>movimientos_Stallone):
            return("Stallone")
        else:
            return("Shuatseneguer")


    elif((movimientos_Shuatseneguer+golpes_Shuatseneguer)>(movimientos_Stallone+golpes_Stallone)):
        return("Stallone")
    else:
        return("Shuatseneguer")

def combate(batalla):
   
    Stallone=jugador("Stallone", batalla["player1"]["movimientos"],batalla["player1"]["golpes"])
    Shuatseneguer=jugador("Shuatseneguer", batalla["player2"]["movimientos"],batalla["player2"]["golpes"])
    #print(Shuatseneguer.status())
    #print(Stallone.status())
    bandera=False
    inicia=quienInicia(Stallone.movimientos,Stallone.golpes,Shuatseneguer.movimientos,Shuatseneguer.golpes)
    movimientoStallone=0
    movimientosShuatseneguer=0
    movimientoActual=0
    narracion=[]

    if inicia=='Stallone':
        ataque=nombreAtaque('Stallone',Stallone.movimientos[movimientoStallone],Stallone.golpes[movimientoStallone])
        Shuatseneguer.vida-=ataque[0]
        movimientoStallone+=1
        narracion.append('Inicia Stallone: {} a su opente Shuatseneguer, perdiendo {} puntos de vida'.format(ataque[1],ataque[0]) )

    if inicia=='Shuatseneguer':
        ataque=nombreAtaque('Shuatseneguer',Shuatseneguer.movimientos[movimientosShuatseneguer],Shuatseneguer.golpes[movimientosShuatseneguer])
        Stallone.vida-=ataque[0]
        movimientosShuatseneguer+=1
        narracion.append('Inicia Shuatseneguer: {} a su opente Stallone, perdiendo {} puntos de vida'.format(ataque[1],ataque[0])) 

    while bandera == False:
        if movimientoActual == movimientoStallone:
            ataque=nombreAtaque('Stallone',Stallone.movimientos[movimientoStallone],Stallone.golpes[movimientoStallone])
            movimientoStallone+=1
            Shuatseneguer.vida-=ataque[0]
            if ataque[1]=='':
                narracion.append('Juega Stallone: no ofrece daño a su oponente')
            else:
                narracion.append('Juega Stallone: {} a su opente Shuatseneguer, perdiendo {} puntos de vida'.format(ataque[1],ataque[0]) )
            

            if Stallone.vida<=0:
                bandera=True
                narracion.append('Gana Shuatseneguer y aun le quedan {} puntos de vida'.format(Shuatseneguer.vida))
                break


        if movimientoActual == movimientosShuatseneguer:
            ataque=nombreAtaque('Shuatseneguer',Shuatseneguer.movimientos[movimientosShuatseneguer],Shuatseneguer.golpes[movimientosShuatseneguer])
            Stallone.vida-=ataque[0]
            movimientosShuatseneguer+=1
            if ataque[1]=='':
                narracion.append('Juega Shuatseneguer: no ofrece daño a su oponente')
            else:
                narracion.append('Juega Shuatseneguer: {} a su opente Stallone, perdiendo {} puntos de vida'.format(ataque[1],ataque[0]))
            if Shuatseneguer.vida<=0:
                bandera=True
                narracion.append('Gana Stallone y aun le quedan {} puntos de vida.'.format( Stallone.vida))
                break


        movimientoActual+=1

    print(narracion)
    return narracion

##------------Clase jugador---------------------------------------------------
class jugador:
    def __init__(self,nombre,movimientos,golpes):
        self.vida=6
        self.nombre = nombre
        self.movimientos=movimientos
        self.golpes=golpes

    def status(self):
        print(self.nombre)
        print(self.vida)
        print(self.golpes)
        print(self.movimientos)
#----------------------------------------------------------------------------------------------

try:
    info = json.loads(input())
    context=combate(info)
except:
    context=["Error en la carga de la batalla, por favor intenta cargar un json valido"]


for x in context:
    print (x)