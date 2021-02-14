from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit ^C.")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

contain =  f'{line1}\n{line2}\n{line3}'
target.write(contain)

print("And finally, we close it.")
target.close()
