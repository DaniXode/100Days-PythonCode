foods=[]
prices=[]
total=0
while True:
    food =input('enter a food to buy(q to quite)')
    if food =='q' or food =='':
        break
    else:
        price=float(input(f'enter the price of a{food}:$'))
        foods.append(food)
        prices.append(price)

print('--- your cart ---')

for food in foods:
    print(food,end=' ')
for price in prices:
    if price=='':
        print('please enter price vale')
    total+=price
print(f'your total is:${total}')


