
f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\names.txt","w")

languages=["python","java","c#","javascript"]

for l in languages:
    
    f.write(l + "\n")  # take only strings
    
f.close()


# text="hello world"

# f.write(text)

# f.close()