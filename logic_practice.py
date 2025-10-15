# Ian Lee
# 10/14/2025


# 1. Basic Selection Structure
# Write a program that asks the user for their age and prints whether they are eligible to vote (age >= 18).
#   A basic selection structure includes an if-then condition, 
#   statements that executive when the condition is true, an else statement, 
#   statements that execute when the condition is false. 

# Declare variables
userAge = input("What is your age? ")
votingEligible = "Congratulations! You are eligible to vote."
tooYoung = "I'm sorry, you are ineligible to vote."
badInput = "That is not a valid age. Please enter an numerical value."

# Selection if-then conditional statements
# Checks input to determine if the variable userAge is a digit, and if that digit is greater or less than 18.
if userAge.isdigit() == True and int(userAge) >= 18:
    print(votingEligible)
elif userAge.isdigit() == True and int(userAge) < 18:
    print(tooYoung)
else:
    print(badInput)

# Adds a space between parts.
print(" ")


# 2. Relational Comparison Operators
# Ask the user for two numbers and compare them using all six relational operators (==, !=, <, >, <=, >=). 

# Declare variables
firstNumber = float(input("Please enter a number: "))
secondNumber = float(input("Thank you. please enter a second number: "))
numEql = firstNumber == secondNumber
numNotEql = firstNumber != secondNumber
numLesser = firstNumber < secondNumber
numGreater = firstNumber > secondNumber
numLessEql = firstNumber <= secondNumber
numGreatEql = firstNumber >= secondNumber

# Prints a comparison using all six relational operators
print(f"Is {firstNumber} equal to {secondNumber}? {numEql}")
print(f"Is {firstNumber} not equal to {secondNumber}? {numNotEql}")
print(f"Is {firstNumber} less than {secondNumber}? {numLesser}")
print(f"Is {firstNumber} greater than {secondNumber}? {numGreater}")
print(f"Is {firstNumber} less than or equal to {secondNumber}? {numLessEql}")
print(f"Is {firstNumber} greater than or equal to {secondNumber}? {numGreatEql}")

# Adds a space between parts.
print(" ")


# 3. AND Logic
# Ask the user for their test score and attendance percentage. Print whether they pass the course
# score >= 70 & attendance >= 80%

# Declare variables
testScore = float(input("Please enter your test score as a decimal number: "))
attendScore = float(input("Please enter your attendance score: "))

# if-then with an AND statement
if testScore >= 70.0 and attendScore >= 80.0:
    print("You have passed the course!")
else:
    print("You have not passed the course...")

# Adds a space between parts.
print(" ")


# 4. OR Logic
# Ask the user if they have either a student ID or a library card. Print whether they can enter the library. 

# Declare variables
studentID = input("Do you have your student ID (yes or no)? ".lower())
libraryCard = input("Do you have your library card (yes or no)? ".lower())

#if-then with an OR statement
if studentID == "yes" or libraryCard == "yes":
    print("You are allowed to enter the library!")
else:
    print("Sorry, you can't enter the library at this time...")

# Adds a space between parts.
print(" ")


# 5. NOT Logic
# Ask the user if they are banned (yes or no). Use NOT to determine if they can access the system.

# Declare variables
bannedStatus = input("Have you been banned from the system (yes or no)?").lower()

# if-then with a NOT statement
if not bannedStatus == "yes":
    print("You can access the system at this time.")
else:
    print("You cannot access the system at this time.")

# Adds a space between parts.
print(" ")


# 6. Combining AND/OR with Precedence
# Write a program that checks if a user qualifies for a scholarship: GPA >= 3.5 and (volunteer hours >= 50 or leadership role is yes). 

# Declare variables
currentGPA = float(input("Please enter your current GPA: "))
volunteerHours = int(input("Please enter your current volunteer hours (round to nearest hour): "))
leaderRole = input("Have you taken on a leadership role (yes or no): ").lower()

# if-then with AND/OR and Precedence
if currentGPA >= 3.5 and (volunteerHours >= 50 or leaderRole == "yes"):
    print("You qualify for this scholarship!")
else:
    print("Our apologies, you don't qualify for this scholarship...")