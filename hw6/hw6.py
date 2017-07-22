#hw6.py
# Student Health Record System
# EECS 12, Fall 2013
# Mario Ruiz ID: 46301389


import math
from graphics import *


# The function should return the button number selected
def checkClickPosition(click):
# TODO: click is the Point from the user mouse click
    if click.x >=44 and click.x<=56 and click.y>=33 and click.y<=37:
        button=1
    if click.x >=44 and click.x<=56 and click.y>=28 and click.y<=32:
        button=2
    if click.x >=44 and click.x<=56 and click.y>=23 and click.y<=27:
        button=3
    if click.x >=44 and click.x<=56 and click.y>=18 and click.y<=22:
        button=4
    if click.x >=44 and click.x<=56 and click.y>=13 and click.y<=17:
        button=5
    if click.x >=44 and click.x<=56 and click.y>=3 and click.y<=7:
        button=6

    return button

def convertToBMI(weight, height):
    bmi = weight / (height *height) * 703
    return bmi

def bmiResult(bmi):
#TODO: Check what BMI category the student is using bmi
    if bmi<= 18.5:
        bmiresult="Underweight"
    elif 18.5<bmi<=24.9:
        bmiresult="Normal weight"
    elif 25<bmi<=29.9:
        bmiresult="Overweight"
    elif bmi>=30:
        bmiresult="Obese"
    
    return bmiresult

def targetWeight(bmi, weight, height):
    optimalweight =0
    if  18.5 > bmi or bmi > 25:
        optimalbmi = (18.5+24.9)/2
        #TODO:
        #Calculat the optimal weight using optimalbmi, height and weight
        optimalweight=((height*height)*21.7)/703
        return optimalweight
    else:
        return weight


def main():
    win = GraphWin("Student Health Record System", 600, 400)
    win.setCoords(0.0, 0.0, 60, 40)
    textFn = Text(Point(6, 35), "File Name:")
    textFn.draw(win)
    textId = Text(Point(6, 31), "Student ID:")
    textId.draw(win)
    textName = Text(Point(6, 27), "Student Name:")
    textName.draw(win)
    textWeight = Text(Point(6, 23), "Weight(Lbs):")
    textWeight.draw(win)
    textHeight = Text(Point(6, 19), "Height(Inches):")
    textHeight.draw(win)
    bmiLetter = Text(Point(6, 15), "BMI Category:")
    bmiLetter.draw(win)

    
    textButtonOpen = Text(Point(50, 35), "Open")
    textButtonOpen.draw(win)
    textButtonAdd = Text(Point(50, 30), "Find Student")
    textButtonAdd.draw(win)
    textButtonFind = Text(Point(50, 25), "Add Student")
    textButtonFind.draw(win)
    textButtonSave = Text(Point(50, 20), "Change Weight")
    textButtonSave.draw(win)
    textButtonTarget = Text(Point(50, 15), "Advise Weight")
    textButtonTarget.draw(win)
    textButtonQuit = Text(Point(50, 5), "Quit")
    textButtonQuit.draw(win)
    textMessage = Text(Point(20, 5), "Enter the health record file name and click Open.")
    textMessage.setTextColor("Blue")
    textMessage.draw(win)
    
    buttonOpen = Rectangle(Point(56,33),Point(44,37))
    buttonOpen.draw(win)
    buttonFind = Rectangle(Point(56,28),Point(44,32))
    buttonFind.draw(win)
    buttonAdd = Rectangle(Point(56,27), Point(44,23))
    buttonAdd.draw(win)
    buttonSave = Rectangle(Point(56,22), Point(44,18))
    buttonSave.draw(win)
    buttonTarget = Rectangle(Point(56,17), Point(44,13))
    buttonTarget.draw(win)
    buttonQuit = Rectangle(Point(56,7), Point(44,3))
    buttonQuit.draw(win)
                          
    fnInput = Entry(Point(24, 35), 25)
    fnInput.draw(win)
    idInput = Entry(Point(24, 31),25)
    idInput.draw(win)
    nameInput = Entry(Point(24,27),25)
    nameInput.draw(win)
    weightInput = Entry(Point(24,23),25)
    weightInput.draw(win)
    heightInput = Entry(Point(24,19),25)
    heightInput.draw(win)
    bmiTextInput = Entry(Point(24, 15), 25)
    bmiTextInput.draw(win)

    #TODO: create all lists to be used in the program
    #studentList=[["id"],["name"],["lbs"],["in"],["BMI"]]
    studentList=[]
    while True: # This is the main loop
        click = win.getMouse()
        op = checkClickPosition(click)
		
        if op == 1: #click on Open
        #Operations for opening a file, read info into lists and close the file
            studentList=[]
            file=fnInput.getText()
            text=open(file,'r')
            with text as f:
                data= f.readlines()
                for i in data:
                    info=i.split()
                    studentList.append(info)
            textMessage.setText("File "+file+" opened.")
            text.close()
            ###INFO###
            info={}
            for i in range(len(studentList)):
                info[eval(studentList[i][0])]= studentList[i]
				
        elif op == 2: #click on Find
        #Operations for Finding a Student
            x=idInput.getText()
            if eval(x) in info: #If there exists a student with the Student ID
                textMessage.setText("Student with id "+x+" found in the system")
                student=info.get(eval(x))
                nameInput.setText(student[1]+' '+student[2])
                weightInput.setText(student[3])
                heightInput.setText(student[4])
                bmi=convertToBMI(eval(student[3]),eval(student[4]))
                category=bmiResult(bmi)
                bmiTextInput.setText(category)

            else: #If there is no student with the student ID
                textMessage.setText("Student with id "+x+" does not exist in the system")


         #Add Not Working
						
#        elif op == 3: #click on Add
#        #Operations for Adding a Student
#            x=idInput.getText()
#            if eval(x) in info: #If there exists a student with the student ID
#                textMessage.setText('Student id already exists in sytem') 
#            else :  #If there is no student with the student ID
#                name=nameInput.getText()
#                ID=idInput.getText()
#                textMessage.setText("Student "+name+' with id '+ID+' added into the system')
#                file=fnInput.getText()
#                text=open(file,'w')
#                weight=(student[3])
#                height=(student[4])
#                student[ID,name,weight,height]
#                text.write(student)
#                text.close
#                print(student)
              


        elif op == 4: #click on Change Weight
        #Operations for changing the weight of a student
            x=idInput.getText()
            if eval(x) in info : #If there exists a student with the student ID, change weight
                change=weightInput.getText()
                student[3]=change
                textMessage.setText('Updated the weight of student id '+x+' to '+change)
            else: #If there is no student with the student ID
                textMessage.setText("Student with id "+x+" does not exist in the system") 
				
        elif op == 5: #click on Advise Weight
        #Operations for checking a Student's weight
            x=idInput.getText()
            if eval(x) in info: # There exists a student with the given student ID
                student=info.get(eval(x)) 
                bmi=convertToBMI(eval(student[3]),eval(student[4]))
                weight=eval(student[3])
                height=eval(student[4])
                target=targetWeight(bmi,weight,height)
                if target == weight: #If the student is in the right weight range
                    textMessage.setText('Student is in the right weight range')            
                else: #If the student is underweight or overweight or obese
                    textMessage.setText('Student '+x+'s target weight is '+str(target)+'lbs.')
            else: #If there is no student with the student ID
                textMessage.setText("Student with id "+x+" does not exist in the system")
        elif op == 6: #click on Quit
            #Writing the lists to the file and get out of the main loop
            break
#        else:
#            # possible error conditions
#            
    win.close()

main()
