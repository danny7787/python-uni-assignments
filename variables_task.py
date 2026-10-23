# My information
name = "Danny"
age = 41
height = 170.0

# Display my information
print("My name is", name, "and I am", age,
      "years old. My height is", height, "cm.")

# Calculate my age in months
age_in_months = age * 12
print("My age in months is", age_in_months)

# Add 10 cm to my height
new_height = height + 10
print("My height plus 10 cm is", new_height, "cm")

# Check if my age is greater than 18
print("Is my age greater than 18?", age > 18)

# Convert my height to an integer
height_integer = int(height)
print("My height as an integer is", height_integer)

# Original mistake:
# print("My age is " + age)

# Error message:
# TypeError: can only concatenate str (not "int") to str

# Correction: convert age to text
print("My age is " + str(age))

