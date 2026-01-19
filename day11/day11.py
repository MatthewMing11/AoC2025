# Python script for day 11
file = open("input.txt","r")
devices={}
for line in file:
    line=line.strip()
    line=line.split()
    device=line[0][:len(line[0])-1]
    devices[device]=line[1:]
paths=[]
queue=[["you"]]
while len(queue)!=0:
    curr=queue.pop(0)
    if curr[-1]=="out":
        paths.append([i for i in curr])
    else:
        device=devices[curr[-1]]
        for output in device:
            if output not in curr:
                queue.append(curr+[output])
print(len(paths))

#part 2
file = open("input.txt","r")
devices={}
for line in file:
    line=line.strip()
    line=line.split()
    device=line[0][:len(line[0])-1]
    devices[device]=line[1:]
paths=[]
# left,middle,right=0,0,0
# queue=[["fft"]]
# while len(queue)!=0:
#     curr=queue.pop(0)
#     if curr[-1]=="fft":
#         # if "dac" in curr and "fft" in curr:
#         #     print(curr)
#         paths.append([i for i in curr])
#     else:
#         device=devices[curr[-1]]
#         for output in device:
#             if output not in curr:
#                 queue.append(curr+[output])
# print(len(paths))
# queue=["svr"]
# count={queue[0]:1}
# visited=[]
# while queue:
#     curr=queue.pop()
#     visited.append(curr)
#     if curr=="fft":
#         # if "dac" in curr and "fft" in curr:
#         print(curr)
#         continue
#     elif curr=="dac" or curr=="out":
#         continue
#     else:
#         device=devices[curr]
#         for output in device:
#             if output not in visited:
#                 queue.append(output)
#                 if output not in count:
#                     count[output]=count[curr]
#                 else:
#                     count[output]+=count[curr]
# print("Done")
# print(count["fft"])
# left=count["fft"]

# queue=["fft"]
# count={queue[0]:1}
# visited=[]
# while queue:
#     curr=queue.pop()
#     visited.append(curr)
#     if curr=="dac":
#         # if "dac" in curr and "fft" in curr:
#         print(curr)
#         continue
#     elif curr=="out":
#         continue
#     else:
#         device=devices[curr]
#         for output in device:
#             if output not in visited:
#                 queue.append(output)
#                 if output not in count:
#                     count[output]=count[curr]
#                 else:
#                     count[output]+=count[curr]
# print("Done")
# print(count["dac"])
# middle=count["dac"]

# queue=["dac"]
# count={queue[0]:1}
# visited=[]
# while queue:
#     curr=queue.pop()
#     visited.append(curr)
#     if curr=="out":
#         # if "dac" in curr and "fft" in curr:
#         print(curr)
#         continue
#     elif curr=="fft":
#         continue
#     else:
#         device=devices[curr]
#         for output in device:
#             if output not in visited:
#                 queue.append(output)
#                 if output not in count:
#                     count[output]=count[curr]
#                 else:
#                     count[output]+=count[curr]

# print("Done")
# print(count["out"])
# right=count["out"]
# print(left*middle*right)
#cheated for this
from functools import lru_cache
# cache={}
@lru_cache(maxsize = None)
def dfs(node,met_dac,met_fft):
    # key = (node,met_dac,met_fft)
    # if key in cache:
    #     return cache[key]
    # total=0
    # for device in devices[node]:
    #     # print(device)
    #     met_dac=met_dac or (device=="dac")
    #     met_fft=met_fft or (device=="fft")
    #     if device=="out":
    #         if met_dac and met_fft:
    #             total+=1
    #     else:
    #         total+=dfs(device,met_dac,met_fft)
    # cache[device]=total
    # # print(device,total)
    # return total
    if node=="fft":
        met_fft= True
    if node=="dac":
        met_dac=True
    if node =="out":
        return 1 if (met_dac and met_fft) else 0
    total=0
    for device in devices[node]:
        total+=dfs(device,met_dac,met_fft)
    return total
tot=dfs("svr",False,False)
print(tot)