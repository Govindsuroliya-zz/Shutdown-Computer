import  os
import time
user_input  =  input("Should You shutdown your computer (y/n)")
if user_input == "y":
    print("Shutting down computer in 5 seconds")
    time.sleep(5)
    os.system("shutdown /s /t 1")
elif user_input == "n":
    print("Close program in 5 seconds")
    time.sleep(5)
    exit()
else :
    print(" Your input is incorrect. please enter \"y/n/\" only.")        