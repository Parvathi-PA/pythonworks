
year=int(input("enter year:"))

def is_leapyear(year):
    
    if year<0:
        return False
    
    if year%4==0 and year%100!=0 or year%100==0 and year%400==0:
        
        return True
    else:
        
        return False
    

def test_leapyear():
    
     assert is_leapyear(2024)==True,"non centuary year chk failed"
     
     assert is_leapyear(2025)==False,"invalid centuary year chk failed"
     
     assert is_leapyear(2000)==True,"centuary year chk failed"
     
     assert is_leapyear(1900)==False," inValid centuary year chk failed"
     
     assert is_leapyear(-2022)==False,"invalid year chk failed"
     
try:
    
    test_leapyear()
    
    print("test passed")
    
except Exception as e:
    
    print("failded",e)