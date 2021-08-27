from github import Github
import sys

print("Hello Repo")
token = sys.argv[1]
g = Github(token)
repos = g.get_user("jakub-qak").get_repos() 
repos_list = [repo.name for repo in repos]
print(repos_list)
print(len(repos_list))