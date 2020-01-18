from github import Github
import re
import pygit2
# First create a Github instance:
import os, sys

g = Github("d4a731d1dc9e40d43f9548929e9b4a62a19badc9")

repos = []
wanted = []

print('Searching dockersamples organization for Dockerfile or docker-compose.yml at root directory')
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
