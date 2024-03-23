
# GitHub Repository Cloner For Micropython ESP

This Micropython module is designed for cloning GitHub repositories. By using this module, you can easily obtain a copy of a GitHub repository.

#### WARNING:   
Before using this module, please make sure to save all files  and directories you want to keep in another location. This module will remove all files and directories in the destination path before cloning the repository.




## Installation

Copy main.py from this repository to your ESP, or run this code.

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

## Usage/Examples

```javascript
from github_cloner import Git_cloner
url="<your repository url>"
cloner = Git_cloner(url)
cloner.run_cloner()
```


## Authors

- Author: [Antonio Etemadi]
- Email: [AntonioEtemadi@gmail.com]
- GitHub: [https://github.com/Antonio-Etemadi]

