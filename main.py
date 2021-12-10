class Item:
    def __init__(self,name): #constructor 
        print(f"New instance name is :{name}")
        self.name=name #dynamic attribute assignment
    def calculate_total_price(self,x,y):
        return x*y

item1=Item("Phone")
#item1.name="Phone"
item1.price=1000
item1.quantity=50



item2=Item("Laptop")
#item2.name="Laptop"
item2.price=10000
item2.quantity=3



