
# Cash Utility Functions ===================

# Cash amounts will be represented by integers denoting cents
# Half pennies will be truncated down to nearest integer value

def cashToString(cash: int) -> str:
    integer_string = str(cash)
    return "$" + integer_string[0:-2] + "." + integer_string[-2:]

def discount(cash_amount: int, discount: int) -> int:
    return (cash_amount * discount) // 100 # Half penny truncated using floor div

# ==========================================
