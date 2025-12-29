# Python script for day 3
file = open("input.txt","r")
total = 0
for line in file:
    line=line.rstrip()
    batts=[]
    for i in range(len(line)):
        dig=line[i]
        if len(batts)<2:
            batts.append(dig)
        else:
            if int(batts[1])<int(dig):
                if int(batts[0])<int(batts[1]):
                    batts[0]=batts[1]
                    batts[1]=dig
                else:
                    batts[1]=dig
            else:
                if int(batts[0])<int(batts[1]):
                    batts[0]=batts[1]
                    batts[1]=dig
    total+=int("".join(batts))
print(total)

#part 2
file = open("input.txt","r")
total = 0
for line in file:
    line=line.rstrip()
    batts=[]
    for i in range(len(line)):
        dig=line[i]
        if len(batts)<12:
            batts.append(dig)
        else:
            move=False
            for j in range(11):
                if int(batts[j])<int(batts[j+1]):
                    move=True
                    for k in range(j,11):
                        batts[k]=batts[k+1]
                    break
            if move or int(batts[11])<int(line[i]):
                batts[11]=dig
    total+=int("".join(batts))
print(total)
