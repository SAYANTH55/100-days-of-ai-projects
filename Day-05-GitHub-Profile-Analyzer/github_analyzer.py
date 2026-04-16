import requests

def github_analyzer(username):
    
    url = f"https://api.github.com/users/{username}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        print("GitHub Profile Info")
        print("-------------------")
        print("Name:", data.get("name"))
        print("Username:", data.get("login"))
        print("Public Repos:", data.get("public_repos"))
        print("Followers:", data.get("followers"))
        print("Following:", data.get("following"))
    
    else:
        print("User not found")


username = input("Enter GitHub Username: ")

github_analyzer(username)