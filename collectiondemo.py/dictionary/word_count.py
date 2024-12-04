

words=["hello","hai","hello","hai","hai"]

# word_count={}

# for w in words:
#     if w in word_count:
        
#         word_count[w]+=1
#     else:
        
#         word_count[w]=1

word_count={w:words.count(w) for w in words }
        
print(word_count)

recursive_word=[k for k,v in word_count.items() if v>1 ]

print(recursive_word)

#display non recursive words

non_recursive=[k for k,v in word_count.items() if v==1 ]

print(non_recursive)

text="AABBBCCgCDmDDD"

charecter_count={ ch:text.count(ch) for ch in text }
print(charecter_count)

for k,v in charecter_count.items():
    if v==1:
        print(k)

non_recursive={ k for k,v in charecter_count.items() if v==1}
print(non_recursive)

