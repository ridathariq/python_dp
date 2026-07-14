r = int(input())
unit = int(input())
n = int(input())

arr = list(map(int, input().split()))  

if arr is None or r <= 0 or unit <= 0 or n <= 0:
    print(-1)  
    
else:
    r_count = r * unit
    t_food = 0
    t_house = 0
    
    for food in arr:
        t_food += food
        t_house += 1
        
        if t_food > r_count:
            print(t_house)
            break
    else:        
        print(0) # Number of rats