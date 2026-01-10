# # Python script for day 10
file = open("input.txt","r")
total = 0
buttons = []
displays = []
for line in file:
    line=line.strip()
    line=line.split()
    displays.append(line[0])
    wiring=line[1:len(line)-1]
    wiring=[eval(wire.replace(")",",)")) for wire in wiring ]
    buttons.append(wiring)
for i in range(len(displays)):
    queue=[(["." for j in range(len(displays[i])-2)],button,0) for button in buttons[i]]
    visited={queue[j][1]:[queue[j][0]] for j in range(len(buttons[i]))}
    while True:
        display,instructions,layer=queue.pop(0)
        for light in instructions:
            if display[light]==".":
                display[light]="#"
            elif display[light]=="#":
                display[light]="."
        layer+=1
        if display not in visited[instructions]:
            visited[instructions].append(display)
        if "".join(display)==displays[i][1:len(displays[i])-1]:
            total+=layer
            # print(total)
            break
        for button in buttons[i]:
            if display not in visited[button]:
                queue.append(([i for i in display],button,layer))
print(total)

#part 2
from z3 import *
file = open("input.txt","r")
total = 0
buttons = []
jolts = []
for line in file:
    line=line.strip()
    line=line.split()
    jolts.append(line[len(line)-1])
    wiring=line[1:len(line)-1]
    wiring=[eval(wire.replace(")",",)")) for wire in wiring ]
    buttons.append(wiring)
for i in range(len(jolts)):
    level=jolts[i].strip("{}").split(",")
    level=[int(i) for i in level]
    affects=[]
    for button in buttons[i]:
        placeholder=len(level)*[0]
        for num in button:
            placeholder[num]=1
        affects.append(placeholder)
    # print(affects)
    xs = [Int(f"x{i}") for i in range(len(buttons[i]))]
    opt=Optimize()
    for x in xs:
        opt.add(x>=0)
    for j in range(len(level)):
        coeffs=[affect[j] for affect in affects]
        # print(coeffs)
        # print(level[j])
        opt.add(Sum(c*x for c,x in zip(coeffs,xs))==level[j])
    opt.minimize(Sum(xs))
    if opt.check() == sat:
        m=opt.model()
        # print("Solution:")
        # for x in xs:
            # print(x,"=",m[x])
        # print("Sum =",sum(m[x].as_long() for x in xs))
        total+=sum(m[x].as_long() for x in xs)
print(total)
