arr=[1,5,9,3,4,1]
ln=len(arr)
freq={}
for i in arr:
    if i in freq :
        freq[i]+=1
    else:
        freq[i]=1
for j in freq:
    if freq[j]>1:
        print(True)
        break
    else:
        print(False)

        
        