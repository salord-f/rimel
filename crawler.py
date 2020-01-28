import re
import pygit2
from github import Github
import re
import base64


# First create a Github instance:
import os, sys

g = Github(os.environ['TOKEN'])
repositoryClone = './repository/'

repos = []
wantedRepo = []
wanted = []


x = g.get_repos()
reposQuery = g.search_repositories("stars:>5000 topic:docker")

query = b'mongo'


print('Total repos queried : ' + str(reposQuery.totalCount))
for repoQuery in reposQuery:
    # TODO do it recursively, at least for src ...
    print("Repository : " + repoQuery.name)
    files = repoQuery.get_contents("")
    for file in files:
        if 'Dockerfile' == file.path or 'docker-compose.yml' == file.path:
            content = base64.b64decode(file.content)
            if re.search(query, content) is not None:
                try:
                    wantedRepo.append(repoQuery)
                    print('This repo has a Dockerfile or a docker-compose.yml, and either has the keyword : ' + query.decode('utf-8') + ', cloning.')
                    pygit2.clone_repository(repoQuery.git_url, './repository/' + repoQuery.name + '/')
                    break
                except ValueError:
                    print('Repository already cloned')

print('Number of repos kept : ' + str(len(wantedRepo)))

found = []

count = 0
for dir in os.listdir(repositoryClone):
    for file in os.listdir(repositoryClone + dir):
        #print(file)
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