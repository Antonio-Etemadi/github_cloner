# GitHub Repository Cloner

This Micropython module is designed for cloning GitHub repositories. By using this module, you can easily obtain a copy of a GitHub repository.

Please note that before cloning the repository, this module will remove all files and directories in the destination path. Therefore, make sure the destination path is empty or that you have already transferred all its contents to a secure location.

## Installation

Run main.py in Micropython 


Usage
To clone a GitHub repository, you can use the following command:


from github_cloner import Git_cloner
url="https://github.com/Antonio-Etemadi/github_cloner"
cloner = Git_cloner(url)
cloner.run_cloner().

Warning:            
This module will remove all files and directories in the destination path before cloning the repository.

