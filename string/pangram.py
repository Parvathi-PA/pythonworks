
text="The quick blown fox jumps over the lazcy dog"

alpha_sequ=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","u","r","s","t","u","v","w","x","y","z")

is_pangram=True

for ch  in alpha_sequ:
    
    if ch not in text:
        
        is_pangram=False
        
        break
        
print(is_pangram)