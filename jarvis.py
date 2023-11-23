


import datetime

import wikipedia
import openai


import pyaudio
import webbrowser
import speech_recognition as sr
import os
import glob
import time
import win32com.client

apikey="paste your api key"


speaker=win32com.client.Dispatch("SAPI.SpVoice")



def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response=openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)
        say(text)

    # promp = "What is the capital of France?"
    #
    # response = Bard.get_answer(promp)
    #
    # print(response["text"])

def say(text):
    speaker.Speak(text)

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=0.6 #used to specify the wait time before processing ip
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred"



if __name__=='__main__':
    say("Hello I am Jarvis, how can i assist you")
    while(True):
        print("Listening...")
        query=takeCommand()
        sites=[["youtube","https://www.youtube.com"],
               ["wikipedia","https://www.wikipedia.com"],
               ["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])
        if "play music".lower() in query.lower():
            musicPath= r"C:\Users\abbya\Music\music"
            musicFiles = glob.glob(os.path.join(musicPath, "*.mp3"))# Get a list of all MP3 files in the folder
            for musicFile in musicFiles:

                os.startfile(musicFile)
                time.sleep(180)
        if "time" in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            hour=datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            if int(hour) >12:
                hour=int(hour)-12
                say(f"the time is {hour} {min} pm")
            else:
                say(f"the time is {hour} {min} am")
            print(strfTime)

        if "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)



        if "stop".lower() in query.lower() or "shutdown".lower() in query.lower():
            say("Powering down")
            print("Goodbye...")
            time.sleep(2)
            exit(0)
        #say(query)
