from math import *
with open("file1.txt", "r") as file:
    lines = file.readlines()
    centers = []
    for line in lines:
        numbers = line.split()
        a = int(numbers[0])
        b = int(numbers[1])
        centers.append([a,b])
with open("file2.txt", "r") as f:
    lines = f.readlines()
    points = []
    for line in lines:
        numbers = line.split()
        a = int(numbers[0])
        b = int(numbers[1])
        points.append([a,b])
for center, point in zip(centers, points):
    a = int(center[0])
    b = int(center[1])
    c = int(point[0])
    d = int(point[1])
    lenth = sqrt(((a-c)**2) + ((b-d)**2))
    if lenth==5:
        print(0)
    elif lenth>5:
        print(2)
    else:
        print(1)









