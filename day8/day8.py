# Python script for day 8
file = open("input.txt","r")
lines=file.readlines()
points=[lines[0].strip()]
dists={}
for line in lines[1:]:
    line=line.strip()
    for i in range(len(points)):
        point=line.split(",")
        point=[int(j) for j in point]
        refpoint=points[i].split(",")
        refpoint=[int(k) for k in refpoint]
        conn=str(i)+"-"+str(len(points))
        dists[conn]=sum([(refpoint[m]-point[m])**2 for m in range(3)])
    points.append(line)
used={}
circuits=[]
cranges=sorted(dists,key=dists.get)
for i in range(1000):
    curr=cranges[i].split("-")
    if curr[0] not in used and curr[1] not in used:
        used[curr[0]]=len(circuits)
        used[curr[1]]=len(circuits)
        circuits.append(curr)
    elif curr[0] in used and curr[1] not in used:
        used[curr[1]]=used[curr[0]]
        circuits[used[curr[0]]].append(curr[1])
    elif curr[1] in used and curr[0] not in used:
        used[curr[0]]=used[curr[1]]
        circuits[used[curr[1]]].append(curr[0])
    else:
        if used[curr[0]]!=used[curr[1]]:
            circuits[used[curr[0]]]+=circuits[used[curr[1]]]
            circuits[used[curr[0]]]=list(set(circuits[used[curr[0]]]))
            circuits.pop(used[curr[1]])
            for use in used:
                for j in range(len(circuits)):
                    if use in circuits[j]:
                        used[use]=j
                        break

circuits=sorted(circuits,key=len,reverse=True)
print(len(circuits[0])*len(circuits[1])*len(circuits[2]))

#part 2
file = open("input.txt","r")
lines=file.readlines()
points=[lines[0].strip()]
dists={}
for line in lines[1:]:
    line=line.strip()
    for i in range(len(points)):
        point=line.split(",")
        point=[int(j) for j in point]
        refpoint=points[i].split(",")
        refpoint=[int(k) for k in refpoint]
        conn=str(i)+"-"+str(len(points))
        dists[conn]=sum([(refpoint[m]-point[m])**2 for m in range(3)])
    points.append(line)
used={}
circuits=[]
cranges=sorted(dists,key=dists.get)
i=0
while True:
    curr=cranges[i].split("-")
    if curr[0] not in used and curr[1] not in used:
        used[curr[0]]=len(circuits)
        used[curr[1]]=len(circuits)
        circuits.append(curr)
    elif curr[0] in used and curr[1] not in used:
        used[curr[1]]=used[curr[0]]
        circuits[used[curr[0]]].append(curr[1])
    elif curr[1] in used and curr[0] not in used:
        used[curr[0]]=used[curr[1]]
        circuits[used[curr[1]]].append(curr[0])
    else:
        if used[curr[0]]!=used[curr[1]]:
            circuits[used[curr[0]]]+=circuits[used[curr[1]]]
            circuits[used[curr[0]]]=list(set(circuits[used[curr[0]]]))
            circuits.pop(used[curr[1]])
            for use in used:
                for j in range(len(circuits)):
                    if use in circuits[j]:
                        used[use]=j
                        break
    if len(max(circuits,key=len))==len(points):
        a=int(points[int(curr[0])].split(',')[0])
        b=int(points[int(curr[1])].split(',')[0])
        print(a*b)
        break
    i+=1