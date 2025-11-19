# U. Float or int
N = input()
# Check if number has decimal point
if '.' not in N:
    # Pure integer
    print("int", N)
else:
    # Split integer and decimal part
    integer, decimal = N.split('.')
    # Check if decimal part is all zeros
    if int(decimal) == 0:
        print("int", integer)
    else:
        # float case
        print("float", integer, "0." + decimal if not decimal.startswith("0.") else decimal)
