import rotatescreen
import time

screen = rotatescreen.get_primary_display()

print("\t\t\t\t!!!!!CAUTION!!!!!\n\t\t\t***This thing can MESS UP your computer***")

x = int(input("\n1.START\n2.QUIT\nYour option: "))

if x != 1 or 2:
    print("Invalid Input, Just enter the numbers i.e 1 or 2")

elif x == 1:
    for k in range(10,0,-1):
        time.sleep(1)
        print(k)
    print("/////GET READY FOR THE HEART ATTACK/////\n-----And don't even dare to stop this while its running-----")
    time.sleep(3)
    for i in range(201):
        time.sleep(1)
        screen.rotate_to(i * 90 % 360)

elif x == 2:
    print("\n!!!! Sorry, but there is no way back !!!!")
    for k in range(10,0,-1):
        time.sleep(1)
        print(k)
    print("\n/////GET READY FOR THE HEART ATTACK/////\n-----And don't even dare to stop this while its running-----")
    time.sleep(3)
    for i in range(201):
        time.sleep(1)
        screen.rotate_to(i * 90 % 360)



