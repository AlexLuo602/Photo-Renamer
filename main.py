import os
import time
import shutil

global c
c = 0


def Format_Changer(date):
    formatted_date_a = time.ctime(os.path.getctime(date)).split(" ")
    formatted_date_b = []

    if "" in formatted_date_a:
        formatted_date_a.remove("")

    if len(formatted_date_a[2]) == 1:
        formatted_date_a[2] = "0" + formatted_date_a[2]

    month = formatted_date_a[1]
    __time__ = formatted_date_a[3]
    __time__ = __time__.split(":")
    formatted_date_a[3] = "꞉".join(__time__)

    if month == "Jan": formatted_date_a[1] = "1"
    elif month == "Feb": formatted_date_a[1] = "2"
    elif month == "Mar": formatted_date_a[1] = "3"
    elif month == "Apr": formatted_date_a[1] = "4"
    elif month == "May": formatted_date_a[1] = "5"
    elif month == "Jun": formatted_date_a[1] = "6"
    elif month == "Jul": formatted_date_a[1] = "7"
    elif month == "Aug": formatted_date_a[1] = "8"
    elif month == "Sep": formatted_date_a[1] = "9"
    elif month == "Oct": formatted_date_a[1] = "10"
    elif month == "Nov": formatted_date_a[1] = "11"
    elif month == "Dec": formatted_date_a[1] = "12"

    formatted_date_b.append(formatted_date_a[4])
    formatted_date_b.append(formatted_date_a[1])
    formatted_date_b.append(formatted_date_a[2])
    formatted_date_final = "-".join(formatted_date_b)
    formatted_date_final += " " + formatted_date_a[3]
    return formatted_date_final


#Iterates through all the files in the folder
def File_renaming(source):

    duplicate = []
    list_of_files = os.listdir(source)
    for i, file in enumerate(list_of_files):
        try:
            # list_of_files = os.listdir(source)
            #Shows Progress
            print("Renaming file #" + str(i + 1) + "...")

            #extracts what type the file is
            # type_a = file.split(".")
            # type_b = []
            # type_b.append(type_a[len(type_a)-1])
            # type_b = "".join(type_b)
            # if type_b == "ini": continue

            #Declares old file name and new file name
            new_name = Format_Changer(source + "\\" + file)
            old_file_name = source + "\\" + file

            #Checks for duplicates
            # if new_name + "." + type_b in list_of_files:
            #     duplicate.append(new_name)
            #     new_name += "_(%d)_" %(duplicate.count(new_name) + 1)

            # new_name = new_name + "." + type_b
            new_name = new_name + ".JPG"
            new_file_name = source + "\\" + new_name
            os.rename(old_file_name, new_file_name)
            shutil.move(src= new_file_name, dst="D:\Jess' Temp2\Pictures")
            os.system("cls")
        except:
            count = 0
            while new_name in os.listdir(source):
                c = count
                count += 1
                if count == 1:
                    new_name = new_name.replace(".JPG", "(%d).JPG" % (count))
                else:
                    new_name = new_name.replace("(%d).JPG"%(c),"(%d).JPG"%(count))
                print(new_name)

            while new_name in os.listdir("D:\Jess' Temp2\Pictures"):
                c = count
                count += 1
                new_name = new_name.replace("(%d).JPG" % (c), "(%d).JPG" % (count))
                print(new_name)

            new_file_name = source + "\\" + new_name
            os.rename(old_file_name, new_file_name)
            shutil.move(src=new_file_name, dst="D:\Jess' Temp2\Pictures")
            continue
            
            

while True:
    #Inputs from the user
    source = input("Which folder do you want to modify: ")
    File_renaming(source)
    print("All done! Thanks for waiting!")
    time.sleep(1)
    print("Would you like to continue?")
    print("")
    print("Press y or yes to continue")
    users_input = input("Press any other key to exit: ")
    print(users_input)
    if users_input != "y" and users_input != "yes":
        break

# https://www.youtube.com/watch?v=hSTw7CAWRpo video for shutil syntax