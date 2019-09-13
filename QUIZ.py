import json, sys
import time

print("Hello, Welcome to MURI'S QUIZ\n")

def menu():
    while True:
        menu = ("""
        1 - Computer Quiz
        2 - English Quiz
        3 - Maths Quiz
        4 - True Or False Quiz
        5 - Exit system\nYour Option: """)

        userchoice = input(menu)

        if userchoice == "1":
             Computer_Quiz()

        elif userchoice == "2":
            English_Quiz()

        elif userchoice == "3":
            Maths_Quiz()

        elif userchoice == "4":
             T_OR_F_Quiz()
            
        elif userchoice == "5":
            print("Goodbye")
            sys.exit()

        else:
            print("Command nor recognised, Please try again: ")


def Computer_Quiz():
  with open('ComputerQuestions.json') as f:
      data = json.load(f)
      exam = data["exam"]
      passed_score = 0
  for z in exam:
    print(z["question"])
    print(" a. " + z["a"])
    print(" b. " + z["b"])
    print(" c. " + z["c"])
    print(" d. " + z["d"])
    ans = input('\nPlease select from options a - d: ')
    if ans == z['answer']:
      passed_score  = passed_score+1
      print("Correct\n")
    else:
      print("Wrong. The Correct Answer is " + z["answer"])
        
  print("Result: "+ "Thank you for playing "+ " You got "+ str(passed_score) + " out of " + str(len(exam))+ " correct")
 
 
  print('\nTHANK YOU')
  print('Goodbye')


def English_Quiz():
  with open('EnglishQuestions.json') as f:
      data = json.load(f)
      exam = data["English"]
      passed_score = 0

  for z in exam:
    print(z["question"])
    ans = input('\nTrue Or False: ')
    if ans == z['answer']:
      passed_score  = passed_score+1
      print("Correct")
  
    else:
      print("Wrong. The Correct Answer is " + z["answer"])
        
  print("Result: "+ "Thank you for playing "+ " You got "+ str(passed_score) + " out of " + str(len(exam))+ " correct")


def Maths_Quiz():
  with open('MathQuestions.json') as f:
      data = json.load(f)
      exam = data["maths"]
      passed_score = 0

  for z in exam:
    print(z["question"])
    time.sleep (3)
    ans = input('\nYour Answer: ')
    if ans == z['answer']:
      passed_score  = passed_score+1
      print("Correct\n")
  
    else:
      print("Wrong. The Correct Answer is " + z["answer"])
        
  print("Result: "+ "Thank you for playing "+ " You got "+ str(passed_score) + " out of " + str(len(exam))+ " correct")

def T_OR_F_Quiz():
  with open('TrueorFalseQuestions.json') as f:
      data = json.load(f)
      exam = data["true_or_false"]
      passed_score = 0

  for z in exam:
    print(z["question"])
    ans = input('\nTrue Or False: ')
    if ans == z['answer']:
      passed_score  = passed_score+1
      print("Correct\n")
  
    else:
      print("Wrong. The Correct Answer is " + z["answer"])
        
  print("Result: "+ "Thank you for playing "+ " You got "+ str(passed_score) + " out of " + str(len(exam))+ " correct")

menu()
