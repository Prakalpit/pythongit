print ( "Hi I am python version A.12.4.cE \n I can help you open different applications installed in this computer."
        " \n here are the examples of the applications i can open \n "
        "1) calculator\n 2) wordpad \n 3) notepad \n 4)excel \n 5) Word \n 6)powerpoint ")
user_choice = input ("Which app would you like me to open?  : ")
if user_choice == "calculator" or user_choice == "wordpad" or user_choice =="notepad" or user_choice=="powerpoint" or user_choice== "excel" or user_choice=="word":
    if user_choice == "calculator" :
        import subprocess

        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        print ("Valid user choice!")
    elif user_choice== "wordpad" :
        import subprocess

        subprocess.Popen('C:\\Windows\\System32\\write.exe')
        print("Valid user choice!")
    elif user_choice=="notepad" :
        import subprocess

        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        print(" Valid user choice!")
    elif user_choice=="excel":
        import subprocess

        subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\Office16\excel.exe')
        print ("valid user choice!")
    elif user_choice=="word":
        import subprocess
        subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\Office16\winword.exe')
        print("valid user choice!")
    elif user_choice=="powerpoint":
        import subprocess
        subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\Office16\powerpnt.exe')
        print("valid user choice!")
    print ("opening " + user_choice)
else :
    print("invalid input ! please check the provided options! ")