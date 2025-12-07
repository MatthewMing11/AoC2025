# Python script for day 2
file = open("input.txt","r")
total = 0
ranges=file.read().split(",")
print(ranges)
for rng in ranges:
    fid,lid = rng.split("-")
    fid=int(fid)
    lid=int(lid)
    for i in range(fid,lid+1):
        num=str(i)
        if len(num)%2==0:
            if num[:len(num)//2]==num[len(num)//2:]:
                total+=i 
print(total)

#part 2
file = open("input.txt","r")
total = 0
ranges=file.read().split(",")
print(ranges)
for rng in ranges:
    fid,lid = rng.split("-")
    fid=int(fid)
    lid=int(lid)
    for i in range(fid,lid+1):
        num=str(i)
        subs=dict()
        for j in range(1,len(num)//2+1):
            if j*num.count(num[:j])==len(num):
                subs[num[:j]]=num.count(num[:j])
                if subs[num[:j]] >1:
                    break
        if len(subs)==0:
            continue
        maxsubs=max(subs,key=subs.get)
        # print(i)
        # print(subs)
        if subs[maxsubs]>1:
            total+=i 
print(total)
