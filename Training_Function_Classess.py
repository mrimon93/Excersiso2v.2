#Becoming Expert in Github and Function and Clasess
#https://www.youtube.com/watch?v=Ej_02ICOIgs
# Learning about objecting Programming
#https://www.youtube.com/watch?v=JeznW_7DlB0



print("Time for Training Function and Classess With Python and GitHub")


class Item:
    pay_rate = 0.8 #Class attribute
    #Defining the parameters accoring to the output i want
    def __init__(self,name: str, price: floar, quantity=0): #Magic Method 14.28 Min
        #Run validations to the recieved arguments
        #Don't want to be negative number or less then 0

        #Using assert as commant

        assert price >=0, f"price {price} is not valid"
        assert quantity >=0




        #Inserting the Value
        self.name = name
        self.age = age
        self.quantity = quantity
    def calculate_total_price(self,x,y):
        return x * y

item1 = Item("phone",112)
item1.name = "Phone"
item1.price = 100
item1.quantity = 5


#Printing value by using Method from Return and the values inputted in Item 1
print(item1.name,item1.age)