#https://github.com/pndurette/gTTS
from gtts import gTTS
import pygame
import time, sys

sentence = input("Ingrese su texto:\n")
vowels = ["a", "e", "i", "o", "u","á", "é", "í", "ó", 
"ú","ü","A", "E", "I", "O", "U","Á", "É", "Í", "Ó", "Ú","Ü"]

for i in range(len(vowels)):
        sentence = sentence.replace(vowels[i], vowels[i] + "p" + vowels[i])
print(sentence)

tts = gTTS(text=sentence, lang='es-us')
#tts = gTTS(text=sentence, lang='es-us', slow='False')
tts.save("jeringoso.mp3")

pygame.mixer.init()
pygame.mixer.music.load("jeringoso.mp3")
print ("")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
	time.sleep(1)
print ("Chau!")

