import time
start_time = time.time()

questFile = open('questFile.txt', 'r')
ansFile = open('ansFile.txt', 'r')

List_Of_Questions = [question.strip() for question in questFile.readlines()] # print(List_Of_Questions) list of questions
List_Of_Answers = [answer.strip() for answer in ansFile.readlines()] # print(List_Of_Answers) list of answers

score = 0

''' using zip() function is an iterator of tuples where the first item in each passed iterator is paired together,
    and then the second item in each passed iterator are paired together '''

for question, answer in zip(List_Of_Questions, List_Of_Answers):
    The_question = print(question, '\n')
    user_choice = input('Your answer: ')
    if user_choice == answer:
        print('Correct\n')
        score += 1
    else:
        print('Incorrect\n')
    print('---' * 50)

print("You got " + str(score) + "/" + str(len(List_Of_Questions)) +
      " correct and it talk you: " + str((time.time() - start_time)) + " seconds")

questFile, ansFile.close()