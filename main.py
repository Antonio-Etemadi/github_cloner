try :
    from github_cloner import Ota_github
except :
    import urequests as requests
    url = "https://raw.githubusercontent.com/Antonio-Etemadi/goithub_cloner/main/github_cloner.py"
    response = requests.get(url)
    if response.status_code == 200:
        with open("github_cloner.py", "wb") as file:
            file.write(response.content)
        print("File downloaded successfully.")
    else:
        print("Failed to download the file.")
    
from github_cloner import Ota_github
#url="your github repository"
#url = "github.com/Antonio-Etemadi/github_cloner"
#url =https://github.com/Antonio-Etemadi/github_cloner

url="https://github.com/Antonio-Etemadi/github_cloner"
ota_instance = Ota_github(url)
ota_instance.run_ota()
gc.collect()
