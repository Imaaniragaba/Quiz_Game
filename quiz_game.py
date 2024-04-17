print("Welcome to quiz night in Bikini Bottom!")

playing = input("Do you want to play? Y or N: ").lower()

if playing != "y":
    quit()
print("Okay, let's play!")

score = 0

question = input("Who lives in a pineapple and under the sea? ")

if question.lower() == "spongebob squarepants":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

question = input("Who owns crusty crab restaurant? ")

if question.lower() == "mr. crabs":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

question = input("Who was the driving instructor in bikini bottom? ")

if question.lower() == "mrs. puff":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

question = input("Who was the most famous bodybuilder in bikini bottom? ")

if question.lower() == "larry":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

print(f'You got {score} questions correct!')
print(f'Your score: {score / 4 * 100}%')

