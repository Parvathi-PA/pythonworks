
words_file_path="C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\word_files.txt"

palindrome_path="C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\palindrome_word.txt"

f_words_file=open(words_file_path,"r")

f_palindrome=open(palindrome_path,"w")

# for words in f_words_file:
    
#     words=words.rstrip("\n")
    
#     reversed_word=words[::-1]
    
#     if words==reversed_word:
        
#         f_palindrome.write(words + "\n")


#or 
        
        
def is_palindrome(words):
    
   reversed_word=words[::-1]
    
   return True if reversed_word==words else False

for words in f_words_file:
    
    words=words.rstrip("\n")
    
    if is_palindrome(words):
        
        f_palindrome.write(words+"\n")
        
        
        
        
        
        
        
        
        
        
        
        
        
f_palindrome.close()

f_words_file.close()

