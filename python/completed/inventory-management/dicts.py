"""Functions to keep track and alter inventory."""


def create_inventory(items: list[str]) -> dict[str:int]:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    return {item: items.count(item) for item in set(items)}


def add_items(inventory: dict[str:int], items: list[str]) -> dict[str:int]:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if inventory.get(item):
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory: dict[str:int], items: list[str]) -> dict[str:int]:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory: dict[str:int], item: str):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, None)
    return inventory


def list_inventory(inventory: dict[str:int]) -> list[tuple[str, int]]:
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(item, value) for item, value in inventory.items() if value > 0]
