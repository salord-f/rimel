import re
import os

numberOfRepo = 0
inDocker = 0
inDockerCompose = 0
inBoth = 0
query = b'version'
repositoryClone = './repository/'


def contains_wanted(file):
    print("------------------------------")
    with open(file, 'r') as fileString:
        data = (fileString.read().replace('\n', '')).encode()
        if re.search(query, data) is not None:
            return True


def analyze_file(file):
    global inDocker
    global inDockerCompose
    global inBoth

    in_docker_bool = False
    in_docker_compose_bool = False
    if re.search('Dockerfile*', file):
        if contains_wanted(file):
            inDocker += 1
            in_docker_bool = True
    if re.search('docker-compose*', file):
        if contains_wanted(file):
            inDockerCompose += 1
            in_docker_compose_bool = True
    if in_docker_bool and in_docker_compose_bool:
        inBoth += 1
        inDocker -= 1
        inDockerCompose -= 1
    if in_docker_bool or in_docker_compose_bool:
        return True


for folder in os.listdir(repositoryClone):
    numberOfRepo += 1
    print("*****************************")
    newPath = repositoryClone + folder
    isFile = os.path.isfile(newPath)
    isDirectory = os.path.isdir(newPath)
    if isFile:
        print("file : " + newPath)
        if analyze_file(newPath):
            break
    elif isDirectory:
        print("directory : " + newPath)
        for folderRecu in os.listdir(newPath):
            newPathRecu = newPath + "/" + folderRecu
            print("fileRecu : " + "/" + newPathRecu)
            if analyze_file(newPathRecu):
                break
print("##############################################RESULT###########################################################")
print("String wanted : " + str(query))
print("Number of repo analyzed : " + str(numberOfRepo))
print("in DockerCompose : " + str(inDockerCompose))
print("in Docker : " + str(inDocker))
print("in Both : " + str(inBoth))
