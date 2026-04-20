# Conditional structure
score = 85

if score >= 90:
    print("The student earned an A.")
elif score >= 70:
    print("The student passed the class.")
else:
    print("The student needs more practice.")

# For loop
numbers = [3, 7, 0, 12, 5]

print("\nHere are the positive numbers doubled:")
for number in numbers:
    if number == 0:
        continue
    print(f"{number} doubled is {number * 2}.")

# While loop
secret_number = 6
guess = 0

print("\nGuess the secret number.")
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Correct! You guessed the secret number.")
        break
    else:
        print("That is not correct. Try again.")