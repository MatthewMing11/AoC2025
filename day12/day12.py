# Python script for day 12
file = open("input.txt","r")
total=0
phase1=True
shapes={}
index=0
#i cheated, i found the quick solution online(not code but hint)
for line in file:
    line=line.strip()
    if ":" in line and line[-1]!=":":
        phase1=False
    if phase1:
        if ":" in line:
            indy=int(line[:len(line)-1])
            shapes[indy]=0
            index=indy
        else:
            shapes[index]+=line.count("#")
    else:
        line=line.split()
        region=line[0].strip(":").split("x")
        arear=int(region[0])*int(region[1])
        presents=line[1:]
        areap = sum([shapes[i]*int(presents[i])for i in range(len(presents))])
        # print(arear)
        # print(areap)
        # print(arear==areap)
        if arear>=areap:
            total+=1
# print(shapes)
print(total)
