class Customer:
    def __init__(self,name,membership_type): #constructor or intitializer when a customer is created
        self.name=name
        self.membership_type=membership_type
        print("customer created")

c=Customer("Lara","Gold")
c2=Customer("Ruuh","Allo")

print(c.name,c.membership_type)
print(c2.name,c2.membership_type)
