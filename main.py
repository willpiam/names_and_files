"""
Programmer: William



"""

import pybrary#gets some other code ive written


def newFile():
    #makes a whole new file
    names = []
    temp = ""
    for i in range (0,5):
        temp = str(input("Please enter name "+str(i+1)+":"))
        names.append(temp)
        print (" ")
    temp = str(input("Please enter a file name (filename does not need to alread excist:"))
    pybrary.writeArray(temp,names)
                   
def readNames():
    #reads a file of names
    array = []
    try:
        file = str(input("enter a file name: "))
        array = pybrary.readFile(file)
        print (array)
    except IOError:
        print ("somethig went wrong. Prehaps you entered a file name which does not excist")
        print ("")
        print ("Please try again...")
        print ("")
        array = readNames()
    return array


def editName():
    #edits a user specified line in a specified file
    try:    #try and get a REAL file to edit
        print ("You have chosen to edit a name in a file. You will have to first specify the file in which the line you wish to edit resides")
        file = str(input("please enter the file name on this line ---->"))
        array = pybrary.readFile(file)  #we will get the whole file as an array... edit THAT array... and then over write the old file with the eddited array
    except:
        print ("something went wrong. I spoke to the guys in the back and they said you'll have to redo this function all over. Sorry about this but it WAS probiby your fault.")
        editName()
        return #should end the whole function !!!!!!-------  I NEEEEEEEEEEEEEEED THIS TO END THE WHOLE FUNCTION ----------!!!!!!!!

    #time to edit that array
    print ("Which line would you like to edit?")
    print (" ")
    print ("1___________"+array[0])
    print ("2___________"+array[1])
    print ("3___________"+array[2])
    print ("4___________"+array[3])#menu .... what line does user want to edit......shows user what is on each line
    print ("5___________"+array[4])
    print (" ")
    
    done = False
    while (done == False):
        print ("I HAVE HAD A LONG DAY. IF YOU ENTER A NUMBER LESS THAN ONE OR GREATER THAT 5 YOU WILL BREAK THIS PROGRAM.")#AN INOVATIVE APPROCH TO GETTING SAFE INPUT
        print ("TO BE VERY CLEAR... DO NOT ENTER A NUMBER OTHER THAN 1, 2, 3, 4, OR 5")
        print ("IF YOU DO THIS PROGRAM WILL CRASH BUT BEFORE IT DOES THAT IT WILL SEND ME AN EMAIL SAYING WHO YOU ARE. THEN I WILL HUNT YOU DOWN AND GET VERY UPSET")
        skip = False
        snum = str(input("Enter choice here ------>"))
        try:
            num = int(snum)
        except:
            done = False
            skip = True
            print ("We will have to get you to retry entering a choice...")
            print (" ")
            
        if (skip != True):#we have good input
            var = array[num -1]
            print ("Your line currently says: "+ var)
            print ("What would you rather it say?")
            var = input("ENTER YOUR REVISIONS ON THIS LINE --->")

            array[num -1] = var

            #now write that array to the file (overwrite not append)
            #luckly i have already writen the code to do just that
            pybrary.writeArray(file,array)
            done = True#we have reached the end of the function

            
            
        

    
    
        
    
"""
def disSingle():
    #displays a single name (user specified)
def delt():
    #deletes a name and moves the next line up to where it was so we're not left with an empty line

"""
import time
def wantToCon():
    #asks if user wants to contine with the program..
    #returns false if the user does not returns true if the user wants to continue
    done = False
    while (done == False):
        print ("Would you like to continue with the program?")
        print ("")
        print ("Your options are:")
        print ("")
        print ("code--------answer--------description".upper())
        print ("(1)---------Yes-----------will loop file (your work will still be saved)")
        print ("(2)---------No------------Will end program (your work will still be saved)")
        print ("")

        con = str(input("respond here------>"))

        if (con == "1"):
            print ("We will continue")
            return True
        elif(con == "2"):
            print ("GOODBYE!")
            time.sleep(3)   #dramatic effect
            return False
        else:
            done = False    #continue



con = True

while (con == True):
    print ("(1)create a new five name file".center(40,"-"))
    print ("(2)Display all names".center(40,"-"))
    print ("(3)Edit a specific name".center(40,"-"))
    print ("(4)Display a specific name".center(40,"-"))
    print ("(5)Delete a specific name".center(40,"-"))#block presents options to user
    print ("".center(40,"-"))

    
    do = str(input("What do you want to do?"))
    skip = False
    if (do == "1"):
        newFile()
    elif (do == "2"):
        readNames()
    elif (do == "3"):
        editName()
    elif (do == "4"):
        disSingle()
    elif (do == "5"):
        delt()
    else:
        print ("")
        print ("You entered bad input... Please try again".title())
        print ("")
        skip = True
    if (skip != True):
        con = wantToCon()
    
