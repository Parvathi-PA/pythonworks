

# source_char="silent"

# targest_char="listen"

# is_anagram=True

# for ch in source_char:
    
#     if ch in targest_char:
        
#         is_anagram=False
        
# print(is_anagram)


source_char="silent"

targest_char="listen"

is_anagram=True

for ch in source_char:
    
     if ch not in targest_char:
         
         is_anagram=False
         
         break
     
print(is_anagram)
         
         
        