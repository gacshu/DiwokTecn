from pydub import AudioSegment
from pydub.playback import play
from easygui import *
import sys
import serial, time
import serial.tools.list_ports
comlist = serial.tools.list_ports.comports()
connected = []
for element in comlist:
    connected.append(element.device)
print("Connected COM ports: " + str(connected))

arduino = serial.Serial('COM3', 9600)
antonio = []
dedos = ["pulgar", "indice", "corazon", "anular", "meñique"]
pulgar, indice, corazon, anular, meñique = "", "", "", "", ""
dedos_v = [pulgar, indice, corazon, anular, meñique]
lista = []
rutas = []
names = []
probi = []
b = True
c = 0
f=open("sonidos.txt","r")
lineas=f.readlines()
print(lineas)
f.close()
def importar():
    concion = fileopenbox("Que sonido quieres importar?\nO Presiona <cancel> pa salir.")
    nombre = enterbox("¿Como se llama el sonido?")
    f=open("sonidos.txt","a")
    f.write(concion + "," + nombre + "\n")
    f.close()
    menu()

def rep():
	for n in range(1):
		b = False
		f=open("sonidos.txt","r")
		lista=f.readlines()
		print(lista)
		for linea in lista:
		    probi= linea.split(",")
		    names.append(probi[1])
		    rutas.append(probi[0])
		    print(names)
	for dedo in dedos:
	    msg ="Que sonido quieres para el " + dedo + "?\nO Presiona <cancel> pa salir."
	    title = dedo
	    
	    print("hoal")

	    for n in range(1):
	        choice = choicebox(msg, title, names)
	        if choice is None:
	            sys.exit(0)
	        choice = rutas[names.index(choice)]
	        choice = choice.replace("\n","")
	        antonio.append(choice)


	    	#play(cancion)
	print("dadad")

def menu():
    msg ="Que quieres hacer?\nO Presiona <cancel> pa salir."
    title = "Menu"
    choices = ["Importar", "Tocar"]
    choice = choicebox(msg, title, choices)
    if choice is None:
        sys.exit(0)
    elif choice == "Importar":
        importar()
    else:
        rep()


menu()


while 1==1:

	sonidos1 = arduino.readline().decode("utf-8")
	sonidos1 = sonidos1.replace("\r\n", "")

	print(sonidos1)
	a = (sonidos1.split(","))



	if a[1] == "0":
		print(antonio[0])
		play(AudioSegment.from_file(antonio[0]))
		
	elif a[1] == "1":
		print(antonio[1])
		play(AudioSegment.from_file(antonio[1]))
		
	elif a[1] == "2":
		print(antonio[2])
		play(AudioSegment.from_file(antonio[2]))
		
	elif a[1] == "3":
		print(antonio[3])
		play(AudioSegment.from_file(antonio[3B]))
		
	elif a[1] == "4":
		print(antonio[4])
		play(AudioSegment.from_file(antonio[4]))
		
	#time.sleep(0.5)
