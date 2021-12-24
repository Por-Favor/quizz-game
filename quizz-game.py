print("Welcome to Quizz Game")

play = input("Start the game? yes/no? ")

if play != "yes":
    quit()

rules = ('Rules: type answers with no Cap and space between each word')
print(rules) 
print("The game has started")

a1 = str(['central processing unit'])
a2 = str(['graphics processing unit'])
a3 = str(['random access memory'])
a4 = str(['read only memory'])
a5 = str(['hard disk drive'])
a6 = str(['solid state drive'])
a7 = str(['universal serial bus'])

user_answer = input("What does CPU stand for? ")
if user_answer in a1:
    print("correct!")    
else:
    print("incorrect!")

user_answer = input("What does GPU stand for? ")
if user_answer in a2:
    print("correct!")    
else:
    print("incorrect!")

user_answer = input("What does RAM stand for? ")
if user_answer in a3:
    print("correct!")    
else:
    print("incorrect!")
  
user_answer = input("What does ROM stand for? ")  
if user_answer in a4:
    print("correct!")    
else:
    print("incorrect!")

user_answer = input("What does HDD stand for? ")    
if user_answer in a5:
    print("correct!")    
else:
    print("incorrect!")

user_answer = input("What does SSD stand for? ")    
if user_answer in a6:
    print("correct!")    
else:
    print("incorrect!")

user_answer = input("What does USB stand for? ")    
if user_answer in a7:
    print("correct!")    
else:
    print("incorrect!")