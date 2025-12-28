# Python script for day 7
file = open("input.txt","r")
total = 0
lines=file.readlines()
beams=[lines[0].index("S")]
for line in lines[1:]:
    line=line.strip()
    newbeams=[]
    for beam in beams:
        if line[beam]=="^":
            total+=1
            if beam-1 not in newbeams:
                newbeams.append(beam-1)
            if beam+1 not in newbeams:
                newbeams.append(beam+1)
        else:
            if beam not in newbeams:
                newbeams.append(beam)
    beams=newbeams
print(total)

#part 2
file = open("input.txt","r")
lines=file.readlines()
beams={lines[0].index("S"):1}
for line in lines[1:]:
    line=line.strip()
    newbeams={}
    for beam in beams:
        if line[beam]=="^":
            if beam-1 not in newbeams:
                newbeams[beam-1]=beams[beam]
            else:
                newbeams[beam-1]+=beams[beam]
            if beam+1 not in newbeams:
                newbeams[beam+1]=beams[beam]
            else:
                newbeams[beam+1]+=beams[beam]    
        else:
            if beam not in newbeams:
                newbeams[beam]=beams[beam]
            else:
                newbeams[beam]+=beams[beam]
    beams=newbeams
total=0
for beam in beams:
    total+=beams[beam]
print(total)