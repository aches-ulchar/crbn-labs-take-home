
# Cash Utility Functions ===================

# Cash amounts will be represented by integers denoting cents
# Half pennies will be truncated down to nearest integer value

def cash_to_string(cash: int) -> str:

    if cash < 0:
        raise ValueError("Value cash must be a positive integer")

    integer_string = f"{cash:03d}"
    return "$" + integer_string[0:-2] + "." + integer_string[-2:]

def discount(cash_amount: int, discount: int) -> int:
    return (cash_amount * discount) // 100 # Half penny truncated using floor div

# ==========================================
