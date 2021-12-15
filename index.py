class Customer:
    def __init__(self,name,membership_type): #constructor or intitializer when a customer is created
        self.name=name
        self.membership_type=membership_type
        print("customer created")
    

    def update_membership(self,new_membership):
        self.membership_type=new_membership

    def __str__(self):
        print("Converting to string")
        return self.name+" "+self.membership_type
   # def print_all_customers(customers):
    #        for customer in customers:
     #           print(customer)
    def __eq__(self, other):
        if self.name==other.name and self.membership_type==other.membership_type:
            return True
        return False

    #__hash__=None
    #__repr_=__str__


#c=Customer("Lara","Gold")
#c2=Customer("Ruuh","Allo")

#print(c.name,c.membership_type)
#print(c2.name,c2.membership_type)

#list of customers
customers=[Customer("Lara","Diamond"), Customer("Ruuh","Platinum")]
#Customer.print_all_customers(customers)
print(customers[0]==customers[1])


data={customers[0]}


#updating customer membership_type
print(customers[1].membership_type)
customers[1].update_membership("Nutron")


print(customers[1].membership_type)
print(customers[0].name)

#Encapsulation
#Inheritence
#Polymorphisom
