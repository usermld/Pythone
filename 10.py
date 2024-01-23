coins = [0, 0, 0, 1,]

count = 0
max_0 = 0
max_1 = 0

for i in coins:
    
    if i == 1:
        max_1 += 1
    
    if i == 0:
        max_0 += 1
        
for i in coins:
    if max_0 > max_1:
        if i == 1:
            count += 1
    if max_1 > max_0:
        if i == 0:
            count += 1
    if max_1 == max_0:
        if i == 0:
            count = max_0
            
        
print(count) 
