first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
def format_name(f_name, l_name):
    first = f_name.title()
    last = l_name.title()
    return f"{first} {last}"
print(format_name(first_name, last_name))
