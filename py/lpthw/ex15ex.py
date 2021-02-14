from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
#txt.close()
print(f"{txt} closed") #为什么不好使?
txt.close
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
#txt.close()
print("txt_again closed") #为什么不好使?
txt_again.close
#搞不懂
