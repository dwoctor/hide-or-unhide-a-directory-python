from platform import system
operatingSystem = system()
if operatingSystem == "Windows" or operatingSystem == "Darwin":
    folderPath = raw_input("Enter the path of the folder you want to hide or unhide: ")
    command = raw_input("Do you want to hide or unhide '{0}': ".format(folderPath)).upper()
    from subprocess import call
    if command == "HIDE":
        if operatingSystem == "Windows":
            call(["attrib", "+H", folderPath])
        elif operatingSystem == "Darwin":
            call(["chflags", "hidden", folderPath])
    elif command == "UNHIDE":
        if operatingSystem == "Windows":
            call(["attrib", "-H", folderPath])
        elif operatingSystem == "Darwin":
            call(["chflags", "nohidden", folderPath])
    else:
        print "ERROR: (Incorrect Command) Valid commands are 'HIDE' and 'UNHIDE' (both are not case sensitive)"
else:
    print "ERROR: (Unknown Operating System) Only Windows and Darwin(Mac) are Supported"