price=[7,1,5,3,6,4]

min_price=price[0]
max_profit=0
profit=0
ln=len(price)

for i in price:
    if i < min_price:
        min_price= i

    profit= i - min_price

    if profit > max_profit:
        max_profit = profit

    
        
print(max_profit)