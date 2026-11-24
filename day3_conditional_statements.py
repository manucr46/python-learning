# 1. Simple if statement
age = 20

if age >= 18:
    print("You are an adult")


# 2. if-else statement
number = 10

if number > 0:
    print("Positive number")
else:
    print("Negative number")


# 3. if-elif-else statement
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 4. Nested if statement
age = int(input("Enter your age: "))

if age >= 18:
    if age >= 21:
        print("You are above 21")
    else:
        print("You are between 18 and 20")
else:
    print("You are below 18")


# 5. Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 6. Positive, Negative or Zero
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 7. Voting Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")