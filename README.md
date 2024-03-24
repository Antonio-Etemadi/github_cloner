
# GitHub Repository Cloner or OTA For Micropython ESP

This Micropython module is designed for cloning GitHub repositories. By using this module, you can easily obtain a copy of a GitHub repository.

#### WARNING:   
Before using this module, please make sure to save all files  and directories you want to keep in another location. This module will remove all files and directories in the destination path before cloning the repository.




## Installation

Install my-project with npm

```bash
try :
    from github_cloner import Git_cloner
except :
    import urequests as requests
    url = "https://raw.githubusercontent.com/Antonio-Etemadi/github_cloner/main/github_cloner/github_cloner.py"
    response = requests.get(url)
    if response.status_code == 200:
        with open("github_cloner.py", "wb") as file:
            file.write(response.content)
        print("File downloaded successfully.")
    else:
        print("Failed to download the file.")

from github_cloner import Git_cloner
url="https://github.com/Antonio-Etemadi/github_cloner"
cloner = Git_cloner(url)
cloner.run_cloner()
```
or copy main.py from this repository to ESP
## Usage/Examples

```javascript
from github_cloner import Git_cloner
url="<your repository url>"
cloner = Git_cloner(url)
cloner.run_cloner()
```


## Running Tests

after first run

```bash
MPY: soft reboot
File downloaded successfully.
Installing logging (latest) from https://micropython.org/pi/v2 to /lib
Copying: /lib/logging.py
Done
2024-03-23 18:22:35 - github_cloner.console - INFO - .........connecting..........
2024-03-23 18:22:35 - github_cloner.console - INFO - new file:------------/README.md✔
2024-03-23 18:22:35 - github_cloner.console - INFO - new file:------------/github_cloner/__init__.py✔
2024-03-23 18:22:35 - github_cloner.console - INFO - new file:------------/github_cloner/github_cloner.py✔
2024-03-23 18:22:35 - github_cloner.console - INFO - new file:------------/github_cloner/✔
2024-03-23 18:22:35 - github_cloner.console - INFO - new file:------------/main.py✔
2024-03-23 18:22:35 - github_cloner.console - INFO - downloaded:------------ /README.md 
2024-03-23 18:22:35 - github_cloner.console - INFO - downloaded:------------ /github_cloner/__init__.py 
2024-03-23 18:22:35 - github_cloner.console - INFO - downloaded:------------ /github_cloner/github_cloner.py 
2024-03-23 18:22:35 - github_cloner.console - INFO - downloaded:------------ /main.py 
2024-03-23 18:22:35 - github_cloner.console - WARNING - remove file:/github_cloner.py❎
2024-03-23 18:22:35 - github_cloner.console - INFO - cleaned memory 1.472 KB
```
and second run
```bash
MPY: soft reboot
2024-03-23 18:26:34 - github_cloner.github_cloner.console - INFO - .........connecting..........
2024-03-23 18:26:34 - github_cloner.github_cloner.console - INFO - Up to date:------------ /README.md✅ 
2024-03-23 18:26:34 - github_cloner.github_cloner.console - INFO - Up to date:------------ /github_cloner/__init__.py✅ 
2024-03-23 18:26:34 - github_cloner.github_cloner.console - INFO - Up to date:------------ /github_cloner/github_cloner.py✅ 
2024-03-23 18:26:34 - github_cloner.github_cloner.console - INFO - Up to date:------------ /github_cloner/✅ 
2024-03-23 18:26:34 - github_cloner.github_cloner.console - INFO - Up to date:------------ /main.py✅ 
2024-03-23 18:26:34 - github_cloner.github_cloner.console - INFO - cleaned memory 6.976 KB
```
## Authors

- Author: [Antonio Etemadi]
- Email: [AntonioEtemadi@gmail.com]
- GitHub: [https://github.com/Antonio-Etemadi]

