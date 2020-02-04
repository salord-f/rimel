import re
import pygit2
from github import Github
import re
import base64

# First create a Github instance:
import os, sys


garbageW10 = 0

def file_is_interesting(query, file_to_analyze, repo_to_analyze):
    global garbageW10
    if (re.search('Dockerfile*', file_to_analyze.path) or re.search('docker-compose*', file_to_analyze.path)) and repo_to_analyze.get_contents(file_to_analyze.path).type != "dir":
        content = base64.b64decode(file_to_analyze.content)
        if re.search(query, content) is not None:
            try:
                print('====> This repo has a Dockerfile or a docker-compose.yml, and has the keyword : ' + query.decode('utf-8') + ', cloning.')
                pygit2.clone_repository(repo_to_analyze.git_url, './repository/' + repo_to_analyze.name + '/')
            except ValueError:
                print('Repository already cloned')
            except:
                garbageW10 += 1
                print('Can\'t clone because w10 is garbage')
            finally:
                return True

def recuFolder(folders, repo_to_analyze, recursive = False):
        while folders:
            file_content = folders.pop(0)
            if file_content.type == "dir":
                print(file_content)
                folder = repo_to_analyze.get_contents(file_content.path)
                for file in folder:
                    if file_is_interesting(query,file, repo_to_analyze):
                        return True
                #if recursive and recuFolder(repo_to_analyze.get_contents(file_content.path), repo_to_analyze, False):
                #    return True
            # folders.extend(repoQuery.get_contents(file_content.path))
            else:
                if file_is_interesting(query, file_content, repo_to_analyze):
                    return True


def contains_docker_file_or_compose_recursively(repo_to_analyze, query):
    files = repo_to_analyze.get_contents("")
    folders = repo_to_analyze.get_contents("")

    for file in files:
        if file_is_interesting(query,file, repo_to_analyze):
            return True
    return recuFolder(folders, repo_to_analyze)


g = Github(os.environ['TOKEN'])
repositoryClone = './repository/'

repos = []
wantedRepo = []
wanted = []
found = []

x = g.get_repos()
reposQuery = g.search_repositories("stars:>5000 topic:docker")

query = b'mongo'

print('Total repos queried : ' + str(reposQuery.totalCount))
for repoQuery in reposQuery:
    print("-------------------- Repository : " + repoQuery.name+" --------------------------")
    if contains_docker_file_or_compose_recursively(repoQuery, query):
        found.append(repoQuery)


print('Number of repos kept : ' + str(len(wantedRepo)))

'''
count = 0
for dir in os.listdir(repositoryClone):
    for file in os.listdir(repositoryClone + dir):
        # print(file)
        if re.search('Dockerfile|docker-compose.yml', file):
            with open(repositoryClone + dir + '/' + file) as f:
                if re.search('mongo', f.read(), re.IGNORECASE):
                    count += 1
                    found.append(dir)

'''
print('number of times the string mongo has been located : ' + str(count))
print(found)
print(str(garbageW10))

'''
for repo in g.get_organization("dockersamples").get_repos():
    contents = repo.get_contents("")
    for content_file in contents:
        repos.append(repo)
        if 'Dockerfile' == content_file.path or 'docker-compose.yml' == content_file.path:
            #if repo.name not in os.listdir('./repository'):
            wanted.append(repo)
            print(repo.name)
            break
                #pygit2.clone_repository(repo.git_url, './repository/'+repo.name+'/')


print('Total repos in org : ' + str(len(repos)))
print('Total chosen repos : ' + str(len(wanted)))
'''
