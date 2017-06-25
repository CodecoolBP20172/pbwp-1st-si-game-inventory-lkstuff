# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    for k, v in inventory.items():
        print(v, k)
    d = sum(inventory.values())
    print("Total number of item: %d" % d)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    import operator

    TITLE_COUNT = "count"
    TITLE_NAME = "item name"

    def get_max_lenght(inventory):
        key_lenght = len(TITLE_NAME)
        value_lenght = len(TITLE_COUNT)
        for k, v in inventory.items():
            key_lenght = max(len(str(k)), key_lenght)
            value_lenght = max(len(str(v)), value_lenght)
        return {"title": key_lenght + 4, "count": value_lenght + 2}

    def print_table_row(count, name, max_lenght):
        print("%s%s%s%s" % (" " * (max_lenght["count"] - len(str(count))), str(count), " " * (max_lenght["title"] - len(name)), name))

    if order == "count,desc":
        sorted_inventory = sorted(inventory.items(), key = operator.itemgetter(1), reverse = True)
    elif order == "count,asc":
        sorted_inventory = sorted(inventory.items(), key = operator.itemgetter(1), reverse = False)
    else:
        sorted_inventory = [(k,v) for k,v in inventory.items()]

    max_lenght = get_max_lenght(inventory)
    print("Inventory:")
    print_table_row(TITLE_COUNT, TITLE_NAME, max_lenght)
    print("-" * (max_lenght["count"] + max_lenght["title"]))
    for k, v in sorted_inventory:
        print_table_row(v, k, max_lenght)
    print("-" * (max_lenght["count"] + max_lenght["title"]))
    d = sum(inventory.values())
    print("Total number of item: %d" % d)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass


def main():
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(inv)

    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)

    print_table(inv, "count,desc")

if __name__ == '__main__':
    main()
