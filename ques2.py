
arr=[3,5,7,9]
target = 8 
ln=len(arr)
for i in range(0,ln) :
    for j in range(i+1,ln):
        if i+j==target :
            print({i},{j})
            
        


            
