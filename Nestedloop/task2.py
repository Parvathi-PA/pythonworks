
student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,38,35],
    "anvin":[32,30,40]
}

#index=1 hari's average mark 

# index=int(input("enter the index:"))

# for i,element in enumerate(student_data):
    
#     # if i+1==index:
        
#         marks=student_data.get(element)
        
#         avg=sum(marks)/len(marks)
#         print(element,avg)
        
# students_avg={k:sum(v)/len(v) for k,v in student_data.items()}

# print(students_avg)

sourse_word="chicken"

targest_word="hen"
# character_count={}

# for ch in sourse_word:
#     if ch in character_count:
#         character_count[ch]+=1
#     else:
#         character_count[ch]=1
# print(character_count)
        
        
character_count={ch:sourse_word.count(ch) for ch in sourse_word}
is_kangaroo=True

for ch in targest_word:
    if ch in character_count and character_count.get(ch)>0:
        character_count[ch]-=1
    else:
        is_kangaroo=False
print(is_kangaroo)