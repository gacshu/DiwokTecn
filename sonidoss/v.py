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

while 1==1:
	rawString = arduino.readline().decode("utf-8")
	print(rawString)
	sonidos1 = (rawString.split(","))
	print(sonidos1)
	sonidos1 = int(sonidos1[0])

	if sonidos1 == 0:
		play(AudioSegment.from_file("C:\\Users\\Etopia\\Documents\\PyThon\\sonidoss\\hihat.mp3"))
	elif sonidos1 == 1:
		play(AudioSegment.from_file("C:\\Users\\Etopia\\Documents\\PyThon\\sonidoss\\kick.mp3"))
	elif sonidos1 == 2:
		play(AudioSegment.from_file("C:\\Users\\Etopia\\Documents\\PyThon\\sonidoss\\snare.mp3"))
	elif sonidos1 == 3:
		play(AudioSegment.from_file("C:\\Users\\Etopia\\Documents\\PyThon\\sonidoss\\hola.mp3"))
	elif sonidos1 == 4:
		play(AudioSegment.from_file("C:\\Users\\Etopia\\Documents\\PyThon\\sonidoss\\tom.mp3"))
	elif sonidos1 == 5:
		play(AudioSegment.from_file("C:\\Users\\Etopia\\Documents\\PyThon\\sonidoss\\conga.mp3"))
	time.sleep(0.5)


