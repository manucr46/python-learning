
# String Data Type - Accessing and Manipulating

text = "Python Programming"

# Accessing characters using indexing
print("First character:", text[0])
print("Last character:", text[-1])

# Accessing characters using slicing
print("First 6 characters:", text[0:6])
print("Programming:", text[7:])

# String manipulation methods
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("Python", "Java"))
print("Length:", len(text))

# Checking string content
print("Starts with Python:", text.startswith("Python"))
print("Contains Programming:", "Programming" in text)

# Removing extra spaces
name = "  Manu CR  "
print("Original:", name)
print("After strip:", name.strip())
