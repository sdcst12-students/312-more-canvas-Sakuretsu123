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
cd = 10
tl = 11
for i in range(len(data)):
    if data[i] == "\n":
        print("linebreak")
    else:
        print(i, i%tl, data[i])
        
        if data[i] == "0":
            cor.append( (i%tl, int(i/tl), 0))
            
        elif data[i] == "1":
            cor.append( (i%tl, int(i/tl), 1))
           
        elif data[i] == "2":
            cor.append( (i%tl, int(i/tl), 2))
            
        elif data[i] == "3":
            cor.append( (i%tl, int(i/tl), 3))
          
        elif data[i] == "4":
            cor.append( (i%tl, int(i/tl), 4))
          
        elif data[i] == "5":
            cor.append( (i%tl, int(i/tl), 5))
          
        elif data[i] == "6":
            cor.append( (i%tl, int(i/tl), 6))
         
    


    

print(cor)

for i in cor:
        if i == "linebreak": 
            print("othing")
        else: 
            if i[2] == 0:
                x1 = i[0]*30 +5
                y1 = i[1]*30 +5
                walls.append(c.create_image(x1,y1, image = water))
            if i[2] == 1:
                x1 = i[0]*30 + 5
                y1 = i[1]*30 + 5
                walls.append(c.create_image(x1,y1, image = plains))
            if i[2] == 2:
                x1 = i[0]*30 + 5
                y1 = i[1]*30 + 5
                walls.append( c.create_image(x1,y1, image = forest))
            if i[2] == 3:
                x1 = i[0]*30 + 5
                y1 = i[1]*30 + 5
                walls.append( c.create_image(x1,y1, image = hills))
            if i[2] == 4:
                x1 = i[0]*30 + 5
                y1 = i[1]*30 + 5
                walls.append( c.create_image(x1,y1, image = mountain))
            if i[2] == 5:
                x1 = i[0]*30 + 5
                y1 = i[1]*30 + 5 
                walls.append( c.create_image(x1,y1, image = swamp))
            if i[2] == 6:
                x1 = i[0]*30 + 5
                y1 = i[1]*30 + 5
                walls.append( c.create_image(x1,y1, image = city))

w.mainloop()