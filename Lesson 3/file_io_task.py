name = input("Enter your name: ")
age = input("Enter your age: ")

print("Welcome", name, "you are", age, "years old.")

with open("user_data.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")

try:
    with open("user_data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file is missing.")

with open("user_data.txt", "a") as file:
    file.write("Data successfully saved.\n")
