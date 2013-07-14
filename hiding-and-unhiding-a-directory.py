def getOperatingSystem():
	from platform import system
	operatingSystem = system()
	return operatingSystem

def getFolderPath():
	folderPathInputMessage = "Enter the path of the folder you want to hide or unhide: "
	folderPath = raw_input(folderPathInputMessage)
	return folderPath

def getCommand(folderPath):
	commandInputMessage = "Do you want to hide or unhide '" + folderPath + "': "
	command = raw_input(commandInputMessage)
	return command

def executeCommand(folderPath, command, operatingSystem):
	#import os
	#os.system("command")
	from subprocess import call
	if command.upper() == "HIDE":
		if operatingSystem == "Windows":
			call("attrib +H " + folderPath)
		elif operatingSystem == "Darwin":
			call(["chflags", "hidden", folderPath])
	elif command.upper() == "UNHIDE":
		if operatingSystem == "Windows":
			call("attrib -H " + folderPath)
		elif operatingSystem == "Darwin":
			call(["chflags", "nohidden", folderPath])
	else:
		raw_input("ERROR: (Incorrect Command) Valid commands are 'HIDE' and 'UNHIDE' (both are not case sensitive)")

operatingSystem = getOperatingSystem()
if operatingSystem == "Windows" or operatingSystem == "Darwin":
	folderPath = getFolderPath()
	command = getCommand(folderPath)
	executeCommand(folderPath, command, operatingSystem)
else:
	raw_input("ERROR: (Unknown Operating System) Only Windows and Darwin(Mac) are Supported")