# Python script for day 6
file = open("input.txt","r")
total = 0
operands=[]
for line in file:
    symbols=line.split()
    if symbols[0]=="+" or symbols[0]=="*":
        for i in range(len(symbols)):
            subtotal=0
            symbol=symbols[i]
            if symbol=="+":
                for operand in operands:
                    subtotal+=operand[i]
            elif symbol=="*":
                subtotal+=1
                for operand in operands:
                    subtotal*=operand[i]
            total+=subtotal
    else:
        symbols=[int(symbol) for symbol in symbols]
        operands.append(symbols)
print(total)

#part 2
file = open("input.txt","r")
total = 0
operands=[]
for line in file:
    symbols=line.split()
    if symbols[0]=="+" or symbols[0]=="*":
        start=0
        for i in range(len(symbols)):
            operandlist=[operand[i] for operand in operands]
            lenlist=[len(operand) for operand in operandlist]
            maxl=max(lenlist)
            file.seek(0)
            newoperandlist=[line[start:start+maxl] for line in file]
            newoperandlist.pop(-1)
            start=start+maxl+1
            newoperands=[]
            symbol=symbols[i]
            subtotal=0
            for j in range(maxl):
                num=""
                for operand in newoperandlist:
                    num+=operand[j]
                newoperands.append(int(num))
            newoperands=newoperands[::-1]
            if symbol=="+":
                for operand in newoperands:
                    subtotal+=operand
            elif symbol=="*":
                subtotal+=1
                for operand in newoperands:
                    subtotal*=operand
            total+=subtotal
    else:
        operands.append(symbols)
print(total)
