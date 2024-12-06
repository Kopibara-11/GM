from pygame import*

w=500
h=800

screen=display.set_mode((w,h))

background=transform.scale(image.load("НАЗВА КАРТИНКИ"), (w,h))

screen.fill((0,0,0))

clock=time.Clock()

run=True
while run:
    for e in event.get():
        if e.type==QUIT:
            run=False
        
    screen.blit(background,(0,0))
        
    clock.tick(60)
    display.update()