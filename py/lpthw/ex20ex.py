from sys import argv

script, input_file = argv

def print_all(f): #打印整个文件
    print(f.read())
    
def rewind(f):
    f.seek(0) #seek是转到字节，此处就是转到第一字节(倒带)
    
def print_a_line(line_count, f): #打印一行
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1  # x += y -> x = x + y
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
