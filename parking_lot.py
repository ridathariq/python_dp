r = int(input())
c = int(input())

arr = list(map(int, input().split()))

if len(arr) != r*c:
    print("INVALID INPUT") 
else:
    max = -1
    r_index = -1

    for i in range(r):
        r = arr[i * c : (i +1) *c]
        count = sum(r)
        if count > max:
            max = count
            r_index = i +1


    print(r_index)
