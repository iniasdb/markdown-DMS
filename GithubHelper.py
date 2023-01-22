from git import Repo
import os
import subprocess
import datetime

class GithubHelper:
    def __init__(self) -> None:
        self.repo = Repo.init("./root")
    
    def add_files(self):
        index = self.repo.index
        index.add(".")
        index.commit(str(datetime.datetime.now()))
    
# h = GithubHelper()
# h.add_files()

if __name__ == "__main__":
    # repo_path = os.getenv('REPO_PATH')
    # Repo object used to interact with Git repositories
    # try:
    #     repo = Repo("./root")
    # except:
    #     repo = Repo.init("./root")

    # # check that the repository loaded correctly
    # if not repo.bare:
    #     print('Repo at ./root successfully loaded.')
    #     index = repo.index
    #     index.add("markdown")
    #     index.add("pdf")
    #     index.commit(message="test")
    #     print(repo.git.status())

    # else:
    #     print('Could not load repository at ./root :')
    os.system("cd root")
    os.system("git init") # No harm in initializing multiple times
    os.system("git add .")
    date = str(datetime.date.today())
    print(date)
    os.system(f"git commit -m {date}")
    # message = os.popen("git ls-remote --exit-code").read()
    # print(message)