from ToDoList import *
from Binary_IP import *

while True:
    print("This is what you can do: ")
    print("\t0.Exit GUPPI")
    print("\t1.To-Do List")
    print("\t2.Binary and IP Converter")
    whatDo = int(input("What do you want to do?: "))
    if (whatDo == 0):
        print("Exiting GUPPI")
        break
    if(whatDo == 1):
	    main()
    elif(whatDo == 2):
	    mainIP()
    else:
	    print("I do not know what that means")
