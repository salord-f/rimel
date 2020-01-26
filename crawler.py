import re
import pygit2
from github import Github
import re


# First create a Github instance:
import os, sys

g = Github(os.environ['TOKEN'])
repositoryClone = './repository/'

repos = []
wantedRepo = []
wanted = []


x = g.get_repos()
reposQuery = g.search_repositories("stars:>3000 topic:docker")


print('Total repos queried : ' + str(reposQuery.totalCount))
for repoQuery in reposQuery:
    # TODO do it recursively, at least for src ...
    print(repoQuery)
    files = repoQuery.get_contents("")
    for file in files:
        if 'Dockerfile' == file.path or 'docker-compose.yml' == file.path:
            print('This repo is being kept' + str(reposQuery.totalCount))
            wantedRepo.append(repoQuery)
            pygit2.clone_repository(repoQuery.git_url, './repository/' + repoQuery.name + '/')
            break
print('Number of repos kept : ' + str(len(wantedRepo)))



count = 0
for dir in os.listdir(repositoryClone):
    for file in os.listdir(repositoryClone + dir):
        print(file)
        if re.search('Dockerfile|docker-compose.yml', file):
            with open(repositoryClone + dir + '/' + file) as f:
                if re.search('mongo', f.read(), re.IGNORECASE):
                    count += 1
print('number of times the string mongo has been located : ' + str(count))


'''
for repo in g.get_organization("dockersamples").get_repos():
    contents = repo.get_contents("")
    for content_file in contents:
        repos.append(repo)
        if 'Dockerfile' == content_file.path or 'docker-compose.yml' == content_file.path:
            #if repo.name not in os.listdir('./repository'):
            wanted.append(repo)
            print(repo.name)
                #pygit2.clone_repository(repo.git_url, './repository/'+repo.name+'/')


print('Total repos in org : ' + str(len(repos)))
print('Total chosen repos : ' + str(len(wanted)))
'''