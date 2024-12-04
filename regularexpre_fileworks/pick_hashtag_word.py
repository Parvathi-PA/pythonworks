from re import finditer

f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\regularexpre_fileworks\\hashtag_file.txt")

for line in f:
    
    # line=line.rstrip("\n")
    
    # words=line.split(" ")
    
    # # for w in words:
    
    # pattern="(#)[a-zA-Z]"
    
    # for w in words:
        
    #  matcher=finditer(pattern,w)
       
    # if matcher!=None:
           
    #        print(w)
    
    
    words=line.rstrip("\n")
    
    pattern="#\w+"
    
    matcher=finditer(pattern,words)
    
    for obj in matcher:
        
        print(obj.group())       
       