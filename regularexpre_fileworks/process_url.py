
from re import findall

f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\regularexpre_fileworks\\url_file.txt")

content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:
    
    print(url)
    