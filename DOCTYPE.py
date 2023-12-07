from os import system
from pytube import YouTube
import pyttsx3
import requests
from colorama import Fore
from art import text2art
import random
from playsound import playsound
Gr = '\033[1;32m'
Wh = '\033[1;37m'

def main():
    print('=================================================')
    print('               created by DOCTYPE_GROUP          ')
    print('=================================================')
    print('               ++++++++++++++++++++              ')
    print('                                                 ')
    print(f' {Wh}============= {Gr}DOCTYPE_GROUP{Wh}=============')
    print("""\033[1;32m
   ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄  ▄█  ███▄▄▄▄      ▄██████▄       
  ███    ███     ███    ███ ███    ███   ███ ▄███▀ ███  ███▀▀▀██▄   ███    ███      
  ███    ███     ███    ███ ███    █▀    ███▐██▀   ███▌ ███   ███   ███    █▀       
 ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀    ███▌ ███   ███  ▄███          
▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ███▌ ███   ███ ▀▀███ ████▄           
  ███    ███     ███    ███ ███    █▄    ███▐██▄   ███  ███   ███   ███    ███   
  ███    ███     ███    ███ ███    ███   ███ ▀███▄ ███  ███   ███   ███    ███    
  ███    █▀      ███    █▀  ████████▀    ███   ▀█▀ █▀    ▀█   █▀    ████████▀    
                                         ▀                                                                                                        
                                    \033[34m          DOCTYPE GROUP          [✔]
                                    \033[34m            Version 1.1.0         [✔]
\033[1;32m """)
 


main()
print('[1] Download Video YouTube')
print('[2] IP Info')
print('[3] text to ASCII')
print('[0] Exit')

option = input('==> ')

if option == '1':

    link = input('Enter the YouTube video link: ')
    yt = YouTube(link)
    
    # Get the stream with progressive="True" and file_extension="mp4"
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    
    # Sort the stream (highest resolution first) and download the first in the list
    stream.order_by('resolution').desc().first().download()


elif option == '2':
    print(f' {Wh}============= {Gr}INFORMATION IP ADDRESS {Wh}=============')

    def get_ip_info(ip_address):
        url = f"https://ipinfo.io/{ip_address}/json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def check_ip_status(ip_address):
        url = f"https://ipinfo.io/{ip_address}/json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if "bogon" in data:
                return "The IP address is a bogon IP."
            elif "error" in data:
                return "Unable to retrieve information for the IP address."
            else:
                return "The IP address is valid."
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    ip_address = input("Enter an IP address: ")
    ip_info = get_ip_info(ip_address)
    print("IP information:")
    print(ip_info)

    ip_status = check_ip_status(ip_address)
    print("IP status:")
    print(ip_status)



elif option == '3':
 def ascii_art():
    while True:
        input_text = input("Enter text (press 'q' to quit): ")
        
        if input_text.lower() == 'q':
            break
        
        available_fonts = ['block', 'starwars', 'acrobatic', '3d', 'doh', 'isometric1', 'letters', 'bulbhead', 'alligator']
        random_font = random.choice(available_fonts)
        art = text2art(text=input_text, font=random_font, chr_ignore=True)
        print(art)

if __name__ == "__main__":
    ascii_art()

elif option == '0':
    def text_to_speech(text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 145)
        engine.setProperty('volume', 1)
        engine.setProperty('voice', 'persian')
        engine.say(text)
        engine.runAndWait()

    say_text = "GOODBY MOTHERFUCKER "
    text_to_speech(say_text)
    exit()

else:
    system('clear')
