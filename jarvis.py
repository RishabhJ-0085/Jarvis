import pyttsx3 # if you install old version try this pip install [package name]==version : current Version: 2.90
import datetime # if you upgrade library try this pip install [package name] --upgrade
import os
import math
from Intro import play_gif
import serial
import time
import random
import string
import requests
import speedtest
import psutil
from pywikihow import search_wikihow
import pyautogui as auto
import operator
import PyPDF2
from playsound import playsound
from bs4 import BeautifulSoup
import pyjokes as jk
import pywhatkit as kit
import wikipedia as wi
import webbrowser as wbe
import speech_recognition as sr
import phonenumbers as num
import folium
from phonenumbers import geocoder,carrier
from  opencage.geocoder import OpenCageGeocode
import threading
import queue
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('volume',20)

def speck(audio):
    engine.say(audio)
    engine.runAndWait()
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as sours:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(sours, timeout=10, phrase_time_limit=15)
    try:
        print("Recognizing.....")
        qeury = r.recognize_google(audio, language = 'en-in')
        print(f"you say-{qeury}")
    except Exception as e:
        """speck("Say Again Please")"""
        return 'none'
    return qeury
def wish():
    hour = datetime.datetime.now().hour
    time = datetime.datetime.now()
    times = str(time.strftime("%H:%M %p"))
    Time = str(time.strftime("%D"))
    if hour>=0 and hour<=12:
        speck(f"Good Morning Sir... its {times}")
    elif hour>12 and hour<16:
        speck(f"Good Afternoon Sir... its {times}")
    else:
        speck(f"Good Evening Sir... its {times}")
    if  "" in Time: # Your birtha:- month/date
        with open('Python Code\\JARVIS\\Birthaday.txt','r') as file:
            reed = file.read()
            if not reed: 
                speck("Wish you very very Happy birthday! sir this is for you")
                os.system(f"start chrome.exe {kit.playonyt("Happy birthaday song")}")
                with open('Python Code\\JARVIS\\Birthaday.txt','a') as file:
                    file.write("ok")
    else:
         with open('Python Code\\JARVIS\\Birthaday.txt','w') as file:
            file.close()
    speck("How can I help you")
def scheduled ():
    try:
        print("Do you want to clear old task")
        speck("Do you want to clear old task")
        asked = TakeCommand().lower()
        if "yes" in asked or "han" in asked:
            speck("Ok sir old task clear")
            file = open('Python Code\\JARVIS\\Scheduled.txt','w')
        else:
            speck("Ok sir")
        speck("Sir please Enter Number of task")
        no_task = int(input("Enter Number of task"))
        for i in range(no_task):
           speck(f"sir say No{i} task")
           askeds = TakeCommand().lower()
           #Scheduled.append(askeds)
           file = open('Python Code\\JARVIS\\Scheduled.txt','a')
           file.write(f"{i+1}.{askeds}\n")
        speck("schedule saved")
        file.close()
    except Exception:
        speck("Sorry sir try again")
def chrome(search):
    chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  
    wbe.register('chrome', None, wbe.BackgroundBrowser(chromePath))  
    web = wbe.get('chrome')  
    web.open(f"https://www.google.com/search?q={search}")
def Weather(city):
    citys = city.replace(" ","+")
    url = f"https://wttr.in/{citys}?format=%C+%t+%h"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        return f"AN error occurred:{e}"
def Arduino():
    try:
        while True:
            ser = serial.Serial('COM6',9600,timeout = 1)
            speck("say what you want to control")
            query = TakeCommand().lower()
            if ser is None:
                speck("disconnect Arduino")
            else:
                if "get back to work" in query or "stop" in query:
                    speck("Ok sir")
                    break
                elif "open" in query:
                    speck("ok sir helmet open")
                    ser.write(b'Helmet open') # or you have to use this // query.encode() \\ for text to convort into bytes
                elif "close" in query:
                    speck("ok sir Helmet close")
                    ser.write(b'Helmet close')
                elif "on" in query:
                    speck("Ok sir light ON")
                    ser.write(b'Light on')
                elif "off" in query:
                    speck("OK sir Light off")
                    ser.write(b'Light off')
    except Exception as e:
        speck("please connect Arduino")
