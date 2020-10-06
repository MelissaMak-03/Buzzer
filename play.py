# Melissa Makonga
#This is a fun game that you should try
import datetime

import speech_recognition as sr
from gtts import gTTS
import os
import playsound

#define the language
from soupsieve.util import upper

count = 0
# read the text
def speak(text, lang):
    global count
    ##for i in range(1000):
    if (upper(lang) == "ENGLISH"):
        output = gTTS(text = text,lang = "en",slow = False)
    if (upper(lang) == "FRENCH"):
        output = gTTS(text = text,lang = "fr",slow = False)
    filename = ("number.mp3")
    output.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def multiple(m,n):
    if (m % n == 0):
        return True
    else:
        return False

def ending(m, n):
    if(m % 10 == n):
        return True
    else:
        return False

print('Welcome to the buzzer game')
langue = input('Please choose a language English or French?')

## English part
if (upper(langue)== "ENGLISH"):
    value = input ('Please choose a number between 1-10:')
    value = int(value)
    print('The rules are simple, we are both going to start counting from 1 and keep going.\n'
      ' whenever the number you want to say is either a multiple of',value, 'or ends with',value,', you need to say BUZZ.\n'
      ' If one of the players do not say BUZZ when he needs to say it, it GAME OVER, that player has lost.\n'
        'If one of the players say BUZZ when the number is not a multiple or do not end with',value,'it GAME OVER, that player has lost.\n'
        ' If you want to quit the game just say stop')

    count = "1"

    word = "BUZZ"
    speak(count, langue)
    computercount = int(count)

    for i in range(1000):
    #text = audio()
        r = sr.Recognizer()
        test = False

        while (test == False):
            with sr.Microphone() as source:
            # get input from user

                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio, language= 'en')
                    test = True
                # print('you said: {}'.format(text))
                except:
                    response = "Sorry, I couldn't hear what you said"
                    speak(response, langue)
                    test = False

## check if the player want to exit the game
        if "stop" in text:
            exit()
## check the player count
        playercount = computercount +1
        if (multiple(playercount,value)== True or ending(playercount,value)== True):
            if (upper(text) != word):
                lost = "You lost! You should have said buzz"
                speak(lost, langue)
                exit()
        if ending(playercount,value)== False:
            if multiple(playercount,value)== False:
                if (text == word):
                    lost = "You lost!, you should have said buzz"
                    speak(lost, langue)
                    exit()
## check the computer count
        suivant = computercount +2
        if (multiple(suivant,value)== True or ending(suivant,value)== True):
            speak(word, langue)
        else:
            numbenext = str(suivant)
            speak(numbenext,langue)
        computercount += 2


## French part

if (upper(langue) == "FRENCH"):
    valeur = input('Choisissez un nombre entre 1-10:')
    valeur = int(valeur)
    print('Les regles sont simples, nous allons tous les deux commencer a compter a partir de 1.\n'
          ' Chaque fois que le nombre que tu t\'appretes a dire est un multiple de', valeur, 'ou finit par', valeur,
          ',Tu dois dire  BUZZ.\n'
          'Si l\'un des joueurs ne dit pas BUZZ quand il doit le dire, c\'est GAME OVER,il a perdu.\n'
          'Si l\'un des joueurs dit BUZZ pour un nombre qui n\'est pas multiple ou ne finit pas par', valeur,
          'c\'est GAME OVER, il a perdu.\n'
          'Si vous voulez quitter le jeu dites STOP')

    cont = "1"

    word1 = "BUZZ"
    speak(cont, langue)
    computercont = int(cont)

    for i in range(1000):
        # text = audio()
        r = sr.Recognizer()
        test = False

        while (test == False):
            with sr.Microphone() as source:
                # get input from user

                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio, language='fr')
                    test = True
                # print('you said: {}'.format(text))
                except:
                    response = "Desole, je n'ai pas compris ce que vous avez dit"
                    speak(response, langue)
                    test = False

        ## check if the player want to exit the game
        if "stop" in text:
            exit()
        ## check the player count
        playercont = computercont + 1
        if (multiple(playercont, valeur) == True or ending(playercont, valeur) == True):
            if (upper(text) != word1):
                lost = "Tu as perdu! Tu aurais du dire BUZZ"
                speak(lost, langue)
                exit()
        if ending(playercont, valeur) == False:
            if multiple(playercont, valeur) == False:
                if (text == word1):
                    lost = "Tu as perdu! Tu aurais du dire BUZZ"
                    speak(lost, langue)
                    exit()
        ## check the computer count
        suivant = computercont + 2
        if (multiple(suivant, valeur) == True or ending(suivant, valeur) == True):
            speak(word1, langue)
        else:
            numbenext = str(suivant)
            speak(numbenext, langue)
        computercont += 2






