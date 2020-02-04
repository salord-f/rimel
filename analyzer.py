import re
import pygit2
from github import Github
import re
import base64

# First create a Github instance:
import os, sys

numberOfRepo = 0
inDocker = 0
inDockerCompose = 0
inBoth = 0
query = b'version'
repositoryClone = './repository/'

def containsWanted(file):
    print("------------------------------")
    with open(file, 'r') as fileString:
        data = (fileString.read().replace('\n', '')).encode()
        if re.search(query, data) is not None:
            print("oui")
            return True


def analyzeFile(file):
    global inDocker
    global inDockerCompose
    global inBoth

    inDockerBool = False
    inDockerComposeBool = False
    if re.search('Dockerfile*', file):
        if containsWanted(file):
            inDocker += 1
            inDockerBool = True
    if re.search('docker-compose*', file):
        if containsWanted(file):
            inDockerCompose += 1
            inDockerComposeBool = True
    if inDockerBool and inDockerComposeBool:
        inBoth += 1
        inDocker -= 1
        inDockerCompose -= 1
    if inDockerBool or inDockerComposeBool:
        return True


for folder in os.listdir(repositoryClone):
    numberOfRepo += 1
    print("*****************************")
    newPath = repositoryClone + folder
    isFile = os.path.isfile(newPath)
    isDirectory = os.path.isdir(newPath)
    if isFile:
        print("file : " + newPath)
        if analyzeFile(newPath):
            break
    elif isDirectory:
        print("directory : " + newPath)
        for folderRecu in os.listdir(newPath):
            newPathRecu = newPath + "/" + folderRecu
            print("fileRecu : " + "/" + newPathRecu)
            if analyzeFile(newPathRecu):
                break
print("numberOfRepo :" + str(numberOfRepo))
print("inDockerCompose :" + str(inDockerCompose))
print("inDocker :" + str(inDocker))
print("inBoth :" + str(inBoth))
