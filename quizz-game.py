print("Welcome to Quizz Game")

play = input("Start the game? yes/no? ")

if play != "yes":
    quit()
    
print("Loading the game...")

user_answer = input("What does CPU stand for? ")
answer = ['central processing unit', "Central Processing Unit", "centralprocessingunit", "CentralProcessingUnit"]
str(answer)

if user_answer in answer:
    print("correct!")    
else:
    print("incorrect")