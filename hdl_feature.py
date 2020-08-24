def input_function():
    hdl = input("Enter HDL: ")
    return int(hdl)


def check_HDL(hdl):
    if hdl >= 60:
        return "Normal"
    elif hdl < 40:
        return "Low"
    else:
        return "Borderline Low"
