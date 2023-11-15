def displayInventory(inventory):
    print("Inventory:")
    for item , count in inventory.items():
        print(f"{count}\t{item}")
    print(f"Total number of items: {sum(inventory.values())}")


def addToInventory(inventory , addedItems):
    for each in addedItems:
        if each not in inventory.keys():
            inventory[each]=1
        else:
            inventory[each] += 1
    return inventory


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
hehe = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(addToInventory(hehe , dragonLoot))