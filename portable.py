def isPython(versionNumber): # Check the version of python running
    import platform
    return platform.python_version().startswith(str(versionNumber))

def consoleReadLine(message): # Read a string from the console
    if isPython(3): # Python 3.x code
        return input(message)
    else: # Python 2.x code
        return raw_input(message)

def consoleWriteLine(message): # Write a string to the console
    import os, sys
    sys.stdout.write(str(message) + os.linesep)

from platform import system
operatingSystem = system()
if operatingSystem == "Windows" or operatingSystem == "Darwin":
    folderPath = consoleReadLine("Enter the path of the folder you want to hide or unhide: ")
    command = consoleReadLine("Do you want to hide or unhide '{0}': ".format(folderPath)).upper()
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
        consoleWriteLine("ERROR: (Incorrect Command) Valid commands are 'HIDE' and 'UNHIDE' (both are not case sensitive)")
else:
    consoleWriteLine("ERROR: (Unknown Operating System) Only Windows and Darwin(Mac) are Supported")