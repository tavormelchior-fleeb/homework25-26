def check(a, b):
    a_list = str(a.getvalue()).split()
    b_list = str(b.getvalue()).split()

    truth_list = []

    for i in range(4):
        if a_list[i] in b_list:
            if a_list[i] == b_list[i]:
                truth_list.append("B")
                b_list[i] = "X"
            else:
                # could be done recursive/assist function
                # elected to use this for worst case (1111) so wouldn't do this three times
                index = b_list.index(a_list[i])
                if a[index] == b[index]:
                    a[index] = "FS"
                    b[index] = "FS"
                    if a_list[i] in b_list:
                        index = b_list.index(a_list[i])
                        if a[index] == b[index]:
                            a[index] = "TS"
                            b[index] = "TS"
                            index = b_list.index(a_list[i])
                            if a_list[i] in b_list:
                                if a[index] == b[index]:
                                    a[index] = "DS"
                                    b[index] = "DS"
                            truth_list.append("C")
                        else:
                            truth_list.append("C")
                else:
                    truth_list.append("C")
        else:
            truth_list.append("")

    return truth_list

