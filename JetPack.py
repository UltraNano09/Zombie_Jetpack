from tkinter import *

def Jetpack_on(event) :
    Can.move(Zombie1,0 ,-pas_1)
    Can.pack()

def Jetpack_off(event) :
    Can.move(Zombie1, 0 ,pas_1)

    Can.pack()


def pions(x, y, color):
    r = 15

    x = 2.5 + marge + pas_1 * (x - 1)
    y = marge - 3 + pas_2 * (y - 1)

    return Can.create_oval(x - r, y - r, x + r, y + r, fill = color ,outline = 'black')


def zombie(x, y):

    x = 2.5 + marge + pas_1 * (x - 1)
    y = marge - 3 + pas_2 * (y - 1)

    return Can.create_image(x , y, image = personnage)

fen = Tk()
personnage = PhotoImage(file = "ZombieJetpack.gif")
nb_de_cases = 75

marge = 2

cote_1 = 800
cote_2 = 1200


Can = Canvas(fen,bg="white", height = cote_1, width = cote_2)

pas_1 = cote_1 / nb_de_cases
pas_2 = cote_2 / 8

for i in range(0,nb_de_cases+1):
    Can.create_line( 0, pas_1 * i + marge, cote_2 , pas_1 * i + marge, fill = 'black')  # Horizontales
    Can.create_line(pas_2 + marge, cote_1 , pas_2 + marge, 0 , fill = 'black') # Verticales

fen.bind("<space>", Jetpack_on)
fen.bind("<KeyRelease>", Jetpack_off)



##Can.create_image(50 , 50, image = personnage)

##Pion_1 = pions(3,2, 'gold' )
Zombie1 = zombie(pas_1 ,3)

Can.pack()

fen.mainloop()
