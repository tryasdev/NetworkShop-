print('Welcome to NetworkShop "MotoTyt"\nEnter what you want to do?')
parts = ['oil', 'wheel']
price = [450, 7000]
Quantity = [7, 2]
number = 0
import random

while True:
    human = input()
    human2 = input()
    if human == 'secret code':
        print('welcome back boss')
        boss = input()
        if boss == 'new position':
            print('who?')
            new_parts = input()
            parts.append(new_parts)
            print('New parts:', parts)
    elif human == 'buy':
        print('Parts:', parts)
        print('Price:', price)
        print('Quantity:', Quantity)
        human = input()
        if human == 'oil':
            print('How much do you want to buy?')
            quantity = int(input())
            Quantity[0] = Quantity[0] - quantity
            if Quantity[0] <= 0:
                print('There is not enough goods in the warehouse!')
            else:
                print('What are you buying:', parts[0], '\nQuantity:', quantity, '\nThank You!''\nPrice:', price[0],
                      '\nIn stock:', Quantity[0])
        if human == 'wheel':
            print('How much do you want to buy?')
            sell = random.randint(10, 3000)
            price[1] = price[1] - sell
            quantity = int(input())
            Quantity[1] = Quantity[1] - quantity
            if Quantity[1] <= 0:
              print('There is not enough goods in the warehouse!')
            else:
                 print('What are you buying:', parts[1], '\nQuantity:', quantity, '\nThank You!''\nPrice:', price[1],
                  '\nIn stock:', Quantity[1])
        else:
            print('Sorry, we dont have such details')
    else:
     print('The command is not recognised')
