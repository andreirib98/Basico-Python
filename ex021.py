import pygame

# Tocar sons no python
pygame.init()
pygame.mixer.music.load('som_py.mp3')
pygame.mixer.music.play()
pygame.event.wait()