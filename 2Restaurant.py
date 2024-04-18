class MenuItem: #Clase base
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    #Setter name
    def set_name(self, new_name):
        self.__name = new_name

    #Getter name
    def get_name(self):
        return self.__name
    
    #Setter price
    def set_price(self, new_price):
        self.__price = new_price

    #Getter price
    def get_price(self):
        return self.__price
    
class Beverage(MenuItem):#Subclase
    def __init__(self, name, price, alcohol, temperature):
        super().__init__(name, price)#Llamando atributos de la clase base
        self.__alcohol = alcohol
        self.__temperature = temperature

    #Setter alcohol
    def set_alcohol(self, new_alcohol):
        self.__alcohol = new_alcohol

    #Getter alcohol
    def get_alcohol(self):
        return self.__alcohol
    
    #Setter temperature
    def set_temperature(self, new_temperature):
        self.__temperature = new_temperature

    #Getter temperature
    def get_temperature(self):
        return self.__temperature
    
class MainCourse(MenuItem):#Subclase
    def __init__(self, name, price, vegetarian, spicy):
        super().__init__(name, price)#Llamando atributos de la clase base
        self.__vegetarian = vegetarian
        self.__spicy = spicy

    #Setter vegetarian
    def set_vegetarian(self, new_vegetarian):
        self.__vegetarian = new_vegetarian
    
    #Getter vegetarian
    def get_vegetarian(self):
        return self.__vegetarian
    
    #Setter spicy
    def set_spicy(self, new_spicy):
        self.__spicy = new_spicy
    
    #Getter spicy
    def get_spicy(self):
        return self.__spicy
    
class Dessert(MenuItem):#Subclase
    def __init__(self, name, price, peanuts, vegan):
        super().__init__(name, price)#Llamando atributos de la clase base
        self.__peanuts = peanuts
        self.__vegan = vegan

    #Setter peanuts
    def set_peanuts(self, new_peanuts):
        self.__peanuts = new_peanuts
    
    #Getter peanuts
    def get_peanuts(self):
        return self.__peanuts
    
    #Setter vegan
    def set_vegan(self, new_vegan):
        self.__vegan = new_vegan
    
    #Getter vegan
    def get_vegan(self):
        return self.__vegan

class Order:
    def __init__(self, order_list: list = []):
        self.order_list = order_list

    def add_items(self, new_items_list: list = []):
        x = 0
        while x<len(new_items_list):
            self.order_list.append(new_items_list[x])#The new items are added to the original order list
            x+=1

    def calculate_total_price(self):
        x = 0
        sum = 0 #The variable is for adding all the prices of the items that are in order_list
        while x<len(self.order_list):
            sum+=self.order_list[x].get_price()
            x+=1
        if self.order_list.count(beer)>=3:#There is a discount for the beers: buy 3, get 1 free
            beer_count = self.order_list.count(beer)
            beer_discount = (beer_count//3)
            sum-=(beer.get_price()*beer_discount)
        print("The total price is $" +str(sum)) 
    
class Payment:#Clase base
    def __init__(self):
        pass

    def pay(self, price):#Se define el método para pagar
        pass

class Tarjeta(Payment):#Subclase
    def __init__(self, card_number, cvv):
        super().__init__()#Llamando atributos de la clase base
        self.card_number = card_number
        self.cvv = cvv
    
    def pay(self, price):#Polimorfismo
        print("Paying " + str(price)+" with credit card.")

class Cash(Payment):#Subclase
    def __init__(self, given_cash:float):
        super().__init__()#Llamando atributos de la clase base
        self.given_cash = given_cash

    def pay(self, price:float):#Polimorfismo
        if self.given_cash>price:
            print("Cash payment accepted. Change: $" + str(self.given_cash-price))
        elif price>self.given_cash:
            print("Cash payment denied. There are missing: $"+ str(price-self.given_cash))
        else:
            print("Cash payment accepted. There is no change.")

beer = Beverage("Beer", 10.000, "Alcoholic", "Cold" )
water = Beverage("Bottle of water", 6.500, "Non-alcoholic", "Room temperature" )
soda = Beverage("Coca-Cola", 6.000,"Non-alcoholic", "Cold" )
coffee = Beverage("Cappuccino", 6.100, "Non-alcoholic", "Hot" )
salad = MainCourse("Caesar salad", 23.000, "Non-vegetarian", "Non-spicy" )
lasagna = MainCourse("Lasagna", 25.000, "Vegetarian", "Non-spicy")
tacos = MainCourse("Chicken Tacos", 20.000, "Non-vegetarian", "Spicy")
waffle = Dessert("Nutella waffles", 15.000, "Contains peanuts", "Non-vegan" )
iceCream = Dessert("Lemon ice cream", 5.000, "Without peanuts", "Vegan" )
tiramisu = Dessert("Tiramisu", 12.000, "Without peanuts", "Non-vegan")


order = Order([waffle, salad, beer])
order.calculate_total_price()
order.add_items([beer, lasagna, tacos, beer, iceCream])
order.calculate_total_price()

paying_order = Cash(200)
paying_order.pay(103) 