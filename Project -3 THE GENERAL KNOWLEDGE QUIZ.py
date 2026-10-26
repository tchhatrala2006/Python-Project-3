
import random as r

l=[
       'Which keyword checks multiple conditions?',
       'Which loop repeats a fixed number of times?',
       'Which loop runs while a condition is True?',
       'Which keyword exits a loop?',
       'Which keyword skips the current iteration?'


]
score=0
for i in range(1,6):
    question=r.choice(l)
    print(question)
    answer=input("Enter the Answer: ")

    if question=='Which keyword checks multiple conditions?' and answer=='elif':
        print(f"Correct Answer: {answer}")
        score+=1
    elif question=='Which keyword exits a loop?' and answer=='break':
        print(f"Correct Answer: {answer}")
        score+=1
    elif question=='Which loop runs while a condition is True?' and answer=='while':
        print(f"Correct Answer: {answer}")
        score+=1
    elif question=='Which keyword skips the current iteration?' and answer=='continue':
         print(f"Correct Answer: {answer}")
         score+=1
    elif question=='Which loop repeats a fixed number of times?' and answer=='for':
        print(f"Correct Answer: {answer}")
        score+=1
    elif question == 'Who created Python?' and answer == 'Guido van Rossum':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'In which year was Python first released?' and answer == '1991':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'What keyword is used to print output in Python?' and answer == 'print':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == ' What function is used to take user input?' and answer == 'input':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == ' What is the extension of a Python file?' and answer == '.py':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Is Python case-sensitive?' and answer == 'Yes':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which data type stores text?' and answer == 'str':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which data type stores whole numbers?' and answer == 'int':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which data type stores decimal numbers?' and answer == 'float':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which data type stores True or False?' and answer == 'bool':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'What is the output of print(5 + 3)?' and answer == '8':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'What is the output of print(10 // 3)?' and answer == '3':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'What is the output of print(10 % 3)?' and answer == '1':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which operator checks equality?' and answer == '==':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which operator means "not equal"?' and answer == '!=':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which keyword is used for decision making?' and answer == 'if':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which keyword is used when the first condition is false?' and answer == 'else':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which function returns the length of a string or list?' and answer == 'len':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which function converts a string to lowercase?' and answer == 'lower':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'What function converts a string to uppercase?' and answer == 'upper':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which function removes whitespace from both ends of a string?' and answer == 'strip':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which operator is used for exponentiation in Python?' and answer == '**':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'What is the output of print(2 ** 3)?' and answer == '8':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which function converts a string to an integer?' and answer == 'int':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which function converts an integer to a string?' and answer == 'str':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which function returns the type of a variable?' and answer == 'type':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which keyword is used to define a function?' and answer == 'def':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which keyword is used to return a value from a function?' and answer == 'return':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'What is the default return value of a function with no return statement?' and answer == 'None':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which data type is immutable: List or Tuple?' and answer == 'Tuple':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which brackets are used to create a list?' and answer == '[]':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which brackets are used to create a tuple?' and answer == '()':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which brackets are used to create a dictionary?' and answer == '{}':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which brackets are used to create a set?' and answer == '{}':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which method adds an element to a list?' and answer == 'append':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which method removes the last element from a list?' and answer == 'pop':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which method sorts a list?' and answer == 'sort':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which method reverses a list?' and answer == 'reverse':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which function finds the maximum value in a list?' and answer == 'max':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which function finds the minimum value in a list?' and answer == 'min':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which function calculates the sum of a list?' and answer == 'sum':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which function sorts without modifying the original list?' and answer == 'sorted':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which keyword is used to create a class?' and answer == 'class':
        print(f"Correct Answer: {answer}")
        score += 1
    elif question == 'Which special method acts as a constructor in Python?' and answer == '__init__':
        print(f"Correct Answer: {answer}")
        score += 1


    else:
        print(f"Wrong Answer: {answer}")
        
print(score)


