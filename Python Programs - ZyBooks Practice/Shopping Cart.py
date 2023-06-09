# Jordan Allen
# ZyLabs 10.19

class TimeTravelLog:
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, total))

    def print_item_description(self):
        print('%s: %s' % (self.item_name, self.item_description))


class TimeTravel:
    def __init__(self, travel_id='none', current_date='January 1, 2016', cart_items=None):
        if cart_items is None:
            cart_items = []
        self.customer_name = travel_id
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

    def remove_item(self, itemName):
        drop_item = False
        for item in self.cart_items:
            if item.item_name == itemName:
                self.cart_items.remove(item)
                drop_item = True
                break
        if not drop_item:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item_to_purchase):
        change_item = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item_to_purchase.item_name:
                change_item = True
                self.cart_items[i].item_quantity = item_to_purchase.item_quantity
                break
        if not change_item:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            add_cost = (item.item_quantity * item.item_price)
            total_cost += add_cost
        return total_cost

    def print_total(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items: %d\n' % self.get_num_items_in_cart())
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print('\nTotal: $%d' % total_cost)

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('\nItem Descriptions')
            for item in self.cart_items:
                item.print_item_description()


def print_menu(shopping_cart):
    shopping_menu = ('\nMENU\n'
                     'a - Add item to cart\n'
                     'r - Remove item from cart\n'
                     'c - Change item quantity\n'
                     "i - Output items' descriptions\n"
                     'o - Output shopping cart\n'
                     'q - Quit\n')

    user_choice = ''
    while user_choice != 'q':
        print(shopping_menu)
        user_choice = input('Choose an option:\n')
        while (user_choice != 'a' and user_choice != 'o' and user_choice != 'i' and user_choice != 'q'
               and user_choice != 'r' and user_choice != 'c'):
            user_choice = input('Choose an option:\n')
        if user_choice == 'a':
            print("\nADD ITEM TO CART")
            item_name = input('Enter the item name:\n')
            item_description = input('Enter the item description:\n')
            item_price = int(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            shopping_cart.add_item(item_to_purchase)

        elif user_choice == 'i':
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            shopping_cart.print_descriptions()

        elif user_choice == 'r':
            print('REMOVE ITEM FROM CART')
            item_name = input('Enter name of item to remove:\n')
            shopping_cart.remove_item(item_name)

        elif user_choice == 'o':
            print('OUTPUT SHOPPING CART')
            shopping_cart.print_total()

        elif user_choice == 'c':
            print('\nCHANGE ITEM QUANTITY')
            item_name = input('Enter the item name:\n')
            new_total = int(input('Enter the new quantity:\n'))
            item_to_purchase = ItemToPurchase(item_name, 0, new_total)
            shopping_cart.modify_item(item_to_purchase)


if __name__ == "__main__":
    cust_name = input("Enter customer's name:\n")
    curr_date = input("Enter today's date:\n")
    print("\nCustomer name: %s" % cust_name)
    print("Today's date: %s" % curr_date)
    new_shopping_cart = TimeTravel(cust_name, curr_date)
    print_menu(new_shopping_cart)
