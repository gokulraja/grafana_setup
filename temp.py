import requests
import json
server = "http://18.223.33.58:3000/"
# Example 1: Get default Home dashboard:
url = server + "/api/dashboards/home"
# To get the dashboard by uid
# url = server + "/api/dashboards/uid/" + uid
headers = {"Authorization":"Bearer #####API_KEY#####"}
r = requests.get(url = url, headers = headers, verify=False)
print(r.json())