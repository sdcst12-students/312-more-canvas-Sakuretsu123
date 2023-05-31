import tkinter as tk

"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountains
5 Swamp
6 City
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map2.txt')

wimg = tk.PhotoImage(file="assets/charmander.png")
img = c.create_image(200,200,image=wimg)




water = tk.PhotoImage(file="assets/map.water.png")
plains= tk.PhotoImage(file="assets/map.plains.png")
forest = tk.PhotoImage(file="assets/map.forest.png")
hills = tk.PhotoImage(file="assets/map.hills.png")
mountain = tk.PhotoImage(file="assets/map.mountain.png")
swamp = tk.PhotoImage(file="assets/map.swamp.png")
city = tk.PhotoImage(file="assets/map.city.png")


data = f.read()
print(data)

cor = []
walls = []

for i in range(len(data)):
    print(i, data[i])
    if data[i] == "0":
        cor.append( (i%10, int(i/10), 0))
    if data[i] == "1":
        cor.append( (i%10, int(i/10), 1))
    if data[i] == "2":
        cor.append( (i%10, int(i/10),2))
    if data[i] == "3":
        cor.append( (i%10, int(i/10),3))
    if data[i] == "4":
        cor.append( (i%10, int(i/10),4))
    if data[i] == "5":
        cor.append( (i%10, int(i/10),5))
    if data[i] == "6":
        cor.append( (i%10, int(i/10),6))
print(cor)

for i in cor:
        if i[2] == 0:
            x1 = i[0]*30 + 5
            y1 = i[1]*30 + 5
            x2 = x1+30
            y2 = y1+30
            walls.append(c.create_image(x1,y1,x2,y2, image = water))
        if i[2] == 1:
            x1 = i[0]*30 + 5
            y1 = i[1]*30 + 5
            x2 = x1+30
            y2 = y1+30
            walls.append(c.create_image(x1,y1,x2,y2, image = plains))
        if i[3] == 2:
            x1 = i[0]*30 + 5
            y1 = i[1]*30 + 5
            x2 = x1+30
            y2 = y1+30
            walls.append( c.create_image(x1,y1,x2,y2, image = forest))
        if i[3] == 3:
            x1 = i[0]*30 + 5
            y1 = i[1]*30 + 5
            x2 = x1+30
            y2 = y1+30
            walls.append( c.create_image(x1,y1,x2,y2, image = hills))
        if i[3] == 4:
            x1 = i[0]*30 + 5
            y1 = i[1]*30 + 5
            x2 = x1+30
            y2 = y1+30
            walls.append( c.create_image(x1,y1,x2,y2, image = mountain))
        if i[3] == 5:
            x1 = i[0]*30 + 5
            y1 = i[1]*30 + 5
            x2 = x1+30
            y2 = y1+30
            walls.append( c.create_image(x1,y1,x2,y2, image = swamp))
        if i[3] == 6:
            x1 = i[0]*30 + 5
            y1 = i[1]*30 + 5
            x2 = x1+30
            y2 = y1+30
            walls.append( c.create_image(x1,y1,x2,y2, image = city))

w.mainloop()