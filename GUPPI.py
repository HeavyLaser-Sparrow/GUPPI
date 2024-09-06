from ToDoList import *
from IPv4 import *
from IPv6 import *

while True:
    print("This is what you can do: ")
    print("\t0. Exit GUPPI")
    print("\t1. To-Do List")
    print("\t2. Binary and IP Converter")
    
    whatDo = int(input("What do you want to do?: "))
    
    if whatDo == 0:
        print("Exiting GUPPI")
        break
    elif whatDo == 1:
        main()
    elif whatDo == 2:
        ipChoice = int(input("Do you want to convert IPv[4] or IPv[6]? "))
        if ipChoice == 4:
            mainIPv4()
        elif ipChoice == 6:
            mainIPv6()
        else:
            print("Invalid IP choice.")
    else:
        print("I do not know what that means")
