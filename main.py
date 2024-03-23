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
