from git import Repo
import os
import datetime

class GithubHelper:
    def __init__(self, remote) -> None:
        self.repo = Repo.init("./root")
        self.remote = remote
        os.chdir("root")
        os.system("git init") # No harm in initializing multiple times
    
    def commit_changes(self):  
        os.system("git add .")

        date = str(datetime.date.today())
        os.system(f"git commit -m {date}")

        os.system("git branch -M main")

        os.system(f"git remote add DMS {self.remote}")
        
        os.system("git config --global http.version HTTP/1.1")
        os.system("git push -u DMS main")
        os.system("git config --global http.version HTTP/2")