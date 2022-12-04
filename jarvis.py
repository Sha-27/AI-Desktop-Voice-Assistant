import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import os
import webbrowser 
import smtplib
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    """ To make our system speak"""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """ To wish us based on the time."""
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning mam!")
    elif hour >=12 and hour<=14:
        speak("Good Afternoon mam!")
    elif hour >14 and hour <=18:
        speak("Good evening mam!")
    else:
        speak("Good night mam!")
    speak("Iam jarvis, Iam your personal assistant, Tell me what should I do")


def takeCommand():
    """It takes microphone input from the user and returns string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language="en-in") #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
def sendEmail(to, content):
    """ It sends mail """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('194g1a05a0@srit.ac.in', '194G1A05A0@srit')
    server.sendmail('194g1a05a0@srit.ac.in', to, content)
    server.close()
if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower() 

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)  
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google classroom" in query:
            webbrowser.open("classroom.google.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir="E:\songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))      
        elif "the time" in query:
            strTime= datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"mam,the time is {strTime}")
        elif "open code" in query:
            codepath="C:\\Users\\Shahida\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "who are you" in query:
            speak("Iam jarvis, Iam your personal assistant, Tell me what should I do")
        elif 'email to shahida' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shaikshahida71342@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry mam . I am not able to send this email")            