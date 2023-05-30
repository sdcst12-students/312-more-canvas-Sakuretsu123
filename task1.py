import tkinter as tk
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map1.txt')

rec = c.create_rectangle(50,50,80,80)
f = open("map1.txt")
data = f.read()

print(data)
cor = []
walls = []
for i in range(len(data)):
    print(i, data[i], i%30, int(i/30))
    if data[i] == "*":
        cor.append( (i%30, int(i/30)))
for i in cor:
    x1 = i[0]*30 + 5
    y1 = i[1]*30 + 5
    x2 = x1+30
    y2 = y1+30
    walls.append( c.create_rectangle(x1,y1,x2,y2,fill="#aa00aa"))
'''

-1,3,4,6,7,8,12,13,14,16,17,18,19,20,21,23,24,25,27,29
-1,6,7,8,10,11,12,16,23,24,27,29
-1 to 8, 10,11,12,14,15,16,18,19,20,21,22,23,26,27,29
-1,5,14,18,25,26,29
-1,3,7 to 14, 16 to 25,27,28,29
-1,3,4,5,6,9,16,17,22,23,28,29
-1,6,7,9,11,12,13,14,15,16,19,20,25,26,29
-1,2,3,4,9,11,12, 18 to 29
-1, 6,7,8,9,14,16
-1 to 29
'''


def keyPress(e):
    print(e)
    print(e.keycode, e.keysym, e.x, e.y)


    if e.keysym == "Up":
        x=0
        y=-5
        x0 = c.coords(rec)
        if x0[1] > 5 :  
            c.move(rec,x,y)
    if e.keysym == "Down":
        x=0
        y=5
        x0 = c.coords(rec)
        if x0[3] < 470 : 
            c.move(rec,x,y)
    if e.keysym == "Left":
        x=-5
        y=0
        x0 = c.coords(rec)
        if x0[0] > 5 :
            c.move(rec,x,y)
    if e.keysym == "Right":
        x=5
        y=0
        x0 = c.coords(rec)
        if x0[2] < 900: 
            c.move(rec,x,y)
    

    
w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)

w.mainloop()