from fungsi_parser import parser_tanggal

def validate_date(arr):
    kabisat = False
    if ((arr[2] % 4 == 0) and (arr[2] % 100 != 0)) or (arr[2] % 4 == 0):
        kabisat = True
    if kabisat:
        if arr[1] == 2:
            if 1 <= arr[0] <= 29:
                return True
            else:
                return False
    else:
        if arr[1] == 2:
            if 1 <= arr[0] <= 28:
                return True
            else:
                return False
    if ((arr[1] == 1) or (arr[1] == 3) or (arr[1] == 5) or (arr[1] == 7) or (arr[1] == 8) or (arr[1] == 10) or (arr[1] == 12)) and (1 <= arr[0] <= 31):
        return True
    elif ((arr[1] == 4) or (arr[1] == 6) or (arr[1] == 9) or (arr[1] == 11)) and (1 <= arr[0] <= 30):
        return True
    else:
        return False
      
