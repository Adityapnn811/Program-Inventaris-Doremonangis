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

def parser_tanggal(tanggal_str):
    tanggal_copy = []
    string_group = ""
    for i in tanggal_str:
        if i == "/":
            tanggal_copy += ""
            tanggal_copy.append(str(string_group))
            string_group = ""
        else:
            string_group += i
    tanggal_copy.append(string_group)
    # Ubah array tanggal ke integer
    for j in range(len(tanggal_copy)):
        tanggal_copy[j] = int(tanggal_copy[j])
<<<<<<< HEAD
    return tanggal_copy
=======
    return tanggal_copy
>>>>>>> 4c5565ec20ae00a28d6429e11e9b28e7f2e0e5ff
