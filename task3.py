#!python3

# Find an image to use as a sprite from the Internet.
# Modify the image (flipping horizontally is a quick way to do that) so that you have
# a second, different image. Use the tkObject.after() method to animate it.
# Note: You can find sprite sheets or tile sheets on the internet to help you!

import tkinter as tk

w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()

tile = 0 

def animate(): 
    global tile
    global sprite
    ig = None
    tile +=1
    tile = tile%2
    if tile: 
        ig = win
    else: 
        ig = winb
    c.itemconfig(sprite,image=ig)
    w.after(200, animate)





win = tk.PhotoImage(file="assets/sp2.png")
winb = tk.PhotoImage(file="assets/sprite sheets.png")
sprite = c.create_image(200,200, image = win)



w.after(200, animate)

def keyPress(e):
    print(e)
    print(e.keycode, e.keysym, e.x, e.y)

    if e.keysym == "Up":
        x=0
        y=-5
        x0 = c.coords(sprite) 
        c.move(sprite,x,y)
    if e.keysym == "Down":
        x=0
        y=5
        x0 = c.coords(sprite)
        c.move(sprite,x,y)
    if e.keysym == "Left":
        x=-5
        y=0
        x0 = c.coords(sprite)
        c.move(sprite,x,y)
    if e.keysym == "Right":
        x=5
        y=0
        x0 = c.coords(sprite)
        c.move(sprite,x,y)
    

    
w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)


w.mainloop()