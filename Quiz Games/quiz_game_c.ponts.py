print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

#question1
answer = input("What color is the sun? ")
if answer.lower() == "yellow":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#question2
answer = input("What color is the ocean? ")
if answer.lower() == "blue":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#question3
answer = input("What color is moom? ")
if answer.lower() == "white":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "%.")