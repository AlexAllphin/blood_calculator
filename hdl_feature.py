# Input takes in an HDL value
def input_function():
    hdl = input("Enter HDL: ")
    return int(hdl)

# Check HDl analyzes the HDL value to return useful information


def check_HDL(hdl):
    if hdl >= 60:
        return "Normal"
    elif hdl < 40:
        return "Low"
    else:
        return "Borderline Low"

# Driver Function calls input_function and check_HDL


def Driver():
    x = input_function()
    check_HDL(x)
