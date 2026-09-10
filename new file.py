print('Welcome to NetworkShop "MotoTyt"\nEnter what you want to do?')
parts = ['oil','carburator']
price = [450, 7000]
Quantity = [7,2]
number = 0
while True:
    human = input()
    if human == 'buy':
        print('Parts:',parts[0],',',parts[1])
        print('Price:',price[0],',',price[1])
        print('Quantity:',Quantity[0],',',Quantity[1])
        human = input()
        if human == 'oil':
            print('How much do you want to buy?')
            quantity = int(input())
            if Quantity[0] - quantity < 0:
                print('There is not enough goods in the warehouse!')
            elif Quantity[0] - quantity > 0:
             print('What are you buying:',parts[0],'\nQuantity:',quantity,'\nThank You!''\nPrice:',price[0],'\nIn stock:',Quantity[0] - quantity)
        elif human == 'carburator':
            print('How much do you want to buy?')
            quantity = int(input())
            if Quantity[1] - quantity < 0:
                print('There is not enough goods in the warehouse!')
            elif Quantity[1] - quantity > 0:
             print('What are you buying:', parts[1], '\nQuantity:', quantity, '\nThank You!''\nPrice:', price[1],'\nIn stock:', Quantity[1] - quantity)
        else:
            print('Sorry, we dont have such details')
