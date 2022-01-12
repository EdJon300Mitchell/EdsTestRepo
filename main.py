
import base64
import argparse, glob, json, re, subprocess, urllib.request, os, sys
import Release as res
from github import Github
from github import InputGitTreeElement

class release_runner:
   
    #GITHUB_ACCESS_TOKEN = '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'
    #g = Github(GITHUB_ACCESS_TOKEN)
   # repo_list = g.get_user().get_repos()
   # for repo in repo_list:
   #     print(repo.name)

    #repo = g.get_user().get_repo('EdsTestRepo') # repo name
   # new_tag =  repo.create_git_tag("v3.3.3", "Kick Ass Release")
   # repo.index.add(['F:/Development/git/GitHub/EdsTestRepo/main.py', 'F:/Development/git/GitHub/EdsTestRepo/testFile.txt'])
    #repo.index.commit('Pushing this file from Python')
    #origin = repo.remote('origin')
    #origin.push(new_tag)
    try: 
        do_release = res.release(4, 4, 4, "")
        do_release.Execute()

    except Exception as e:
        print(e)
