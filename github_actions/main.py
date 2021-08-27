from github import Github
import sys
import csv

print("Hello Repo")
token = sys.argv[1]
g = Github(token)
repos = g.get_user("jakub-qak").get_repos() 
repos_list = [repo.name for repo in repos]
print(repos_list)
print(len(repos_list))

with open("repos.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Repo"])
    for repo in repos_list:
        writer.writerow([repo])