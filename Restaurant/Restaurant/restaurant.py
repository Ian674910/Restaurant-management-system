#importing necessary libraries
import json
#defining the function
def get_rating(reviews):
    rating = 5
    if reviews: #[3,4,5,1,4,5]
        rating = sum(reviews) // len(reviews)
    return '*'*rating    
#
with open('menu.json', 'r') as f:
    data=json.load(f)

items = data.get('items',[])
while True:
    print('-'*50)
    print('Pamoja Restaurant')
    print('-'*50)
    print('1.Show Menu')
    print('2.order items')
    print('3. Add item')
    print('4. Add review')
    print('5. Exit')
    print('-'*50)
    choice= int(input())

    if choice == 1:
        print('-'*50)
        print('id\tname\t\tprice\tRating')
        print('-'*50)
        for item in items:
            print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}\t{get_rating(item.get("reviews",[]))}')
        print('-'*50)
    elif choice == 2:
        ordered_items = {}
        order_items = list(map(int,input('hey what do you want to try? ').split(',')))
        print('-'*50)
        print('id\tname\t\tprice\tquantity\tamount')
        print('-'*50)
        total_bill = 0
        for order_item in order_items:
            for item in items:
                if item['id']== order_item:
                    if order_item in ordered_items:
                        ordered_items[order_item]['quantity'] += 1
                    else:    
                        ordered_items[order_item] = item
                        ordered_items[order_item]['quantity'] = 1
                    break    
        for item in ordered_items:
            name = ordered_items[item]['name']
            price = ordered_items[item]['price']
            quantity = ordered_items[item]['quantity']
            amount = price * quantity
            print(f'{item}\t{name}\t{price}\t{quantity}\t\t{amount}')
            total_bill += amount
        print('-'*50)
        print(f'\t Total Amount: {total_bill}')
        print('-'*50)              
    elif choice == 3:
        name = input('Enter item name: ')
        item_price = input('Enter the price: ')
        item_type = input('veg or non-veg: ')
        items.append({
            'id': len(items) + 1,
            'name': name,
            'price': item_price,
            'veg':True if item_type == 'veg' else False,
            'reviews':[]
        })
        
        data['items'] = items 
        with open('menu.json','w') as f:
            json.dump(data, f)
        print('Item added')    
    elif choice == 4:
        item_id = int(input('Enter the item id: '))
        rating = int(input('give your rating 1-5: ')) 
        for i, item in enumerate(items):
            if item['id'] == item_id:
                items[i]['reviews'].append(rating)
                break
    else:
        data['items'] = items 
        with open('menu.json','w') as f:
            json.dump(data, f)
        print('Thank you...come next time') 
        break            