def pdf(PDF_Read):
    # Open the PDF file in read-binary mode
    pdf_path = 'C:\\Users\\jaisw\\Downloads\\{PDF_Read}.pdf'
    
    # Check if the file exists
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as book:
            # Initialize the PDF reader
            read = PyPDF2.PdfReader(book)
            pages = len(read.pages)  # Get the number of pages
    
            # Print the total number of pages
            print(f"Total number of pages in this PDF is {pages}")
            
            # Get user input for the page number
            try:
                pgN = int(input(f"Enter page number (1 to {pages}): "))
                
                # Check if the entered page number is valid
                if pgN < 1 or pgN > pages:
                    print(f"Invalid page number. Please enter a number between 1 and {pages}.")
                else:
                    # Extract text from the specified page
                    page = read.pages[pgN - 1]  # PyPDF2 pages are 0-indexed
                    text = page.extract_text()
                    
                    # Print the extracted text
                    print(text)
                    speck(text)
            except ValueError:
                speck("Please enter a valid integer for the page number.")
    else:
        speck(f"File not found. Please check the file path.")
    
def location(numbers):
    key = "2ef0bd6a90d34d4aa09faf3fdd5a0f93"
    phone_number = num.parse(numbers)
    phone1 = geocoder.description_for_number(phone_number,"en")
    phone2 = carrier.name_for_number(phone_number,"en")
    print(f"\nPhone Number Location ={phone1}\n{phone2}\n")
    geocoders = OpenCageGeocode(key)
    query = str(phone1)
    results = geocoders.geocode(query)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    """print(lat,lng)"""
    myMap = folium.Map(location=[lat,lng],zoom_start=10)
    folium.Marker([lat,lng],popup = phone1).add_to(myMap)
    myMap.save("JARVIS\\Locastion.html")
