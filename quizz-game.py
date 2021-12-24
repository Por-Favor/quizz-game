print("Welcome to ICT Quizz Game")

play = input("Start the game? yes/no? ")

if play != "yes":
    quit()

rules = ('Rules: type answers with no Cap and space between each word')
print(rules) 
print("The game has started")

mark = 0

user_answer = input("What does CPU stand for? ")
if user_answer == 'central processing unit':
    print("correct!")
    mark += 1    
else:
    print("incorrect!")

user_answer = input("What does GPU stand for? ")
if user_answer == 'graphics processing unit':
    print("correct!")
    mark += 1    
else:
    print("incorrect!")

user_answer = input("What does RAM stand for? ")
if user_answer == 'random access memory':
    print("correct!")
    mark += 1    
else:
    print("incorrect!")
  
user_answer = input("What does ROM stand for? ")  
if user_answer == 'read only memory':
    print("correct!")
    mark += 1    
else:
    print("incorrect!")

user_answer = input("What does HDD stand for? ")    
if user_answer == 'hard disk drive':
    print("correct!")
    mark += 1    
else:
    print("incorrect!")

user_answer = input("What does SSD stand for? ")    
if user_answer == 'solid state drive':
    print("correct!")
    mark += 1    
else:
    print("incorrect!")

user_answer = input("What does USB stand for? ")    
if user_answer == 'universal serial bus':
    print("correct!")
    mark += 1    
else:
    print("incorrect!")

total_question = 7
print("Total score: " + str(mark) + "/7")
print("Percentage: " + str(round((mark/total_question)*100)) + "%")