import pyttsx3
import speech_recognition as sr
import datetime
import microphone
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
#import PyAudio
import setuptools
#from setuptools._distutils.version import LooseVersion
from packaging.version import parse
version=parse('1.0.0')
#for checking the ipaddress
import socket
hostname = 'sanjana30agarwal@gmail.com'
try:
    host_ip = socket.gethostbyname(hostname)
    print(f'The IP address of {hostname} is {host_ip}')
except socket.gaierror as e:
    print(f'Error resolving hostname: {e}')



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source,timeout=5,phrase_time_limit=5)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-IN')
        print(f'User Said:{query}')
    except Exception as e:
        speak("Sorry,Say that again please")
        return None
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello I am jarvis how can I help you")

def sendEmail(to,content):
    server=smtplib.SMTP('smtplib.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sanjana30agarwal@gmail.com','Manjusanju@30')
    server.sendmail('sanjana30agarwal@gmail.com',to,content)
    server.close()

if __name__=="__main__":

    #query = takecommand()
    wish()
    #Logic Building
    while True:
        query = takecommand()
        #if query:
        query = query.lower()
        speak(f"Yes as your command : {query}")
        if "open notepad" in query:
          npath = "C:\\Windows\\system32\\notepad.exe"
          os.startfile(npath)
        elif "open adobe reader" in query:
          apath = "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat.exe"
          os.startfile(apath)
        elif "open command prompt" in query:
          cpath="C:\\Windows\\system32\\cmd.exe"
          os.startfile(cpath)
        #elif "open vs code" in query:
         # vpath = "C:\\Users\\User\\AppData\\Local\\Programs\\MicrosoftVSCode.exe"
          #os.startfile(vpath)
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey()
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            songs="C:\\Users\\User\\Music\\music"
            music=os.listdir(songs)
            rd=random.choice(music)
            os.startfile(os.path.join(songs,rd))
            #To play the music of some particular format
            #for play in music:
            #if play.endswith('mp3')
            #os.startfile(os.path.join(music,play)
        elif "ip address" in query:
            ip=get("https://api.ipify.org").text
            speak(f"Your IP address is{ip}")
        elif "wikipedia" in query:
            speak("Searching Wikipedia")
            query=query.replace('wikipedia'," ")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        #elif "open googlecollab" or "open googlecallapp" in query:
            #webbrowser.open("https://colab.research.google.com/")
        elif "open google" in query:
            speak("what should i search on google")
            cm=takecommand().lower()
            # Construct the Google search URL
            search_url = f"https://www.google.com/search?q={cm}"
            webbrowser.open(search_url)
        elif "send message" in query:
            speak("Please enter the number with country code")
            number=input()
            print(f'number is{number}')
            speak("Please enter the message you want to send")
            msg=input()
            print(f'enter message{msg}')
            speak("Enter the time at which you want to send the message")
            t=int(input())
            speak("Enter the minutes for the time")
            m=int(input())
            kit.sendwhatmsg(number,msg,t,m)
        elif "play songs on youtube" in query:
            speak("Enter the name of the song you want to play")
            s=input()
            kit.playonyt(s)
        elif "send email" in query:
            try:
                speak("what should i send in the email")
                content=takecommand().lower()
                to="newlectindia@gmail.com"
                sendEmail(to,content)
                speak("email has been send to the person")

            except Exception as e:
             print(e)
            speak("sorry email has not been send")

        elif "no thanks" in query:
            speak("Thankyou for using me ,Have a good day")
            sys.exit()

        speak("Do you have any other work")



