def takeCommand():
    wish()
    while True:
        query = TakeCommand().lower()
        if "hello jarvis" in query or "hey jarvis" in query:
            speck("Hello Sir How can I help you")
        elif "pagal" in query or "chor" in query or "gavar" in query or "bevkuf" in query or "bekar" in query:
            speck("sorry sir but i try my best")
        elif "open" in query:
            Remove =['jarvis','open','or','karo','and','ko','sabko','fatafat','my','youtube','google','chrome','wikipedia']
            for remove in Remove:
                query = query.replace(remove,"")
            a = query.strip()
            word = a.lower().strip().split()
            Local = ['download file','video file']
            Found_web = [app for app in word if all(Remove not in app for Remove in ['download','file','video'])]
            Found_local = [file for file in Local if file in a.strip()]  
            if Found_local:
                for a in Found_local:
                    a = a.replace("file","").strip().capitalize()
                    print(a)
                    speck(f"ok sir open {a}")
                    os.startfile(f"C:\\Users\\jaisw\\{a}s")
            if Found_web:
                for a in Found_web:
                    speck(f"ok sir open {a}")
                    os.system(f"start chrome.exe www.{a}.com")
        elif "what are you doing" in query or "kya kar rahe ho" in query:
            speck("i follow your commands sir ")
        elif "time" in query or "samay" in query:
             time1 = datetime.datetime.now()
             times2 = str(time1.strftime("%H:%M %p"))
             print(f"Sir.. its {times2}")
             speck(f"Sir.. its {times2}")
        elif "aaj ka date" in query or "aaj ki tarik" in query or "today date" in query or "aaj ki date" in query:
             time = datetime.datetime.now()
             time = str(time.strftime("%D"))
             print(f"Sir.. its {time}")
             speck(f"Sir.. its {time}")
        elif "jarvis" == query:
            speck("Yes sir what can i do for you")
        elif "thanks" in query or "thank" in query or "shukriya" in query :
            speck("wellcome sir")
        elif "kaise ho" in query or "how are you" in query:
            speck("I am fine sir, and you")
            query = TakeCommand().lower()
            if "achcha" in query or "good" in query:
                speck("Its very nice")
            else: speck("OK sir")
        elif "who are you" in query or "tum kaun ho" in query or "introduction" in query or "introduce" in query:
            speck("Hello, Now may I introduce my self, I am Jarvis a virtual artificial intelligence assistant, I can do any this on bace my program ,let me explane I do search any think on Google , Wikipedia and YouTube and i can open any apps , open some files ,and chacking tempeartuer and battery charging")
        elif "joke" in query:
            j = jk.get_joke()
            print(j)
            speck(j)
        elif "bad" in query:
            speck("Sorry sir but i try my best")
        elif "good" in query or "nice" in query:
            speck("Thanks sir")
        elif "youtube" in query:
            Somg = ['jarvis','search','karo','youtube','open','kholo','ok','per','de']
            Yes = "OK" if 'search' in query else "No"
            for word in Somg:
                query = query.replace(word,"")
                query = query.replace('search on',"")
            query = query.strip()
            if not query:
                if Yes == "No":
                    speck("Sir, You want search any think")
                    ask = TakeCommand().lower()
                    if "yes" in ask or "han" in ask:
                        speck("Sir please say what you want search in YouTube")
                        search = TakeCommand().lower()
                        search = search.replace(" ","+")
                        speck("OK sir searching on youtube")
                        os.system(f"start chrome.exe www.youtube.com/results?search_query={search}")
                    else:
                        speck("OK sir Open youTube")
                        os.system(f"start chrome.exe www.youtube.com")
                else:
                    speck("Sir please say what you want search in YouTube")
                    search = TakeCommand().lower()
                    while search == 'none':
                        speck("Sir please say what you want search in YouTube")
                        search = TakeCommand().lower()
                    search = search.replace(" ","+")
                    speck("OK sir searching on youtube")
                    os.system(f"start chrome.exe www.youtube.com/results?search_query={search}")
            else:
                query = query.replace(" ","+")
                speck("Ok sir searching on youtube")
                os.system(f"start chrome.exe www.youtube.com/results?search_query={query}")
        elif "favourite song" in query or "my favourite song" in query:
            speck("ok sir playing your favourite song")
            """ music_dir = "C:\\Users\\jaisw\\Music"
            rn = random.choice(music_dir)"""
            os.startfile("C:\\Users\\jaisw\\Music\\Spotify.mp3")
        elif "generate password" in query or "make passward" in query:
            speck("Sir witch password you want to make it Number or Character")
            ask = TakeCommand().lower()
            if "numbers" in ask or "number" in ask:
               speck("Sir how many digits you want please Enter")
               Numbers = int(input("Enter Number of digits you want:-"))
               num = ''.join(random.choices(string.digits,k=Numbers))
               speck(f"sir Her is password {num}")
               print(f"Her is a password:-{num}")
            elif "character" in ask or "characters" in ask:
               speck("Sir how many Character you want please Enter")
               Numbers = int(input("Enter Number of Character you want:-"))
               Char = ''.join(random.choices(string.ascii_uppercase, k=Numbers))
               speck(f"sir Her is password {Char}")
               print(f"Her is a password:-{Char}")
            else:
                speck("sorry sir try again")
        elif "spotify" in query:
            speck("OK sir open spotify")
            os.system("start spotify.exe")
        elif "play" in query:
            Somg = ['jarvis','play','karo','video','music']
            for word in Somg:
                query = query.replace(word,"")
            query = query.strip()
            if not query:
                speck("witch song or video play")
                song = TakeCommand().lower()
                for word in Somg:
                    song = song.replace(word,"")
                speck("Ok sir playing this video")
                os.system(f"start chrome.exe {kit.playonyt(song)}")
            else:
                speck("OK sir play this")
                os.system(f"start chrome.exe {kit.playonyt(query)}")
        elif "pw" in query:
            speck("Ok Sir open PW app, you have to wait for a second")
            os.system("start chrome.exe www.pw.live/study/batches/study")
        elif "make schedule" in query or "make my schedule" in query:
            scheduled()
        elif "show my schedule" in query or "what is my schedule" in query:
            file = open('Python Code\\JARVIS\\Scheduled.txt','r')
            a = file.read()
            print(a)
            speck(a)
        elif "chrom" in query or "google" in query:
            try:
                my = ['jarvis','search','google',' on ','chrome','per','karo','can','in']
                command = query
                for word in my:
                   command = command.replace(word,"")
                command = command.strip()
                if not command:
                    while True:
                        speck("sir what you want to search")
                        command = TakeCommand().lower()
                        if command and command!= "none":
                            break
                speck(f"are you searching {command}")
                confirmation = TakeCommand().lower()
                if "yes" in confirmation or "search" in confirmation:
                    speck("OK sir searching on chrom ... Please wait for a second..")
                    chrome(command)
                else:
                    speck("Stop searching")
            except Exception as e:
                speck("sorry sir please say again")
        elif "close" in query:
            try:
               speck("Ok sir closeing chrom")
               os.system("taskkill /f /im chrome.exe")
            except:
                speck("sir chrome is already close")
        elif "calculate" in query or "calculator" in query:
                try:
                    Replace = ["jarvis","calculate","karo","what","is"]
                    for word in Replace:
                        query = query.replace(word,"").strip()
                    if not query:
                        speck("say what i calculate")
                        query = TakeCommand().lower()
                    query = query.replace("multiple","*").replace("divide","/").replace("x","*").replace("^","**").replace("power by","**")
                    result = eval(query)
                    speck(f"Result is{result}")
                    print("Result is", result)
                except Exception:
                    speck("Please say again somthing is wrong in your query")
        elif "open wikipedia" in query or "wikipedia" in query:
            try:
                Q_remove = ['jarvis','search on','wikipedia','per','search','karo','now','ok','open']
                for word in Q_remove:
                    query = query.replace(word,"")
                query = query.strip()
                if not query:
                    while True:
                        speck("What i search on wikipedia")
                        query = TakeCommand().lower()
                        if query and query!= 'none':
                            break
                    for word in Q_remove:
                        query = query.replace(word,"")
                    query = query.strip()
                wikipedia = wi.summary(query, sentences = 2)
                speck("ok sir")
                speck("sir can i print this")
                query = TakeCommand().lower()
                if "print" in query or "yes" in query or "han" in query:
                  speck("ok sir")
                  print(wikipedia)
                speck(f"accoting to wikipedia {wikipedia}")
            except Exception as es:
                speck(f"Sorry sir but i can not understand ")
                print(es)
        elif "cmd" in query:
            speck("ok sir open command prompt")
            os.system("start cmd")
        elif "sleep" in query or "so jao" in query or "good night" in query:
            speck("OK Sir you can call me any time")
            break
        elif "location" in query:
            speck("sir please enter number with contery number")
            try:                
              number = input("Enter number:")
              speck("OK sir tracking this number")
              location(number)
              speck("Sir location track Successfully you see that")
              os.startfile("Python Code\\JARVIS\\locastion.html")
            except Exception as e:
                speck(e)
                print(e)
        elif "meet" in query:
            my = ["my","friends","friend","jarvis meet","meet","sister","brother"]
            command = query
            for word in my:
                command = command.replace(word,"")
            if "rishabh" in command:
                speck("Oh sir its you!")
            elif "jarvis" in command:
                speck("Oh! sir its..my name")
            else:
                speck(f"Hello i am jarvis nice to meet you {command}")
        elif "yahan ka temperature" in query or "temperature" in query:
            try:
                Stop_Word = ["temperature","ka","jarvis","batao","in"]
                search = query
                for word in Stop_Word:
                    search = search.replace(word,"").strip()
                if not search:
                    speck("Sir please tell me City Name")
                    search = TakeCommand().lower()
                if "yahan" in search:
                    search = "Nautanwa"
                speck("please wait for a second")
                temp = Weather(search)
                print(f"current {search} is\n {temp}")
                speck(f"current {search} is {temp}")
            except Exception:
                speck("Sorry sir but something is wrong")
        elif "internet" in query:
            try:     
                speck("please wait sir i checkout")
                st = speedtest.Speedtest()
                dow = int(st.download()/1048576)  #Megabyte = 1024*1024 bytes
                UP = int(st.upload()/1048576)
                print(f"sir we have {dow} bit per second downloading speed \n{UP} bit per second uploading speed")
                speck(f"sir we have {dow} bit per second downloading speed and..... {UP} bit per second uploading speed")
            except Exception as e:
                speck(f"sorry sir but internet is verry slow i can not findout{e}")
        elif "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            if percentage<40:
             print(f"Sir our system have {percentage} percent battery")
             speck(f"Sir our system have {percentage} percent battery..... please charge")
            elif 40<percentage<70:
             print(f"Sir our system have {percentage} percent battery")
             speck(f"Sir our system have {percentage} percent battery.... after some time please charge")
            else:
                print(f"Sir our system have {percentage} percent battery")
                speck(f"Sir our system have {percentage} percent battery")
        elif "volume up" in query:
            auto.press("volumeup")
            speck("volume up")
        elif "volume down" in query:
            auto.press("volumedown")
            speck("volume down")
        elif "mute" in query:
            auto.press("volumemute")
        elif "control" in query:
            Arduino()
        elif "pdf" in query:
            speck("say file name")
            files = TakeCommand().lower()
            pdf(files)
        elif "remember that" in query or "yad karo" in query:
            list =["jarvis","yad karo","remember that"]
            Remember = query
            for word in list:
                Remember = Remember.replace(word,"")
            speck("Sir can i replace this to old text")
            ask =  TakeCommand().lower()
            if "nahin" in ask or "no" in ask or "mat karo" in ask:
               Write = open('JARVIS\\Remember.txt','a')
               Write.write(f"{Remember}\n")
               Write.close() 
            elif "yes" in ask or "han" in ask:
                Write = open('Python Code\\JARVIS\\Remember.txt','w')
                Write = open('Python Code\\JARVIS\\Remember.txt','a')
                Write.write(f"{Remember}\n")
                Write.close() 
            speck(f"Sir i remember{Remember}")
        elif "what you remember" in query or "yad rakhne" in query:
            Write = open("Python Code\\JARVIS\\Remember.txt","r")
            Remember = Write.read()
            print(Remember)
            speck("you told me Remember that"+Remember)
        elif "system" in query:
            speck("Sir first sleep   ME")
        elif "stop" in query or "ruko" in query:
            pass
        elif "say" in query or "repeat" in query:
            query = query.replace('jarvis',"")
            query1 = query.replace('say', "")
            quer = query1.replace('repeat',"")
            speck(quer)
        elif "how to do mode" in query:
            speck("How to do mode is activate")
            while True:
                speck("please tell me what you want to know")
                try:
                    how = TakeCommand().lower()
                    if "exit" in how or "close" in how or "deactivate" in how:
                        speck("ok sir how to mode is close")
                        break
                    else:
                        ma = 1
                        leng = "en-hi"
                        how_do = search_wikihow(how,ma,leng)
                        assert len(how_do) == 1
                        how_do[0].print()
                        speck(how_do[0].summary)
                except Exception as e:
                    speck("Sorry sir, but i am not able to find this")
        elif "who create you" in query or " tumko kisne banaya" in query or "who make you" in query:
            speck("He is biggest fan Iron man,.. The one anonly,.. RJ Rishabh Jaiswal")
        elif "learn" in query:
            Remove = ["jarvis","learn","karo"]
            for word in Remove:
                query = query.replace(word,"")
            learn = query.strip()
            if not learn:
                speck("sir you want write or speeck")
                Question = TakeCommand().lower()
                if "write" in Question or "text" in Question:
                    speck("Ok sir please write")
                    learn = input("Enter:- ")
                else:
                    speck("Ok sir say what i learn?")
                    learn = TakeCommand().lower()
            with open("Python Code\\JARVIS\\learn.txt",'a') as file:
                file.write(f"{learn}\n")
                speck("done sir")
        else:
            Remove = ["jarvis","tell me"]
            for word in Remove:
                query = query.replace(word,"")
            query = query.strip()
            New_Line = []
            with open("Python Code\\JARVIS\\learn.txt",'r') as file:
                lines = file.readlines()
                for line in lines:
                    if query in line:
                        if "what is" in query or "who is" in query:
                            line = line.replace(query,"")
                        else:
                            Remove = ["what is","who is",query]
                            for word in Remove:
                                line = line.replace(word,"")
                        Line = line.strip().capitalize()
                        New_Line.append(Line)
            if len(New_Line)==1:
                print(Line),speck(Line)
                
if __name__ == '__main__':
    play_gif
    speck("....Checking internet connection........ its done.. Checking temperature....... Now everything is OK.... System is online sir, please say, wake up")
    print("Pleass say... Wake UP!")
    while True:
        permission = TakeCommand().lower()
        if "wake up" in permission or "utho" in permission:
            takeCommand()
        elif "system" in permission:
            hour = datetime.datetime.now().hour
            if hour>=16:
                speck("OK sir good night")
            else:
                speck("Ok sir have nice day")
            break
        elif "sleep" in permission or "so jao" in permission:
            speck("Sir please say... Wake UP!")