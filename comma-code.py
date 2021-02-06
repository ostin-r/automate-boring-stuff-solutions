'''
Austin Richards 2/6/21

comma-code contains a function that takes any list and 
returns each item with commas between each and an "and" 
before the last item.
'''

def commaList(user_list):

    if len(user_list) == 0:
        raise Exception('Error: list contains no items')

    newList = ''

    for index, item in enumerate(user_list):

        if index < len(user_list)-1:
            newList = newList + str(item) + ', '

        else:
            newList = newList + 'and ' + str(item)

    print(newList)

l = ['bikes', 'wheels', 'gears', 'helmets']
commaList(l)