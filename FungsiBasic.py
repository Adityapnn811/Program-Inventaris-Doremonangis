##DISCLAIMER : parameter yang database - database ini itu parameter databasneya
#Co : nanti dari constant misal constant USER = "user.csv"
#dipanggilnya nanti open_data(USER)


#ini fungsi buat open datanya nanti dipanggil di loading
#Nanti kalo di main() tinggal di modif dikit

def open_data(database):
    f = open(database,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    return lines

#fungsi parser ala adit
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


#Panjang_header_database isinya banyak header/kolom csv, fixed
#Ini buat ubah yang nomor gt ke integer
def convert_array_data_to_real_values(array_data, panjang_header_database):
  arr_cpy = array_data[:]
  for i in range(panjang_header_database):
    if(i == 0):
      arr_cpy[i] = int(arr_cpy[i])
    elif(i == 2):
      arr_cpy[i] = float(arr_cpy[i])
  return arr_cpy


#Ini buat ngesplit datanya
def convert_line_to_data(line):
  raw_array_of_data = parser(line)
  array_of_data = [data.strip() for data in raw_array_of_data]
  return array_of_data


#Ini buat ngeluarin headernya (yang bagian header pop)
#makenya sama aja, parameternya nanti dapet dari yang lines
def show_header(lines):
  raw_header = lines.pop(0)
  header = convert_line_to_data(raw_header)
  return header

#Ini fungsi yang nanti buat manip data, append dll, 
#parameternya juga dapet dari lines yang direturn
def usable_array_data(lines):
  datas = []
  for line in lines:
    array_of_data = convert_line_to_data(line)
    datas.append(array_of_data)
  return array_of_data


#header ini hasil return dari yg show_header
#yang datas itu hasil return dari usable_array_data
#ada kemungkinan lebih enak ditaro di main biar bisa pake global
#tapi sementara gini dlu aja, nanti bisa dimodif
#FUNGSI INI BUAT NGUBAH DARI ARRAY KE CSVNYA LAGI gt kek di tutorial
def convert_datas_to_string(header, datas):
  string_data = ";".join(header) + "\n"
  for arr_data in datas:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ";".join(arr_data_all_string)
    string_data += "\n"
  return string_data


#fungsi ini buat ngeganti csvnya kayak di tutorial
def write_fix_data(header, datas, database):
  datas_as_string = convert_datas_to_string(header, datas)
  f = open(database, "w")
  f.write(datas_as_string)
  f.close()
