f = open("map1.txt")
data = f.read()

print(data)
walls = []
for i in range(len(data)):
    print(i, data[i], i%30, int(i/30))
    if data[i] == "*":
        walls.append( (i%30, int(i/30)))

print(walls)