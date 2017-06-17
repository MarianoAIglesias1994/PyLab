#https://github.com/pndurette/gTTS
from gtts import gTTS
import pygame
import time, sys

sentence = input("Ingrese su texto:\n")

tts = gTTS(text=sentence, lang='es-us')
tts.save("asistente.mp3")

pygame.mixer.init()
pygame.mixer.music.load("asistente.mp3")
print ("")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
	time.sleep(1)
print ("Chau!")