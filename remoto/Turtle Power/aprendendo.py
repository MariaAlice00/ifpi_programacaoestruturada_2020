from turtle import * # * significa importar tudo da biblioteca turtle
shape('turtle') # o que desenha se pareça com uma tartaruga, ex: arrow(seta), circle, square, triangle, classic
speed(8) # velocidade, de 1 (devagar) a 11 (rápido)

color('Purple')
pensize(7) 
right(90) # direita; left é esquerda; 90 graus
forward(100) # para frente; backward é para trás; 100 pixels
left(90)
forward(50)

color('Orange')
pensize(3)
penup() # tirar a caneta da tela
forward(50)
pendown() # colocar a caneta na tela novamente
forward(50)

done() # pronto