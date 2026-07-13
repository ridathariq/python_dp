m = int(input().strip())
e = int(input().strip())

powers = list(map(int,input().split()))
bonuses = list(map(int,input().split()))    

monsters = list(zip(powers, bonuses))
monsters.sort(key=lambda x: x[0])

count = 0
exp = e


for power, bonus in (monsters):
    if exp >= power:
        exp += bonus
        count +=  1
    else:
        break
print(count)