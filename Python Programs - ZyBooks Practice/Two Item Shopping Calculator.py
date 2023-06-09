# Jordan Allen
# ZyLabs 10.17

class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def init(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(self.item_price) + ' = $'
              + format(self.item_price * self.item_quantity))


if __name__ == '__main__':
    itemOne = ItemToPurchase()
    print('Item 1')
    itemOne.item_name = input('Enter the item name:\n')
    itemOne.item_price = int(input('Enter the item price:\n'))
    itemOne.item_quantity = int(input('Enter the item quantity:\n'))

    itemTwo = ItemToPurchase()
    print('\nItem 2')
    itemTwo.item_name = input('Enter the item name:\n')
    itemTwo.item_price = int(input('Enter the item price:\n'))
    itemTwo.item_quantity = int(input('Enter the item quantity:\n'))

    itemOnePrice = itemOne.item_price * itemOne.item_quantity
    itemTwoPrice = itemTwo.item_price * itemTwo.item_quantity
    totalCost = itemOnePrice + itemTwoPrice

    print('\nTOTAL COST')
    itemOne.print_item_cost()
    itemTwo.print_item_cost()
    print('\nTotal: ${}'.format(totalCost))
