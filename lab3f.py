#!/usr/bin/env python3

my_list = [ 1, 2, 3, 4, 5 ]

def add_item_to_list(orderd_list):
    orderd_list.append(orderd_list[-1] + 1)


def remove_items_from_list(ordered_list, items_to_remove):
    for x in items_to_remove:
        ordered_list.remove(x)



if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)