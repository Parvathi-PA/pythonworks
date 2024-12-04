

# orders=["tea","coffie","tea","coffie","gheeroast","plainroast","porotta","tea"]

# orders_summary={} #create empty dictionary

# for item in orders: #take each items in orders
    
#     if item in orders_summary: #condition check
       
#        orders_summary[item]+=1
       
#     else:
        
#         orders_summary[item]=1
        
# print(orders_summary)




#character count

text="ABBCCB"

# count={}

# for ch in text:
    
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)

#firt recursive character

repeat={}
for ch in text:
    
    if ch in repeat:
        
        print(ch)
        
        break
        
    else:
        
        repeat[ch]=1
        