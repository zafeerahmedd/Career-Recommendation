import turtle
#import requests
import time
import numpy as np
import pandas as pd
import random
df=pd.read_excel('C:/Users/mohammed mubeen uddi/OneDrive/Desktop/Deployment/chat bott/sadq.xlsx')
df=df.loc[np.random.choice(df.index, size=1)]
df1=pd.read_excel('C:/Users/mohammed mubeen uddi/OneDrive/Desktop/Deployment/chat bott/hapq.xlsx')
df1=df1.loc[np.random.choice(df1.index, size=1)]
df3=pd.read_excel('C:/Users/mohammed mubeen uddi/OneDrive/Desktop/Deployment/chat bott/thoughts.xlsx')
df3=df3.loc[np.random.choice(df3.index, size=1)]
#df1 = df1.iloc[np.random.choice(np.arange(len(df1)), size=1)]
#print(df1)
#print(df1)
#create a window
window = turtle.Screen()
window.setup(1128,540)
window.bgpic('C:/Users/mohammed mubeen uddi/OneDrive/Desktop/Deployment/chat bott/bckg.gif')
window.title('therapy Genie')
#turtle for the heading
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color('tomato')
text.goto(195,195)
text.write("I am therapy genie ",align = 'center',font = ('Courier',23,'bold','italic'))
#turtle to write on the screen
ISS = turtle.Turtle()
ISS.hideturtle()
ISS.penup()
ISS.color('red')
ISS.right(90)
def write_on_screen(reply):
    display_message = []
    ISS.clear()
    ISS.goto(200,150)
    
    while len(reply)>40:
        for i in range(40,0,-1):
            if reply[i] == ' ':
                display_message.append(reply[0:i])

                reply = reply[i+1:]
                break
    display_message.append(reply)
    for i in display_message:
        ISS.write(i, align = 'center', font = ('Comic Sans MS',23,'italic'))
        ISS.forward(50)
def answer_question():
    reply = ''

    question = window.textinput('Hey!', 'what is your name')
answer_question()
time.sleep(1)
write_on_screen('that\'s a nice name')
time.sleep(1)
def write_on_screen2(reply):
    display_message = []
    ISS.clear()
    ISS.goto(250,-10)
    
    while len(reply)>100:
        for i in range(100,0,-1):
            if reply[i] == ' ':
                display_message.append(reply[0:i])

                reply = reply[i+1:]
                break
    display_message.append(reply)
    for i in display_message:
        ISS.write(i, align = 'center', font = ('Comic Sans MS',23,'italic'))
        ISS.forward(50)
def answer_question2():
    reply = ''
    question = window.textinput('Hey!', 'how was your day')
    classify=question
    
        
    if classify=='can\'t complain':
        reply=df
        
    elif classify=='good':
        reply=df1
    if classify=='not bad':
        reply=df
    elif classify=='fine':#quote
        reply=df1
        write_on_screen2(reply)
    time.sleep(3)
    reply=df3
    write_on_screen2(reply)
    write_on_screen2('\nhow was your day?\nfine\nnot bad\ncan\'t complain\ngood ')
    answer_question2()
def answer_question3():
        reply = ''

        question = window.textinput('Hey!', 'how are you feeling')
answer_question()
def write_on_screen3(reply):
        display_message = []
        ISS.clear()
        ISS.goto(250,-10)
        
        while len(reply)>100:
            for i in range(100,0,-1):
                if reply[i] == ' ':
                    display_message.append(reply[0:i])

                    reply = reply[i+1:]
                    break
        display_message.append(reply)
        for i in display_message:
            ISS.write(i, align = 'center', font = ('Comic Sans MS',23,'italic'))
            ISS.forward(50)
        def answer_question():
            reply = ''

            question = window.textinput('Hey!', 'Type your question here...')
            
            category = classify(question)

            if category == 'joy':
                reply = 'hope you remain joyful.'
            elif category == 'sad':
                reply = 'dont worry you will be happy'
            elif category == 'anger':
                reply = 'calm down, you will be fine'
            elif category == 'fear':
                reply='you are strong'
            elif category == 'bored':
                reply='get excited your life is full of surprises'
                
                write_on_screen3(reply)
                
                time.sleep(2)
                turtle.bye()
                return
            elif category == 'Error':
                return
            else:
                reply = 'That"s out of space syllabus'
            write_on_screen3(reply)
answer_question3()
def classify(question):
    
        if question == None:
            return 'Error'
        key = "7C5ff8512710e721007647f49a/f5ce7de0-7083-11ec-a0f5-732126ee3369"
        url = 'https://machinelearningforkids.co.uk/api/scratch/'+key+'/classify/'
    
    
        
#answer_question()   



