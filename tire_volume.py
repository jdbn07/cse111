import math
from datetime import datetime

print("To find the volume of a tire please have the tire's type number available.")
print("A tire number is a number appears as such 205/60R15")
pi= math.pi
w = int(input("Enter the width of the tire in mm (ex 205): "))
a=int(input("Enter the aspect ratio of the tire (ex 60): "))
d=int(input("Enter the diameter of the wheel in inches (ex 15): "))

v=(pi*(w**2)*a*(w*a+2540*d))/10000000000
# v=(pi * (pow(w,2)*a*(w*a+2540*d)))/10000000000
print(f"The approximate volume is  {v:.2f}  liters")
question = str(input("Do you need to buy tires with those characteristics?: ")) #After your program prints the tire volume to the terminal window, your program should ask the user if she wants to buy tires with the dimensions that she entered. If the user answers “yes”, your program should ask for her phone number and store her phone number in the volumes.txt file.
if question == "yes":
    ans = str(input("What is your phone number to contact you?:  "))

current_date_and_time=datetime.now(tz=None)
#print(current_date_and_time) #test to see if above worked
with open("volume.txt", mode='a') as record_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {ans}", file=record_file)