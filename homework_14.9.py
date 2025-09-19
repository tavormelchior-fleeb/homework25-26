
def turn_hexa(str_1):
    """
    this function turns a string into a hexadecimal number
    if input is not 1-9 and a-f prints error message
    :param str_1: input string to convert
    :return: the value of str_1 as a hexadecimal number
    """
    # check for valid input, use base 16 integer (include a-f)
    try:
        print(int(str_1, 16))
    except ValueError:
        print("invalid input")


# I got tired of writing descriptions for the functions


def hex_sum(str_1):
    hex_chars = '0123456789abcdefABCDEF'
    total = 0
    current = ""
    for char in str_1:
        if char in hex_chars:
            current += char
        elif current != "":
            total += int(current, 16)
            current = ""
    if current != "":
        total += int(current, 16)
    print(total)


# I didn't do this assignment as a function...
nums_list = []
while 1:
    num = input("please enter a number:")
    try:
        nums_list.append(int(num))
    except ValueError:
        break
print(f"average: {sum(nums_list) / len(nums_list)}")
s_list = sorted(nums_list)
le = len(nums_list)
if le % 2 == 1:
    med = s_list[int((le - 1) / 2)]
else:
    med = (s_list[int(le/2)] + s_list[int(le / 2 - 1)]) / 2
print(f"median: {med}")

