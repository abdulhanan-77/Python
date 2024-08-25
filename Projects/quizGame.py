print("Welcome to the Game!")

playing = input("Do you want to play? yes/no: ")

if playing.lower() != "yes":
    quit()

print("Let's Start")
score = 0
answer = input("What is the capital of Pakistan? ")

if answer.lower() == "islamabad":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of UK? ")

if answer.lower() == "london":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Iran? ")

if answer.lower() == "tehran":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
 
print("You got", str(score), "questions correct!")
print("You got", str((score/4)*100), "%.")
