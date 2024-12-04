
# def review(rating):
    
#     if rating <0:
        
#         raise Exception("too low!!")
    
#     elif rating>10:
        
#         raise Exception("too high !!")
    
#     else:
        
#         print("done!")
        
# try:    
        
#    review(87)
   
# except Exception as e:
    
#     print(e)
    
# print("haai")

# print("hello")




#or


def rating(review):
    
    assert rating>0,"tooo low"
    
    assert rating in range(0,11), "too high"
    
    print("rated")
    
rating(  )