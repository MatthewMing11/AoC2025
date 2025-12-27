# Python script for day 5
file = open("input.txt","r")
total = 0
br=False
fresh=[]
for line in file:
    line=line.strip()
    if not br:
        if line=="":
            br=True
            continue
        frange=line.split("-")
        frange=[int(i) for i in frange]
        fresh.append(frange)
    else:
        for fr in fresh:
            if int(line)>=fr[0] and int(line)<=fr[1]:
                total+=1
                break
print(total)
        
#part 2
file = open("input.txt","r")
total = 0
fresh=[]
for line in file:
    line=line.strip()
    if line=="":
        break
    frange=line.split("-")
    frange=[int(i) for i in frange]
    fresh.append(frange)
fresh=sorted(fresh)
allfresh=[fresh[0]]
for i in range(1,len(fresh)):
    last=allfresh[-1]
    if last[1]>=fresh[i][0]:
        allfresh[-1]=[last[0],max(last[1],fresh[i][1])]
    else:
        allfresh.append(fresh[i])
for i in allfresh:
    total+=i[1]-i[0]+1
print(total)