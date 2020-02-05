from pydub import AudioSegment
from pydub.playback import play
from easygui import *
import sys
import serial, time
import serial.tools.list_ports


pulgar = "C:\\Users\\Etopia\\Documents\\PyThon\\sonidoss\\hihat.mp3"

play(AudioSegment.from_file(pulgar))