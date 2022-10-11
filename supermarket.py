def supermarket():
    items = []
    while True:
        display = input('Press enter to continue.')
        print('------------------Welcome to the supermarket------------------')
        print('1. View items\n2. Add items for sale\n3. Purchase items\n4. Exit')
        choice = input('Enter the number of your choice : ')

        if choice == '1':
            view_inventory(items)

        elif choice == '2':
            add_items_inventory(items)

        elif choice == '3':
            sell_to_customers(items)

        elif choice == '4':
            print('------------------exited------------------')
            break

        else:
            print('You entered an invalid option')


def add_items_inventory(items):
    print('------------------Add items------------------')
    print('To add an item fill in the inventory')
    item = {}
    item['name'] = input('Item name : ')
    while True:
        try:
            item['quantity'] = int(input('Item quantity : '))
            break
        except ValueError:
            print('Quantity should only be in digits')
    while True:
        try:
            item['price'] = int(input('Price $ : '))
            break
        except ValueError:
            print('Price should only be in digits')
    print('Item has been successfully added.')
    items.append(item)

def view_inventory(items):
    print('------------------View Items------------------')
    print('The number of items in the inventory are : ', len(items))
    while len(items) != 0:
        print('Here are all the items available in the supermarket.')
        for item in items:
            print(item)
        break

def sell_to_customers(items):
    print('------------------purchase items------------------')
    print(items)
    purchase_item = input('which item do you want to purchase? Enter name : ')
    quantity_item = int(input('how many '+purchase_item+' are you looking to buy? : '))
    for item in items:
        if purchase_item.lower() == item['name'].lower():
            if item['quantity'] != 0 and item['quantity'] >= quantity_item:
                print('Pay ', int(item['price'])*int(quantity_item), 'at checkout counter.')
                item['quantity'] -= quantity_item
            else:
                continue
                print('item out of stock.')


if __name__ == '__main__':
    supermarket()
