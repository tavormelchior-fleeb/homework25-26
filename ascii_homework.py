def rotate(image: str, degrees: int) -> str:
    lines = image.split("\n")
    if degrees == 0:
        return image
    if degrees == 90:
        # find the columns, and use their reversal as rows
        col = ["" for i in range(len(lines[0]))]
        for line in lines:
            for j in range(len(line)):
                col[j] += line[j]
        return "\n".join([i[::-1] for i in col])
    elif degrees == 180:
        # 90 * 2
        return rotate(rotate(image, 90), 90)
    elif degrees == 270:
        # 90 * 3
        return rotate(rotate(rotate(image, 90), 90), 90)
    elif degrees == 360:
        # reverse all lines, creating a mirror image
        return "\n".join([line[::-1] for line in lines])
    else:
        print("degrees must be of 90, 180, 270, or 360")
        raise ValueError


def convert(image: str, conv_table: list, choice: int ) -> str:
    if conv_table == 0:
        return image
    lines = image.split("\n")
    new = ["" for line in lines]
    conv_dict = {i[0]: i[1:3] for i in conv_table}
    if choice == 0:
        return image
    for i in range(len(lines)):
        for char in lines[i]:
            if char in conv_dict.keys():
                new[i] += conv_dict[char][choice - 1]
            else:
                new[i] += "X"

    return "\n".join(new)


def serialize(text, angle, selection, conv_table, to_print):
    lines = text.split("\n")
    new = ["" for line in lines]
    temp = ["", ""]
    for i in range(len(lines)):
        for char in lines[i]:
            if char == temp[1]:
                temp[0] += 1
            else:
                new[i] += str(temp[0]) + temp[1]
                temp[0] = 1
                temp[1] = char
        new[i] += str(temp[0]) + temp[1]
    serialized = convert(rotate("\n".join(new), angle), conv_table, selection)
    if to_print:
        return serialized
    else:
        with open("output.txt", "w") as file:
            file.write(serialized)
            return file


def deserialize(text, angle, choice, conv_table, to_print):
    # no way to undo convert (what does X become?)
    # de-rotate
    if angle != 0:
        txt = rotate(text, 360-angle)
    else:
        txt = text
    fixed = ""
    for i in range(len(txt)):
        if txt[i].isnumeric():
            try:
                fixed += txt[i+1] * int(txt[i])
            except IndexError:
                continue
    if to_print:
        return fixed
    else:
        with open("output.txt", "w") as file:
            file.write(fixed)
            return file


print(deserialize("3H1 2e1 3l1 3o1,1 1 1W1o1r1l1d1!1\n5g5y", 0, 0, ["ghj", "bsr", "xcv", "!de", "ogt"], True))