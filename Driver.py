from Class import Food

def CreateListSJ():
        items_list = []

        items_amount = int(input("Enter the amount of items: "))
    
        while items_amount < 1:
            print("Invalid. You must enter at least 1 item")
            items_amount = int(input("Enter the amount of items: "))

        for x in range (items_amount):
            print("Item #", x)
            food = input("Enter food: ")
            amount = float(input("Enter amount in lbs: "))
            while amount < 0:
                print("Invalid. Number of lbs must be more than 0")
                amount = float(input("Enter amount in lbs: "))
            foodAdd = Food(food, amount)
            items_list.append(foodAdd)

        return items_list

def displayListSJ(foodList):
     print("Here's a summary of the items purchased: ")
     print("-----------------------------------------")
     for food in foodList:
          foodList[food].__str__()

def main():
     myFoodList = CreateListSJ()

     displayListSJ(myFoodList)

main()

            