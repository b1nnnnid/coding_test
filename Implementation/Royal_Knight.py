now = input()
# nowy = ['a','b','c','d','e','f','g','h']
xindex = int(now[1])
yindex = int(ord(now[0])) - int(ord('a')) + 1
# yindex = 0

# for y in nowy:
#     yindex += 1
#     if now[0] == y:
#         break
        
count = 0
steps = [(-2, -1), (-1, -2), (2, -1), (1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1)]

for step in steps:
    nextx = xindex + step[0]
    nexty = yindex + step[1]
    
    if (nextx > 0 and nextx < 8) and (nexty > 0 and nexty < 8):
        count+=1
        
print(count)