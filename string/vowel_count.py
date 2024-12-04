

#print vowels count
#print consonants

text="abcdefghijklmnopqurstuvwxyz"

v_count=0

c_count=0

for ch in text:
    
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        
        v_count=v_count+1
        
    else:
        
        c_count=c_count+1
        
print("vowel count=",v_count)

print("consonents=",c_count)