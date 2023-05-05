import pygame as pg
pg.init()
pg.mixer.music.load("D:/Futuro/Linguagens/Python/exercises_guana/curso_em_video/music.mp3")
pg.mixer.music.play()
input()
pg.event.wait()
pg.mixer.quit()