import pygame
import sys
import time

pygame.init()
pygame.font.init()
pygame.mouse.set_visible(False)

size = (800, 700)

screen = pygame.display.set_mode(size)

#font = pygame.font.SysFont('Comic Sans MS', 30)
bgImg = pygame.image.load('images/bg.jpg')
bgImg = pygame.transform.scale(bgImg, (800, 700))

def print_item(filename, x, y):
  img = pygame.image.load(filename)
  #img = pygame.transform.scale(img, (800, 700))
  screen.blit(img, (x,y))

while True:
  screen.fill((0,0,0))
  screen.blit(bgImg, (0,0))
  print_item('weather/weather.png', 20, 20)

  #out_temp = file_get_contents('./out_temp.txt')
  #textsurface = font.render('Temp outside: ' + out_temp, False, (255, 255, 255))
  #screen.blit(textsurface,(30,30))

  pygame.display.flip()
  time.sleep(1)

