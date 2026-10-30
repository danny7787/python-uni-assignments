name = input("Enter your name: ")
age = input("Enter your age: ")

print("Welcome", name, "you are", age, "years old.")

with open("user_data.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")

try:
    with open("wrong_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError as error:
    print(error)
