def parser(line):
    line_copy=[]
    string_group = ""
    for i in line:
        if i == ";":
            line_copy += ""
            line_copy.append(str(string_group))
            string_group = ""
        else:
            string_group += i
    line_copy.append(str(string_group))
    return line_copy
