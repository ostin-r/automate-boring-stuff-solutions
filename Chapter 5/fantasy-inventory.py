'''
Austin Richards 2/11/21
'''

def displayInventory(inventory):

    print("\nInventory:\n")
    item_total = 0

    for k, v in inventory.items():
        print(k + ':', v)
        item_total += v

    print("\nTotal number of items: " + str(item_total))

def addToInventory(inventory, addedItems):

    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)