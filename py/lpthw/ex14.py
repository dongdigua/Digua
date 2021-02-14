from sys import argv

script, user_name = argv
promot = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(promot)

print(f"Where do you live {user_name}?")
lives = input(promot)

print(f"What kind of computer do you have?")
computer = input(promot)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure what that is.
Ant you have a {computer} computer. Nice.
""")
