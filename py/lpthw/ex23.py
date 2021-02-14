import sys
script, encoding, error = sys.argv #新写法
#这三个变量似乎都有各自独特的含义

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) #循环运行



def print_line(line, encoding, errors):
    next_lang = line.strip() #带?---删掉每行的\n
    raw_bytes = next_lang.encode(encoding, errors = errors) #编码成原始字节
    cooked_string = raw_bytes.decode(encoding, errors) #解码成字符串
    
    print(raw_bytes, "<===>", cooked_string)
    

languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error) #调用main
#decode bytes, encode strings
