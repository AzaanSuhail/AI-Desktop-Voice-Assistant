import pyttsx3
#pyttsx3 is python library which was made by Nitesh M bhatt and it converts text to Speech

import datetime #it is a inbuilt module in python's library
import speech_recognition as sr
import wikipedia
import webbrowser #inbuilt module this helps to contact to browser like google bing and all
import os #in this project it  is used for songs which are stored locally in our computer
import random #this is used to get the random song  which is stored locally in the system of a user  and to open vs code
import smtplib 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices') #getting details of your voices

# print(voices[0].id)    -->Note voices[0].id is a male voice whose name is David which inbuilt in your computer
# print(voices[1].id)   -->Female voice whose name is Hazel
#you can choose any one voice and you can add external voices also

engine.setProperty('voice',voices[0].id)
# engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis sir Desktop Voice Assistant how may i help you! ")
    
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()
    
def takeCommand():
    '''It takes microphone input and return string as output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=2 #means you can take upto max pause of 2 sec while speaking in between
        audio=r.listen(source)
        
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query
        
if __name__=="__main__":
    wishMe()
 #logic to execute
    while True:
        query=takeCommand().lower()
        
        if 'wikipedia'in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2) #this will return only 2 sentences form the whole wikipedia
            speak("According to Wikipedia")
            print("results")
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open geeks for geek' in query:
            webbrowser.open("https://www.geeksforgeeks.org/") 
        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com/")
        elif 'open notion' in query:
            webbrowser.open("https://www.notion.so/Oops-a371bf35538e4a08b69a6b4bc7c268d7")
        elif 'open github' in query:
            webbrowser.open("https://github.com/AzaanSuhail")
        # elif 'play music' in query:
        #     music_dr="D:\\Non Critical\\songs\\favouritesongs"
        #     songs=os.listdir(music_dr)
        #     print(songs)
        #     rand=random.randint(1, 30)
        #     os.startfile(os.path.join(musc_dir,songs[rand]))
        
        # i don't have songs locally in my computer thats why i just mention the way to play song
        elif 'open LeetCode' in query:
            webbrowser.open("https://leetcode.com/")
        elif 'open Geeks for Geeks' in query:
            webbrowser.open("https://www.geeksforgeeks.org/")
        elif 'open MDN documentation' in query:
            webbrowser.open("https://developer.mozilla.org/en-US/")
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'open Linkedin' in query:
            webbrowser.open("https://www.linkedin.com/in/azaan-suhail-272230239/")
        elif 'the time' in query:
            now_time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir right now time is {now_time}")
        elif 'open vscode' in query:
            vs_code_path="C:\\Users\\Azaan Suhail\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_code_path)
        elif 'open postman' in query:
            post_man_path="C:\\Users\\Azaan Suhail\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Postman\\Postman.exe"
            os.startfile(post_man_path)
            
        #you can send email to any body using smtp lib python library
        
        #---------------------Further addition will be done very shortly-----------------------------#
            
