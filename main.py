
class Item:
    pay_rate=0.8 #class attributes
    all=[]
    def __init__(self,name:str,price:float,quantity:float): #constructor 
        
        #Run validation to received objects
        assert price>=0 ,f"User input error price-{price} cannot be a negative" #to verify and check the correct value of an int output
        assert quantity>=0, f"User input error quantity:{quantity} cannot be a negative"
        
        #assigned self objects
        self.name=name #dynamic attribute assignment
        self.price=price
        self.quantity=quantity

        # Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price*self.quantity
    def apply_discount(self):
        self.price=self.price*  self.pay_rate #Item.pay_rate
item1=Item("Phone",10000,50)
item2=Item("Laptop",60000,10)
item3=Item("Monitor",100000,90)
item4=Item("GPU",300000,40)
item5=Item("CPU",60000,20)


print(Item.all)



item1.apply_discount() 

item2.pay_rate=0.7
item2.apply_discount()

print(item2.price)


#print(item1.calculate_total_price())
#print(item2.calculate_total_price())
#print(Item.__dict__)#all the attribute for class level
#print(item1.__dict__)#all the attribute used in instance level
