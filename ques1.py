arr=[0,1,2,4]
ln=len(arr)
arr.sort()
idx=0
for i in arr:
    if i == idx :
        idx+=1

    else :
        print(idx)

# complexity = O(n)

