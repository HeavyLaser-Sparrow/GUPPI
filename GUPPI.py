from ToDoList import *
from IPv4 import *
from IPv6 import *

while True:
    print("This is what you can do: ")
    print("\t0.Exit GUPPI")
    print("\t1.To-Do List")
    print("\t2.Binary and IPv4 Converter")
    print("\t3.Binary and IPv6 Converter")
    whatDo = int(input("What do you want to do?: "))
    if (whatDo == 0):
        print("Exiting GUPPI")
        break
    if(whatDo == 1):
	    main()
    elif(whatDo == 2):
	    mainIPv4()
    elif(whatDo == 3):
        mainIPv6()
    else:
	    print("I do not know what that means")
