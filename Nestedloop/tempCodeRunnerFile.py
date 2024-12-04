

size=int(input("enter teh size:"))

for row in range(1,size):
    
    for space in range(1,size-row):
        
        print(" ",end="")
        
    for col in range(1,row+1):
            
            print("* ",end="")
            
    print()