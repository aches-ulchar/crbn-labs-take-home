
# Cash Utility Functions ===================

# Cash amounts will be represented by integers denoting cents
# Half pennies will be truncated down to nearest integer value

def cash_to_string(cash: int) -> str:
    """
    Turn an integer representing number of pennies into a
    string representing dollars and cents

    :param int cash: the number of pennies

    :return: a string representation of dollars and cents
    :rtype: str
    """

    if cash < 0:
        raise ValueError("Value cash must be a positive integer")

    integer_string = f"{cash:03d}"
    return "$" + integer_string[0:-2] + "." + integer_string[-2:]

def sum_items_price(item_ids: list, items: dict) -> int:
    """
    Get the total value of the items in cents

    :param list item_ids: a list of the items in the shopping card
    represented by item id strings
    :param items dict: a dictionary indexed by item ids containing the
    available products

    :return: the value of the items in cents
    :rtype: int
    """
    total = 0

    for item_id in item_ids:
        total += items[item_id]["price"]

    return total

def discount(cash_amount: int, discount: int) -> int:
    """
    Get the discount off a cash amount using a percentage

    :param int cash_amount: the amount of the transaction in cents
    :param int discount: the discount as a percentage, given as an integer

    :return: the discount amount (not the price after discount)
    :rtype: int
    """
    return (cash_amount * discount) // 100 # Half penny truncated using floor div

# ==========================================


# List Utility Functions ===================

def count_unique_values(values: list) -> int:
    """
    Counts the number of unique items in a list

    :param list values: a list of items, potentially containing duplicates

    :return: the number of unique values in the list
    :rtype: int
    """
    return len(set(values)) # Converting a list to set removes duplicates

def get_unique_values(n: int, values: list) -> list:
    """
    Retrieves a sample of n unique values from a list, leaving the
    input list unaltered

    :param int n: a positive integer representing the number of unique
    values to sample
    :param list values: the list to sample unique values from

    :return: a list of unique values from the original input list
    :rtype: list
    """
    unique_items = list(set(values)) # Converting a list to set removes duplicates

    if count_unique_values(values) < n:
        raise ValueError("Not enough unique items in list")
    elif n < 0:
        raise ValueError("Value n must be a positive integer")

    return unique_items[0:n]

# Mutates given list
def remove_unique_values(n: int, values: list):
    """
    Removes n unique values from the provided list by MUTATING
    the passed list

    :param int n: the number of unique values to remove
    :param list values: the list to perform the operation on
    """
    unique_items = get_unique_values(n, values)

    for item in unique_items:
        values.remove(item)

def get_total_discount(shopping_cart: list, items: dict) -> int:
    """
    Returns the total discount of items in a list

    :param list shopping_cart: a list of items representing the items
    being purchased by the customer
    :param dict items: a dictionary indexed by item ids containing the
    available products

    :return: the total discount applied to the purchase
    :rtype: int
    """
    undiscounted_items = shopping_cart.copy()
    total_discount = 0
    unique_values = None

    while(len(undiscounted_items) != 0):
        if(count_unique_values(undiscounted_items) >= 5):
            unique_values = get_unique_values(5, undiscounted_items)
            total_discount += discount(sum_items_price(unique_values, items), 20)
            remove_unique_values(5, undiscounted_items)
        elif(count_unique_values(undiscounted_items) >= 4):
            unique_values = get_unique_values(4, undiscounted_items)
            total_discount += discount(sum_items_price(unique_values, items), 15)
            remove_unique_values(4, undiscounted_items)
        elif(count_unique_values(undiscounted_items) >= 3):
            unique_values = get_unique_values(3, undiscounted_items)
            total_discount += discount(sum_items_price(unique_values, items), 10)
            remove_unique_values(3, undiscounted_items)
        elif(count_unique_values(undiscounted_items) >= 2):
            unique_values = get_unique_values(2, undiscounted_items)
            total_discount += discount(sum_items_price(unique_values, items), 5)
            remove_unique_values(2, undiscounted_items)
        else:
            # no applicable discounts
            break

    return total_discount

if __name__ == "__main__":
    import prompt

    available_items = {
            "shirt_1": {"item_name": "Shirt 1", "price": 800},
            "shirt_2": {"item_name": "Shirt 2", "price": 800},
            "shirt_3": {"item_name": "Shirt 3", "price": 800},
            "shirt_4": {"item_name": "Shirt 4", "price": 800},
            "shirt_5": {"item_name": "Shirt 5", "price": 800},
            }

    shopping_cart = []

    print(prompt.INTRO)

    while True:
        user_in = input("> ").lower().split()
        if user_in[0].startswith("h"):
            print(prompt.HELP)
        elif user_in[0].startswith("q"):
            quit()
        elif user_in[0].startswith("d"):
            price = sum_items_price(shopping_cart, available_items)
            current_discount = get_total_discount(shopping_cart, available_items)
            print("Original Price:", cash_to_string(price), "Total Discount:", cash_to_string(current_discount), "Total After Discount:", cash_to_string(price-current_discount))
        elif user_in[0].startswith("c"):
            for item in set(shopping_cart):
                print(item + ":", shopping_cart.count(item))
        elif user_in[0].startswith("l"):
            for k, v in available_items.items():
                print("Item Name:", v["item_name"], "\t Item ID:", k, "\t Price:", cash_to_string(v["price"]))
        elif user_in[0].startswith("a"):
            if len(user_in) > 1 and user_in[1] in available_items:
                if len(user_in) > 2:
                    try:
                        for x in range(0, int(user_in[2])):
                            shopping_cart.append(user_in[1])
                    except ValueError:
                        print("error: n is not a proper integer")
                else:
                    shopping_cart.append(user_in[1])

            else:
                print("USAGE: > a <item_id> [n]")
