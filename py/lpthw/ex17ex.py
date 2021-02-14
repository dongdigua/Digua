from sys import argv
from os.path import exists

scrript, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read() #读取

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}") #是否存在
#print("Ready, hit RETURN to continue, ^C to abort.") 
#input() 

out_file = open(to_file, 'w') #创建
out_file.write(indata) #写入

#print("Alright, all done.")

out_file.close()
in_file.close()
