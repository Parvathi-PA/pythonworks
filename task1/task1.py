

    
    
# nums=[-4,-2,1,4,8]

# closest=nums[0]

# for num in nums:

#     if abs(num)<abs(closest) or (abs(closest)==abs(num) and num>closest ):

#         closest=num

# print(closest)


#  Task2

# word1="abc"
# word2="pqrstgwm"

# merged_string=""

# for i in range(0,len(word1)):
    
#     merged_string+=word1[i]+word2[i]
    
# balanced_string=word2[len(word1):]

# merged_string+=balanced_string

# print(merged_string)





#task 3

# def roman_int(roman):
#     roman_dict={
#         "I" : 1,"V":5,"X":10,"L":50,"c":100,"D":500,"M":1000
#     }
    
#     n=0
#     pre_value=0
    
#     for char in reversed(roman):
#         current_value=roman_dict[char]
#         if current_value<pre_value:
#             n-=current_value
#         else:
#             n+=current_value
#             pre_value=current_value
#     return n
# print(roman_int("DDMXIV"))        



#task 4

# def is_subsequence(s,t):
#     s_index =0
#     t_index = 0
    
#     while s_index < len(s) and t_index < len(t):
#         if s[s_index] == t[t_index]:
#             s_index += 1
#         t_index += 1
    
#     return s_index == len(s)

# print(is_subsequence("abc","ahbgdc"))

#task 5

# prices=[7,1,5,3,6,4]

# min_price=prices[0]

# max_profit=0

# if not prices:
#     print(0)


# for price in prices:
    
#     min_price=min(min_price,price)
#     max_profit=max(max_profit,price-min_price)
    
    
# print(max_profit)




#task 6

# def common_prefix(string):
    
#     prefix=string[0]
    
    
#     for w in string[1:]:
        
#         while not w.startswith(prefix):
            
#             prefix=prefix[:-1]
            
#             if not prefix:
                
#                 return ""
            
#     return prefix
                
# string=["flower","flow","fly"]

# # string=["dog","cat","goat"]

# print(common_prefix(string))
            
       
       
# task 7

nums = [0, 1, 2, 4, 5, 7,9]
i = 0
result = []

while i < len(nums):
    begin = nums[i]
    while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
        i += 1
    end = nums[i]
    
    if begin == end:
        result.append(str(begin))
    else:
        result.append(str(begin) + "->" + str(end))
    
    i += 1

print(result)