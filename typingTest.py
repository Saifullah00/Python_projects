from threading import main_thread
from time import *
import random as r

from pip import main

#Function to count Error
def mistakes(partest, usertext):
    error = 0
    for i in range(len(partest)):
        try :
            if partest[i] != usertext[i]:
                error+=1
        except :
            error+=1
    return error

# Function to count Speed time
def speedTime(time_s, time_e, user_t):
    time_delay = time_e - time_s
    time_round = round(time_delay, 2)
    speed = len(user_t)/time_round
    return round(speed)  

# main program
if __name__ == '__main__':    
    while True:
        choice = input("Ready to start your typing test (Y/N) : \t").upper()
        if(choice == 'Y'):
            text = ["Python is fun, expressive, its readable style, quick editing.",
                    "Python is a widely used general-purpose, high level programming language" ,"Python was created by Guido van Rossum in 1991 ", "Test your typing speed online, find out how fast can you type with Ratatype WPM typing test"]
            test_1 =  r.choice(text)
            print("\n\tCHECK YOUR TYPING SPEED (WPS)\n\tType the given TEXT 👇\n")
            print(test_1, "\n\n")
            time_1 = time()
            user_text = input("Type : ")
            time_2 = time()

            print('Speed : ', speedTime(time_1, time_2, user_text)," w/sec\n")
            print('Error : ', mistakes(test_1, user_text))
        
        elif(choice == 'N'):
            print("Thank you for using !!")
            break
        else :
            print("Wrong choice!!!!")