import pyttsx3
import os
import time
print("███████╗██████╗░░█████╗░████████╗███████╗██████╗░░█████╗░███╗░░██╗░█████╗░██╗░░░░░███████╗░█████╗░░██████╗░██╗░░░░░███████╗░██████╗")
print("██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗████╗░██║██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔════╝░██║░░░░░██╔════╝██╔════╝")
print("█████╗░░██████╔╝███████║░░░██║░░░█████╗░░██████╔╝███████║██╔██╗██║███████║██║░░░░░█████╗░░███████║██║░░██╗░██║░░░░░█████╗░░╚█████╗░")
print("██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██╔══╝░░██╔══██╗██╔══██║██║╚████║██╔══██║██║░░░░░██╔══╝░░██╔══██║██║░░╚██╗██║░░░░░██╔══╝░░░╚═══██╗")
print("██║░░░░░██║░░██║██║░░██║░░░██║░░░███████╗██║░░██║██║░░██║██║░╚███║██║░░██║███████╗███████╗██║░░██║╚██████╔╝███████╗███████╗██████╔╝")
print("╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚══════╝╚═════╝░")
engine = pyttsx3.init()
time.sleep(2.4)
engine.say("what is your name ")
engine.runAndWait()
name = input("enter your name ")
engine.say("enter your age")
engine.runAndWait()
age = input("whats your age ")
engine.say("what is your gender")
engine.say("male or female")
engine.say("enter your choice")
engine.runAndWait()
print("\n 1 female")
print("2 male")
gender1 = input("enter your suggetion")

if int(gender1)<=1:
    gender="miss. "
    print(gender)
elif int(gender1)>1:
    gender="mr. "
    print(gender)
    # engine.say()

print("hello "+gender+". "+name+" welccome to this challenge ")
engine.say("hello. "+gender+". "+name+" welcome to this challenge ")
time.sleep(2.0)
print("currept will fear us. the honest will suppourt us. the heroic will join us")
engine.say("currept will fear us. the honest will suppourt us. the heroic will join us")
time.sleep(2.4)
print("check the readme file to get information about this challange")
engine.say("check readme file to get information about this challenge ")
engine.runAndWait()
time.sleep(2.0)
os.system('cls')
# os.system('clear)
# print("thank you ")
engine.say("thank you")
engine.runAndWait()
