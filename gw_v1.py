import pygame, os, random
from PIL import Image


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (80,50)

# init
pygame.init()
size = (1640, 1000)  # window size W x H
screen = pygame.display.set_mode(size)
background = pygame.image.load("imgs/background.jpg") 
font = pygame.font.SysFont(None, 75)
my_color = (71, 40, 21)
width = 139
height = 220

# load images
backside = pygame.image.load("cards/back.png")
iandy =  pygame.image.load("cards/andy.png")
iangela =  pygame.image.load("cards/angela.png")
icreed =  pygame.image.load("cards/creed.png")
idarryl =  pygame.image.load("cards/darryl.png")
idwight =  pygame.image.load("cards/dwight.png")
ierin =  pygame.image.load("cards/erin.png")
igabe =  pygame.image.load("cards/gabe.png")
iholy =  pygame.image.load("cards/holy.png")
ijan =  pygame.image.load("cards/jan.png")
ijim =  pygame.image.load("cards/jim.png")
ikaren =  pygame.image.load("cards/karen.png")
ikelly =  pygame.image.load("cards/kelly.png")
ikevin =  pygame.image.load("cards/kevin.png")
imere =  pygame.image.load("cards/meredith.png")
imich =  pygame.image.load("cards/michael.png")
imose =  pygame.image.load("cards/mose.png")
inellie =  pygame.image.load("cards/nellie.png")
ioscar =  pygame.image.load("cards/oscar.png")
ipam =  pygame.image.load("cards/pam.png")
iphyllis =  pygame.image.load("cards/phyllis.png")
iroy =  pygame.image.load("cards/roy.png")
iryan =  pygame.image.load("cards/roy.png")
istanley =  pygame.image.load("cards/stanley.png")
itoby =  pygame.image.load("cards/toby.png")
playing =  pygame.image.load("cards/back.png")

# character class
class person:
    def __init__(self, name, img, nm):
        self.id = nm
        self.img = img
        self.name = name
        self.clicked = False
        self.tmp = backside
        # position = positions[self.id]

# character array
xspacer = 20
yspacer = 20
inity = 30

theoffice = [person("kevin", ikevin, 0), person("angela", iangela, 1), person("holy", iholy, 2), person("darryl", idarryl, 3), person("jan", ijan, 4), person("mose", imose, 5),
             person("toby", itoby, 6), person("meredith", imere, 7), person("oscar", ioscar, 8), person("andy", iandy, 9), person("karen", ikaren, 10), person("ryan", iryan, 11),
             person("pam", ipam, 12), person("kelly", ikelly, 13), person("gabe", igabe, 14), person("roy", iroy, 15), person("creed", icreed, 16), person("erin", ierin, 17),
             person("jim", ijim, 18), person("michael", imich, 19), person("phyllis", iphyllis, 20), person("nellie", inellie, 21), person("stanley", istanley, 22), person("dwight", idwight, 23)]

positions = [(xspacer,inity),(width+2*xspacer, inity), (2*width+3*xspacer, inity), (3*width+4*xspacer, inity), (4*width+5*xspacer, inity), (5*width+6*xspacer, inity),
             (xspacer,height+yspacer+inity),(width+2*xspacer, height+yspacer+inity), (2*width+3*xspacer, height+yspacer+inity), (3*width+4*xspacer, height+yspacer+inity), (4*width+5*xspacer, height+yspacer+inity), (5*width+6*xspacer, height+yspacer+inity),
             (xspacer,2*height+2*yspacer+inity),(width+2*xspacer, 2*height+2*yspacer+inity), (2*width+3*xspacer, 2*height+2*yspacer+inity), (3*width+4*xspacer, 2*height+2*yspacer+inity), (4*width+5*xspacer, 2*height+2*yspacer+inity), (5*width+6*xspacer, 2*height+2*yspacer+inity),
             (xspacer,3*height+3*yspacer+inity),(width+2*xspacer, 3*height+3*yspacer+inity), (2*width+3*xspacer, 3*height+3*yspacer+inity), (3*width+4*xspacer, 3*height+3*yspacer+inity), (4*width+5*xspacer, 3*height+3*yspacer+inity), (5*width+6*xspacer, 3*height+3*yspacer+inity)]

def getcard():
    global playing
    num = random.randint(0, 23)
    s = "cards/"+theoffice[num].name+".png"
    c = Image.open(s)

    base_width = 350
    wpercent = (base_width / float(c.size[0]))
    hsize = int((float(c.size[1]) * float(wpercent)))
    c = c.resize((base_width, hsize), Image.Resampling.LANCZOS)

    mode = c.mode
    size = c.size
    data = c.tobytes()
    playing = pygame.image.fromstring(data, size, mode)

running = True
select = False
while running:
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    # set background
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    # set cards
    for idx, i in enumerate(theoffice):
        screen.blit(i.img, positions[idx])
    # select playing card
    if not select:
        getcard()
        select = True

    txt = font.render("You are:", True, (0,0,255))
    screen.blit(txt, (1220, 190))
    screen.blit(playing, (1150, 250))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.time.wait(100)
        for indx, (w, h) in enumerate(positions):
            # check mouse in columns
            if (w <= mouse[0] <= w+width) and (h <= mouse[1] <= h+height):
                if not theoffice[indx].clicked:
                    theoffice[indx].tmp = theoffice[indx].img 
                    theoffice[indx].img = backside
                    theoffice[indx].clicked = True
                else:
                    theoffice[indx].img = theoffice[indx].tmp
                    theoffice[indx].clicked = False