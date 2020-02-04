import re
import os

numberOfRepo = 0
inDocker = {}
inDockerCompose = {}
inBoth = {}
# query = b'version'
queries = ['version', 'ports', 'environment', 'tests']
repositoryClone = './repository/'


def contains_wanted(file, word):
    print("------------------------------")
    with open(file, 'r') as fileString:
        data = (fileString.read().replace('\n', '')).encode()
        if re.search(word.encode(), data) is not None:
            return True


def analyze_file_docker(file):
    global inDocker

    for query_docker in queries:
        if contains_wanted(file, query_docker):
            inDocker[query_docker] = inDocker[query_docker] + 1


def analyze_file_docker_compose(file):
    global inDockerCompose

    for query_compose in queries:
        if contains_wanted(file, query_compose):
            inDockerCompose[query_compose] = inDockerCompose[query_compose] + 1


def isDocker(file):
    if re.search('Dockerfile*', file):
        return True
    else:
        return False


def isDockerFile(file):
    if re.search('docker-compose*', file):
        return True
    else:
        return False


for query in queries:
    inDockerCompose[query] = 0
    inDocker[query] = 0
    inBoth[query] = 0

for folder in os.listdir(repositoryClone):
    docker = ""
    dockerFile = ""
    numberOfRepo += 1
    print("*****************************")
    newPath = repositoryClone + folder
    if os.path.isdir(newPath):
        print("directory : " + newPath)
        for folderRecu in os.listdir(newPath):
            newPathRecu = newPath + "/" + folderRecu
            if os.path.isdir(newPathRecu):
                print(newPathRecu)
                for subFolder in os.listdir(newPathRecu):
                    newPathRecu = newPathRecu + "/" + subFolder
                    if os.path.isfile(newPathRecu):
                        if isDocker(newPathRecu) and docker == "":
                            docker = newPathRecu
                        elif isDockerFile(newPathRecu) and dockerFile == "":
                            dockerFile = newPathRecu
                        print(newPathRecu)
            elif os.path.isfile(newPathRecu):
                if isDocker(newPathRecu) and docker == "":
                    docker = newPathRecu
                elif isDockerFile(newPathRecu) and dockerFile == "":
                    dockerFile = newPathRecu
                print(newPathRecu)

        if docker != "":
            analyze_file_docker(docker)
        if dockerFile != "":
            analyze_file_docker_compose(dockerFile)
            # if isDocker(newPathRecu) and docker == "":
            #    docker = ...
            # elif isDockerFIle(newPathRecu) and dockerFile == "":
            #    dockerFile = ...
            # if analyze_file(newPathRecu):
            # break

'''for query in queries:
    print("############################################RESULT#########################################################")

    print("String wanted : " + str(query))
    print("Number of repo analyzed : " + str(numberOfRepo))
    print("in DockerCompose : " + str(inDockerCompose[query]))
    print("in Docker : " + str(inDocker[query]))
    print("in Both : " + str(inBoth[query]))
'''
print("Number of repo analyzed : " + str(numberOfRepo))
print("in docker file : " + str(inDocker))
print("in docker compose : " + str(inDockerCompose))
