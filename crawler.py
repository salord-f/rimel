import base64
import datetime
# First create a Github instance:
import os
import re

from github import Github

garbageW10 = 0


def file_is_interesting(query, file_to_analyze, repo_to_analyze):
	global garbageW10
	if (re.search('Dockerfile*', file_to_analyze.path) or re.search('docker-compose*', file_to_analyze.path)) and repo_to_analyze.get_contents(
		file_to_analyze.path).type != "dir":
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


def recuFolder(folders, repo_to_analyze, recursive=False):
	while folders:
		file_content = folders.pop(0)
		if file_content.type == "dir":
			print(file_content)
			folder = repo_to_analyze.get_contents(file_content.path)
			for file in folder:
				if file_is_interesting(query, file, repo_to_analyze):
					return True
		# if recursive and recuFolder(repo_to_analyze.get_contents(file_content.path), repo_to_analyze, False):
		#    return True
		# folders.extend(repoQuery.get_contents(file_content.path))
		else:
			if file_is_interesting(query, file_content, repo_to_analyze):
				return True


def contains_docker_file_or_compose_recursively(repo_to_analyze, query):
	files = repo_to_analyze.get_contents("")
	folders = repo_to_analyze.get_contents("")

	for file in files:
		if file_is_interesting(query, file, repo_to_analyze):
			return True
	return recuFolder(folders, repo_to_analyze)


def tighten_query(query, queries, low_date, high_date):
	print(low_date)
	print(high_date)
	if low_date > high_date:
		print("Date inversal")
		return
	low_date = datetime.datetime.strptime(low_date.__str__(), '%Y-%m-%d').date()
	high_date = datetime.datetime.strptime(high_date.__str__(), '%Y-%m-%d').date()
	year_diff = int((high_date.year - low_date.year) / 2)
	month_diff = int(((high_date.year - low_date.year) * 12 + (high_date.month - low_date.month)) / 2)

	print("Year diff : " + str(year_diff))
	print("Month diff : " + str(month_diff))

	if year_diff != 0:
		high_date = high_date.replace(year=int(high_date.year - year_diff))
		reposQuery = g.search_repositories(query + " created:" + str(low_date) + ".." + str(high_date))
		print('Total repos queried : ' + str(reposQuery.totalCount))
		if reposQuery.totalCount < 1000:
			queries.append(reposQuery)
			return tighten_query(query, queries, high_date, now)
		tighten_query(query, queries, low_date, high_date)
	elif month_diff != 0:
		print("Month")
		if high_date.month - month_diff <= 0:
			high_date = high_date.replace(year=high_date.year - 1, month=12 + high_date.month - month_diff)
		else:
			high_date = high_date.replace(year=high_date.year, month=high_date.month - month_diff)
		reposQuery = g.search_repositories(query + " created:" + str(low_date) + ".." + str(high_date))
		print('Total repos queried : ' + str(reposQuery.totalCount))
		if reposQuery.totalCount < 1000:
			queries.append(reposQuery)
			return tighten_query(query, queries, high_date, now)
		tighten_query(query, queries, high_date, now)

	else:
		print("Day")


g = Github(os.environ['TOKEN'])
repositoryClone = './repository/'

repos = []
wantedRepo = []
wanted = []
found = []
initial_date = datetime.date(2011, 1, 1)
now = datetime.date.today()

x = g.get_repos()
# reposQuery = g.search_repositories(" created:>2011-01-01")
query = "stars:>5 topic:javascript"
queries = []
tighten_query(query, queries, initial_date, now)

count = 0
for q in queries:
	print(q.totalCount)
	count += q.totalCount
print("Total : " + str(count))
# query = b'mongo'

'''
print('Total repos queried : ' + str(reposQuery.totalCount))
for repoQuery in reposQuery:
	print("-------------------- Repository : " + repoQuery.name + " --------------------------")
	if contains_docker_file_or_compose_recursively(repoQuery, query):
		found.append(repoQuery)

print('Number of repos kept : ' + str(len(wantedRepo)))
'''
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
# print('number of times the string mongo has been located : ' + str(count))
# print(found)
# print(str(garbageW10))

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
