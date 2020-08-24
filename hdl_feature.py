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
# Output Function


def output_function(hdl, analysis):
    print("This value of HDL ({}) is {}.".format(hdl, analysis))
    return

# Driver Function calls input_function and check_HDL


def Driver():
    x = input_function()
    message = check_HDL(x)
    output_function(x, message)
    return


# Call Function
Driver()
