from sys import argv

# I guess argv accepts as many arguments as you want but the first one appears to be the name of the script always?
# when using argv the you have to pass some value to it and that can be used as a variable for other things like user_name here
script, user_name = argv
prompt = "==> "

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live? {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
