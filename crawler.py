import re
import pygit2
from github import Github
import re

# First create a Github instance:
import os, sys


def file_is_docker_or_compose(file_to_analyze):
    if 'Dockerfile' == file_to_analyze.path or 'docker-compose.yml' == file_to_analyze.path:
        print('This repo has a Dockerfile or a docker-compose.yml, cloning.')
        wantedRepo.append(repoQuery)
        try:
            pygit2.clone_repository(repoQuery.git_url, './repository/' + repoQuery.name + '/')
            return True
        except ValueError:
            print('Repository already cloned')


def contains_docker_file_or_compose_recursively(repo_to_analyze):
    print("Repository : " + repo_to_analyze.name)
    files = repo_to_analyze.get_contents("")
    folders = repo_to_analyze.get_contents("")

    for file in files:
        if file_is_docker_or_compose(file):
            return True
    while folders:
        file_content = folders.pop(0)
        if file_content.type == "dir":
            print('sub-directory not analysed')
            # folders.extend(repoQuery.get_contents(file_content.path))
        else:
            if file_is_docker_or_compose(file_content):
                return True


g = Github(os.environ['TOKEN'])
repositoryClone = './repository/'

repos = []
wantedRepo = []
wanted = []

x = g.get_repos()
reposQuery = g.search_repositories("stars:>5000 topic:docker")

print('Total repos queried : ' + str(reposQuery.totalCount))
for repoQuery in reposQuery:
    contains_docker_file_or_compose_recursively(repoQuery)

print('Number of repos kept : ' + str(len(wantedRepo)))

found = []

count = 0
for dir in os.listdir(repositoryClone):
    for file in os.listdir(repositoryClone + dir):
        # print(file)
        if re.search('Dockerfile|docker-compose.yml', file):
            with open(repositoryClone + dir + '/' + file) as f:
                if re.search('mongo', f.read(), re.IGNORECASE):
                    count += 1
                    found.append(dir)
print('number of times the string mongo has been located : ' + str(count))
print(found)

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
