try :
    from github_cloner import Ota_github
except :
    import urequests as requests

url = "https://raw.githubusercontent.com/Antonio-Etemadi/foil/main/ota_cloner.py"
response = requests.get(url)

if response.status_code == 200:
    with open("github_cloner.py", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
    
else:
    print("Failed to download the file.")
from ota_cloner import OTA
url = "github.com/repos/Antonio-Etemadi/foil"
ota_instance = OTA(url)
ota_instance.run_ota()
gc.collect()
