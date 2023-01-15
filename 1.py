def verify_e_o(value):
    value = float(value)
    if value.is_integer():
        if value % 2 == 0:
            print("even")
        else:
            print("odd")
        for i in range(0, 18, 2):
            print(value + i, sep='', end=', ', flush=True)
        print(value + 18, sep='', end='.\n', flush=False)
    else:
        print("error : input is a number with significant digits beyond the decimal point")

if __name__ == '__main__':
    verify_e_o(23.00)