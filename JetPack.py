from tkinter import *

def Jetpack_on(event) :
    global gravity
    gravity = 100
    Can.move(Zombie1,0 ,-pas_1)
    Can.pack()
global gravity
gravity = 100

def Jetpack_off() :
    global gravity
    Can.move(Zombie1, 0 ,pas_1)
    if gravity >= 25 :
        gravity = gravity -2
    else :
        gravity = 25
    Can.after(gravity, Jetpack_off)
    personnage =PhotoImage(file = "ZombieJetpackoff.gif")
    Can.pack()



def zombie(x, y):

    x = 2.5 + marge + pas_1 * (x - 1)
    y = marge - 3 + pas_2 * (y - 1)

    return Can.create_image(x , y, image = personnage)

fen = Tk()
personnage = PhotoImage(file = "ZombieJetpackon.gif")
nb_de_cases = 75

speed = 100

marge = 2

cote_1 = 800
cote_2 = 1200


Can = Canvas( fen, bg = "white" , height = cote_1, width = cote_2 )

pas_1 = cote_1 / nb_de_cases
pas_2 = cote_2 / 8

#for i in range(0,nb_de_cases+1):
#    Can.create_line( 0, pas_1 * i + marge, cote_2 , pas_1 * i + marge, fill = 'white')  # Horizontales
#    Can.create_line(pas_2 + marge, cote_1 , pas_2 + marge, 0 , fill = 'white') # Verticales

fen.bind( "<space>" , Jetpack_on)
Can.after(100, Jetpack_off)

Zombie1 = zombie(pas_1 ,3)

Can.pack()

fen.mainloop()
