class Bank:
    
    accno:int
    
    balance:int
    
    ac_type:str
    
    customer_name:str
    
    def __init__(self,accno,balance,ac_type,customer_name):
        
        self.accno=accno
        
        self.balance=balance
        
        self.ac_type=ac_type
        
        customer_name=customer_name
        
    def deposit(self,amount):
        
        self.balance+=amount
        
        print(f"yor account {self.accno} has been created with amount {amount} avl balance {self.balance}")
        
    def withdraw(self,amount):
        
        if self.balance<amount:
            
           print("insufficient amount")
           
        else: 
            
            self.balance-=amount
        
            print(f"your account {self.accno} has been debited with {amount} avl balance {self.balance}")
        
        
    def get_balance(self):
        
        print("your avl balance",self.balance)
        
bank_instance1=Bank("ac635",45000,"saving","anu")

bank_instance1.deposit(1000)
bank_instance1.withdraw(46000)
bank_instance1.get_balance()