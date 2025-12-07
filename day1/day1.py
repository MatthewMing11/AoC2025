# Python script for day 1
file = open("input.txt","r")
count = 0
num = 50
for line in file:
    ori,dist = line[0], int(line[1:])
    if ori=="L":
        num=(num-dist)%100
    elif ori=="R":
        num=(num+dist)%100
    if num==0:
        count+=1
print(count)

#part 2
file = open("input.txt","r")
count = 0
num = 50
for line in file:
    ori,dist = line[0], int(line[1:])
    old=num
    # print(line)
    if ori=="L":
        start=num-dist+1
        num=(num-dist)%100
        start=start+(-start%100)
        while start<old:
            count+=1
            start+=100
    elif ori=="R":
        start=num+dist-1
        num=(num+dist)%100
        start=start-(start%100)
        while start>old:
            count+=1
            start-=100
    if num==0:
        count+=1
print(count)