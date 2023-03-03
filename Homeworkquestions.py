
from tkinter import *
import random


def multiplicationmathqueustions():
    count = 0
    answers = []
    answersdict = dict()
    answersheet = dict()
    gradecount = 0
    while count < 5:
        file1 = open('Questions2.txt', 'w')
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        questions = number1*number2
        file1.write(str(questions) + '\n')
        print("what is %d Times %d" % (number1, number2))
        answer = input()
        answersdict[answer] = 1
        answers.append(answer)
        file1.close()
        file1 = open('Questions2.txt', 'r')
        for line in file1:
            line = line.rstrip()
            answersheet[line] = 1
        count += 1
        file1.close()
    if answersdict == answersheet:
        print("100")
    else:
        for b in answers:
            if b in answersheet:
                gradecount += 1
        if gradecount == 4:
            print("Your Grade is 80")
        elif gradecount == 3:
            print("Your Grade is 60")
        elif gradecount == 2:
            print("Your Grade is 40")
        elif gradecount == 1:
            print("Your Grade is 20")
        elif gradecount == 0:
            print("Your Grade is 0")


def additionmathquestions():
    count = 0
    grade = 0
    while count < 10:
        file1 = open('Questions1.txt', 'w')
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        questions = number1+number2
        file1.write(str(questions) + '\n')
        print("what is %d plus %d" % (number1, number2))
        answer = input()
        file1.close()
        file1 = open('Questions1.txt', 'r')
        for line in file1:
            if int(line) == int(answer):
                grade += 1
        count += 1
        file1.close()
    print(grade)
    if grade == 10:
        print("Your Grade is 100")
    elif grade == 9:
        print("Your Grade is 90")
    elif grade == 8:
        print("Your Grade is 80")
    elif grade == 7:
        print("Your Grade is 70")
    elif grade == 6:
        print("Your Grade is 60")
    elif grade == 5:
        print("Your Grade is 50")
    elif grade == 4:
        print("Your Grade is 40")
    elif grade == 3:
        print("Your Grade is 30")
    elif grade == 2:
        print("Your Grade is 20")
    elif grade == 1:
        print("Your Grade is 10")
    elif grade == 0:
        print("Your Grade is 0")


def homework():
    print("choose to do either multiplication or addition math")
    choice = input()
    if choice == 'addition':
        additionmathquestions()
    elif choice == 'multiplication':
        multiplicationmathqueustions()


def login():
    window = Tk()

    def ButtonFunction():
        window.destroy()
    usernameget = StringVar()
    passwordget = StringVar()
    okbtn = Button(window, text="Login", command=ButtonFunction)

    usernameentry = Entry(window, text="enter username", textvariable=usernameget)
    passwordentry = Entry(window, text="enter password", textvariable=passwordget)

    okbtn.grid(row=3, column=1)

    usernameentry.grid(row=0, column=1)
    passwordentry.grid(row=1, column=1)
    window.mainloop()
    username = usernameget.get()
    password = passwordget.get()
    return username, password


def logincheck(username, password):
    users = open("Final_Users.txt")
    for line in users:
        fileusername = line.split('::')[0]
        filepassword = line.split('::')[1]
        if username == fileusername:
            if password == filepassword:
                print("user has logged in")
                homework()
            else:
                login()
        else:
            login()


username, password = login()
logincheck(username, password)
