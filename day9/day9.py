# Python script for day 9
file = open("input.txt","r")
largest = 0
tiles=[]
for line in file:
    curr=line.split(",")
    curr=[int(i) for i in curr]
    for tile in tiles:
        area = (abs(tile[0]-curr[0])+1)*(abs(tile[1]-curr[1])+1)
        largest=max(largest,area)
    tiles.append(curr)
print(largest)

#part 2
# Takes too long, but gets correct answer
# real	615m3.130s
# user	614m51.239s
# sys	0m2.178s
file = open("input.txt","r")
largest = 0
reds=[]
greens=[]
minR=1000000000
maxR=0
rows={}#only has border points
for line in file:
    curr=line.split(",")
    curr=[int(i) for i in curr]
    maxR=max(curr[1],maxR)
    minR=min(curr[1],minR)
    if curr[1] not in rows:
        rows[curr[1]]=[curr[0]]
    else:
        rows[curr[1]].append(curr[0])
    reds.append(curr)
for i in range(-1,len(reds)-1):
    if reds[i][0]==reds[i+1][0]:
        start=min(reds[i][1],reds[i+1][1])
        end=max(reds[i][1],reds[i+1][1])
        for j in range(start+1,end):
            greens.append([reds[i][0],j])
            if j not in rows:
                rows[j]=[reds[i][0]]
            else:
                rows[j].append(reds[i][0])
    else:
        if reds[i][1]==reds[i+1][1]:
            start=min(reds[i][0],reds[i+1][0])
            end=max(reds[i][0],reds[i+1][0])
            for j in range(start+1,end):
                greens.append([j,reds[i][1]])
                rows[reds[i][1]].append(j)
for row in rows:
    rows[row]=sorted(rows[row])
print(rows)
largest=0
recorded=[]
badpoints=[]
for i in range(len(reds)):
    for j in range(i+2,len(reds)):
        if i==0 and j==len(reds)-1:
            continue
        if (abs(reds[i][0]-reds[j][0])+1)*(abs(reds[i][1]-reds[j][1])+1) <largest:
            continue
        print("corners")
        print(reds[i])
        print(reds[j])
        tests=[]
        x1, y1 = reds[i]
        x2, y2 = reds[j]

        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)

        points = set()
        bad= False

        # Vertical edges
        for y in range(ymin, ymax + 1):
            if (xmin,y) in badpoints or (xmax,y) in badpoints:
                bad=True
                break
            points.add((xmin, y))
            points.add((xmax, y))
        if bad:
            continue
        # Horizontal edges
        for x in range(xmin, xmax + 1):
            if (x,ymin) in badpoints or (x,ymax) in badpoints:
                bad=True
                break
            points.add((x, ymin))
            points.add((x, ymax))
        if bad:
            continue
        tests=list(points)
        good=True
        for test in tests:
            if test[0] in rows[test[1]]:
                continue
            if test in recorded:
                continue
            nodesl=0
            nodesr=0
            left=[col for col in rows[test[1]] if col<test[0]]
            right=[col for col in rows[test[1]] if col>test[0]]
            if [left,right] in recorded:
                continue
            startnum=0
            start=False
            for k in left:
                if not start and k+1 in left:
                    start=True
                    startnum=k
                elif not start and k+1 not in left:
                    nodesl+=1
                elif start and k+1 not in left:
                    if test[1]-1 in rows and test[1]+1 in rows and ((startnum in rows[test[1]+1] and k in rows[test[1]-1]) or (startnum in rows[test[1]-1] and k in rows[test[1]+1])):
                        nodesl+=1
                    start=False 
            startnum=0
            start=False
            for k in right:
                if not start and k+1 in right:
                    start=True
                    startnum=k
                elif not start and k+1 not in right:
                    nodesr+=1
                elif start and k+1 not in right:
                    if test[1]-1 in rows and test[1]+1 in rows and  ((startnum in rows[test[1]+1] and k in rows[test[1]-1]) or (startnum in rows[test[1]-1] and k in rows[test[1]+1])):
                        nodesr+=1
                    start=False
            if nodesl==nodesr and nodesl%2==1:#checking for valid point and adding it
                # print("Here")
                # print(test[0],test[1])
                # rows[test[1]].append(test[0])
                recorded.append([left,right])
            else:
                good=False
                print("Bad point")
                print(test)
                print(nodesl)
                print(nodesr)
                badpoints.append(test)
                break
        if good:
            area = (abs(reds[i][0]-reds[j][0])+1)*(abs(reds[i][1]-reds[j][1])+1)
            largest=max(largest,area)
            print(largest)
print(largest)
