shopping_list = set()
what_to_do = ''
while what_to_do != 'Exit':
    what_to_do = input('Type in Exit to quit,\n'
                       'show to print shopping list,\n'
                       'add to add item to shopping list\n'
                       'remove to remove item form shopping list.\n')
    if what_to_do == 'Exit':
        print('You typed ', what_to_do, 'the program is stopping!')
    elif what_to_do == 'show':
        if len(shopping_list) > 0:
            for item in shopping_list:
                print(item)
        else:
            print('Shopping list is empty!')
    elif what_to_do == 'add':
        item = input('What do you want to add:')
        shopping_list.add(item)
    elif what_to_do == 'remove':
        item = input('What do you want to remove:')
        if shopping_list.__contains__(item):
            shopping_list.remove(item)
        else:
            print(item, 'is not in the list!')
    else:
        print('You typed something wrong, try again')

