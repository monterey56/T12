#create a list called menu, which contains at least 4 items in the cafe
#create a dictionary called stock which contains the stock value of each menu item
#create a dictionary called price which contains the price of each item on the menu
#calculate total_stock worth in the cafe
#print the result of total_stock

menu = ["biscuits", "tea", "sandwich", "full english"]
stock = {"biscuits": 50, "tea": 30, "sandwich": 10, "full english": 5}
price = {"biscuits": 1.0, "tea": 2.0, "sandwich": 5.0, "full english": 7.0}

total_stock = 0
for item in menu:
    total_stock += stock[item] * price[item]

print(total_stock)