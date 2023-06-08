
# Cash Utility Functions ===================

# Cash amounts will be represented by integers denoting cents
# Half pennies will be truncated down to nearest integer value

def cash_to_string(cash: int) -> str:

    if cash < 0:
        raise ValueError("Value cash must be a positive integer")

    integer_string = f"{cash:03d}"
    return "$" + integer_string[0:-2] + "." + integer_string[-2:]

def sum_items_price(item_ids, items):
    total = 0

    for item_id in item_ids:
        total += items[item_id]["price"]

    return total

def discount(cash_amount: int, discount: int) -> int:
    return (cash_amount * discount) // 100 # Half penny truncated using floor div

# ==========================================


# List Utility Functions ===================

def count_unique_values(values: int) -> int:
    return len(set(values)) # Converting a list to set removes duplicates

def get_unique_values(n: int, values: list) -> list:
    unique_items = list(set(values)) # Converting a list to set removes duplicates

    if count_unique_values(values) < n:
        raise ValueError("Not enough unique items in list")
    elif n < 0:
        raise ValueError("Value n must be a positive integer")

    return unique_items[0:n]

# Mutates given list
def remove_unique_values(n: int, values: list):
    unique_items = get_unique_values(n, values)

    for item in unique_items:
        values.remove(item)

def get_total_discount(shopping_cart, items):
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

