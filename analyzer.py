import re
import os
import xlsxwriter
import csv


#TODO repo de ref docker + standard docker
#TODO quantifie, def coefficient de conformité, pas dire oui ou non

numberOfRepo = 0
inDocker = {}
inDockerCompose = {}
inSpring = {}
inBoth = {}
interesting_projects = []

queries = ['version', 'ports', 'environment', 'tests', 'server']
repositoryClone = './repository/'
queriesTest = {
    "inDocker": ['version', 'ports', 'environment', 'tests', 'server'],
    "inDockerCompose": ['version', 'ports', 'environment', 'tests', 'server'],
    "inSpring": ['version', 'ports', 'environment', 'tests', 'server']
}
queriesExtra = {
    "connectionBD":
    {
        "inDocker": ['version', 'ports', 'environment', 'tests', 'server'],
        "inDockerCompose": ['version', 'ports', 'environment', 'tests', 'server'],
        "inSpring": ['version', 'ports', 'environment', 'tests', 'server']
    },
    "version":
    {
        "inDocker": ['version'],
        "inDockerCompose": ['version'],
        "inSpring": ['version']
    },
    "extra":
    {
        "inDocker": ['ADD', 'FROM', 'EXPOSE', 'tests', 'server'],
        "inDockerCompose": ['ADD', 'FROM', 'environment', 'tests', 'server'],
        "inSpring": ['ADD', 'FROM', 'environment', 'tests', 'server']
    }
}

def contains_wanted(file, word):
    print("------------------------------")
    try:
        with open(file, 'r', encoding="utf8") as fileString:
            data = (fileString.read().replace('\n', '')).encode()
            if re.search(word.encode(), data) is not None:
                return True
    except Exception:
        return False


def analyze_file_docker(file):
    found = []
    for blabla in queriesExtra:
        keywordsAnalyzed = queriesExtra.get(blabla)
        for query_docker in keywordsAnalyzed["inDocker"]:
            if contains_wanted(file, query_docker):
                found.append(blabla)
                break
    return found


def analyze_file_docker_compose(file):
    found = []
    for blabla in queriesExtra:
        keywordsAnalyzed = queriesExtra.get(blabla)
        for query_compose in keywordsAnalyzed["inDockerCompose"]:
            if contains_wanted(file, query_compose):
                found.append(blabla)
                break
    return found


def isDockerFile(file):
    if re.search('Dockerfile*', file):
        return True
    else:
        return False


def isDocker(file):
    if re.search('docker-compose*', file):
        return True
    else:
        return False


def is_src_folder(folder):
    if re.search('src*', folder):
        return True
    else:
        return False


def find_src_folder(path):
    src_folder_tab = []
    for folder_recu_src in os.listdir(path):
        new_path_recu_src = path + "/" + folder_recu_src
        if os.path.isdir(new_path_recu_src):
            if is_src_folder(new_path_recu_src):
                src_folder_tab.append(new_path_recu_src)
            else:
                src_folder_tab += find_src_folder(new_path_recu_src)
    return src_folder_tab


def try_construct_path(src_folder):
    new_src_folder = src_folder + "/main/resources/"
    if os.path.isdir(new_src_folder):
        for file in os.listdir(new_src_folder):
            #file_absolute_path = file + "/" + new_src_folder
            file_absolute_path = new_src_folder + "/" + file

            if re.search('application.properties', file_absolute_path):
                print(file_absolute_path)
                return file_absolute_path
    return None


def find_app_properties(path):
    src_folder = find_src_folder(path)
    if len(src_folder) != 0:
        return try_construct_path(src_folder[0])


def analyze_file_spring(file):
    found = []
    for blabla in queriesExtra:
        keywordsAnalyzed = queriesExtra.get(blabla)
        for query_spring in keywordsAnalyzed["inSpring"]:
            if contains_wanted(file, query_spring):
                found.append(blabla)
                break
    return found


def analyzeSpring(path):
    app_properties_path = find_app_properties(path)
    if app_properties_path is not None:
        return analyze_file_spring(app_properties_path)
    else:
        return []


for query in queriesExtra:
    inDocker[query] = 0
    inSpring[query] = 0
    inDockerCompose[query] = 0


for folder in os.listdir(repositoryClone):
    docker = ""
    dockerFile = ""
    print("*****************************")
    newPath = repositoryClone + folder
    if os.path.isdir(newPath):
        numberOfRepo += 1
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

        results_docker = []
        results_docker_compose = []
        results_spring = []

        if docker != "":
            results_docker = analyze_file_docker(docker)
        if dockerFile != "":
            results_docker_compose = analyze_file_docker_compose(dockerFile)
        for result_docker in results_docker:
            inDocker[result_docker] = inDocker[result_docker] + 1
            #if result_docker in results_docker_compose:
                #inBoth[result_docker] = inBoth[result_docker] + 1
        for result_docker_compose in results_docker_compose:
            inDockerCompose[result_docker_compose] = inDockerCompose[result_docker_compose] + 1

        # ana java / js
        print("------------------------ SPRING ANALYSIS        --------------------")
        results_spring = analyzeSpring(newPath)
        for result_spring in results_spring:
            inSpring[result_spring] = inSpring[result_spring] + 1
        print("------------------------ END OF SPRING ANALYSIS --------------------")

        total = 0
        project = {
            "folder": folder
        }
        if results_docker:
            total = total + len(results_docker)
            project["docker"] = len(results_docker)
        if results_docker_compose:
            total = total + len(results_docker_compose)
            project["compose"] = len(results_docker_compose)
        if results_spring:
            total = total + len(results_spring)
            project["spring"] = len(results_spring)
        if total > 0:
            interesting_projects.append([total, project])


print("Number of repo analyzed : " + str(numberOfRepo))
print("Looking for the words : " + str(queries))
print("in docker file : " + str(inDocker))
print("in docker compose : " + str(inDockerCompose))
print("in spring : " + str(inSpring))
#print("in both : " + str(inBoth))
print("Interesting projects : ")
interesting_projects.sort(key=lambda x: x[0], reverse=True)
for interesting_project in interesting_projects:
    docker = interesting_project[1]["docker"] if interesting_project[1].get("docker") else 0
    compose = interesting_project[1]["compose"] if interesting_project[1].get("compose") else 0
    spring = interesting_project[1]["spring"] if interesting_project[1].get("spring") else 0
    print("Values :", interesting_project[0], 
        "dockerfile :", docker,
        "compose :", compose,
        "spring :", spring,
        "repository :", interesting_project[1]["folder"]
    )


workbook = xlsxwriter.Workbook('data.csv')
worksheet = workbook.add_worksheet()
row = 0
col = 0

worksheet.write(row, col, numberOfRepo)
worksheet.write(row, col + 1, "inDocker")
for key in inDocker.keys():
    row += 1
    worksheet.write(row, col, key)
    worksheet.write(row, col + 1, inDocker[key])
row = 0
col += 1
worksheet.write(row, col + 1, "inDockerCompose")
for key in inDockerCompose.keys():
    row += 1
    worksheet.write(row, col + 1, inDockerCompose[key])
row = 0
col += 1
worksheet.write(row, col + 1, "inSpring")
for key in inSpring.keys():
    row += 1
    worksheet.write(row, col + 1, inSpring[key])

workbook.close()
