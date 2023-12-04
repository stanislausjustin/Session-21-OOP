class Food:

    def __init__(self, name, amount):
        self.__name = name
        self.__amount = amount
        self.__sprice = 0
        self.__cprice = 0
        self.__PriceListSJ ()
        self.__calcCostSJ ()


    def __PriceListSJ(self):
        if self.__name is 'Dry Cured Iberian Ham':
            self.__sprice = 177.80
        elif self.__name is 'Wagyu Steaks':
            self.__sprice = 450.00
        elif self.__name is 'Matsutake Mushrooms':
            self.__sprice = 272.00
        elif self.__name is 'Kopi Luwak Coffee':
            self.__sprice = 306.50
        elif self.__name is 'Moose Cheese':
            self.__sprice = 487.20
        elif self.__name is 'White Truffles':
            self.__sprice = 3600.00
        elif self.__name is 'Blue Fin Tuna':
            self.__sprice = 3603.00
        elif self.__name is 'Le Bonnotte Potatoes':
            self.__sprice = 270.81
        else:
            print("Invalid, try again dumbass")
    
    def __calcCostSJ(self):
        self.__cprice = self.__amount * self.__sprice
        return self.__cprice
    
    def __str__(self):
        return f"The total cost for {self.__amount} pounds of {self.__name} is {self.c_price}" 
            






