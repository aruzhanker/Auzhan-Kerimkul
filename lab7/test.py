import pygame as pg
pg.init()


screen= pg.display.set_mode((550, 550))
pg.display.set_caption('GREAT DIANA$$$ GAME')
icon= pg.image.load('WKND/images/anime.png')
pg.display.set_icon(icon)

figure= pg.Surface((100,100))
figure.fill('white')
mnch= pg.image.load('WKND/images/uchiwa.flower.png')


done= True
while done:
    pg.display.update()
    '''screen.blit(figure, (0,0))
    screen.blit(figure, (300, 500))
    screen.blit(figure, (300,0))
    screen.blit(figure, (0, 500))
    screen.blit(figure, (100,100))
    screen.blit(figure, (200,200))
    screen.blit(figure, (100,300))
    screen.blit(figure, (200, 400))
    pg.draw.circle(figure, 'black', (50,50), 25)'''
    screen.blit(mnch, (10,10))
    

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            done = False

