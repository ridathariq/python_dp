s = input("Enter String: " )


def subseq(string, current = "", index = 0):
    if index == len(string):
        if current != "":
            print(current)
        return
    
    subseq(string, current= current + string[index], index = index + 1)
    subseq(string, current , index = index + 1)

  
subseq(s)
     