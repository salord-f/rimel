import base64
import datetime
import os
import re

import pygit2
from github import Github

garbageW10 = 0


def file_is_interesting(query, file_to_analyze, repo_to_analyze):
	global garbageW10
	if (re.search('Dockerfile*', file_to_analyze.path)
			or re.search('docker-compose*', file_to_analyze.path)):
		print('====> This repo has a Dockerfile or a docker-compose.yml.')
		return True
		'''
		content = base64.b64decode(file_to_analyze.content)
		if re.search(query, content) is not None:
			try:
				print('====> This repo has a Dockerfile or a docker-compose.yml, and has the keyword : ' + query.decode(
					'utf-8') + ', cloning.')
			# pygit2.clone_repository(repo_to_analyze.git_url, './repository/' + repo_to_analyze.name + '/')
			except ValueError:
				print('Repository already cloned')
			except:
				garbageW10 += 1
				print('Can\'t clone because w10 is garbage')
			finally:
				return True
		'''

def recuFolder(folders, repo_to_analyze, query, recursive=True):
	while folders:
		file_content = folders.pop(0)
		if file_content.type == "dir":
			if recursive:
				recuFolder(repo_to_analyze.get_contents(file_content.path), repo_to_analyze, query, True)
		else:
			if file_is_interesting(query, file_content, repo_to_analyze):
				return True


def contains_docker_file_or_compose_recursively(repo_to_analyze, query, folder="", recursive=True):
	files = repo_to_analyze.get_contents(folder)

	for file in files:
		# print(file)
		if file.size > 900000:
			continue
		if isinstance(repo_to_analyze.get_contents(file.path), list):
			# print(repo_to_analyze.get_contents(file.path))
			if recursive:
				if recuFolder(repo_to_analyze.get_contents(file.path), repo_to_analyze, query, False):
					return True
		if file_is_interesting(query, file, repo_to_analyze):
			return True


g = Github(os.environ['TOKEN'])
repositoryClone = './repository/'

repos = []
wantedRepo = []
wanted = []
found = []
from_date = datetime.date(2018, 1, 1)
from_date_query = " created:>" + str(datetime.datetime.strptime(from_date.__str__(), '%Y-%m-%d').date())
# now = datetime.date.today()
x = g.get_repos()
stars = 5
query = "stars:>" + str(stars) + " topic:spring sort:stars"
reposQuery = g.search_repositories(query + from_date_query)

current_stars = stars + 1
old_top_repo = None
top_repo = None

while current_stars > stars:
	print("loop")
	for q in reposQuery:
		try:
			print("-------------------- Repository : " + q.full_name + " --------------------------")
			if top_repo is None:
				top_repo = q
			# print(str(q.full_name) + " " + str(q.created_at))
			if contains_docker_file_or_compose_recursively(q, b'mongo'):
				found.append(q)
				pygit2.clone_repository(q.git_url, './repository/' + q.name + '/')
			current_stars = q.stargazers_count
		except Exception as err:
			print('error')
			print(err)
	print('Current stars : ' + srt(current_stars))
	query = "stars:" + str(stars) + ".." + str(current_stars) + " topic:spring sort:stars"
	reposQuery = g.search_repositories(query + from_date_query)
	if old_top_repo == top_repo:
		break
	old_top_repo = top_repo
	top_repo = None

print("Stopped at stars : " + str(current_stars))

print('Repositories found : ' + str(len(found))

for q in found:
	print(q.full_name)
