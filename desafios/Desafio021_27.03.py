import pygame
pygame.mixer.init()
pygame.mixer.music.load('can_t_hold_us.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
