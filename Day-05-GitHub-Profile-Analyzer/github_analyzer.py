import requests
import matplotlib.pyplot as plt
import os

#  Get GitHub token from environment (safe method)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

def github_analyzer(username):
    
    user_url = f"https://api.github.com/users/{username}"
    repo_url = f"https://api.github.com/users/{username}/repos"
    
    user_response = requests.get(user_url, headers=headers)
    repo_response = requests.get(repo_url, headers=headers)
    
    if user_response.status_code != 200:
        print("User not found")
        return
    
    user_data = user_response.json()
    repos = repo_response.json()
    
    #  Basic Info
    print("\nGitHub Profile Info")
    print("-------------------")
    print("Name:", user_data.get("name"))
    print("Username:", user_data.get("login"))
    print("Public Repos:", user_data.get("public_repos"))
    print("Followers:", user_data.get("followers"))
    print("Following:", user_data.get("following"))
    
    #  Accurate Language Analysis (bytes-based)
    language_bytes = {}
    
    for repo in repos:
        lang_url = repo["languages_url"]
        lang_response = requests.get(lang_url, headers=headers)
        
        if lang_response.status_code == 200:
            data = lang_response.json()
            
            for lang, bytes_count in data.items():
                language_bytes[lang] = language_bytes.get(lang, 0) + bytes_count
    
    if not language_bytes:
        print("\nNo language data available")
        return
    
    #  Sort languages
    sorted_lang = dict(sorted(language_bytes.items(), key=lambda x: x[1], reverse=True))
    
    print("\nLanguage Usage (by code size):")
    total_bytes = sum(sorted_lang.values())
    
    for lang, size in sorted_lang.items():
        percent = (size / total_bytes) * 100
        print(f"{lang}: {percent:.2f}%")
    
    #  Filter small languages (<2%) for clean chart
    filtered_lang = {
        k: v for k, v in sorted_lang.items()
        if (v / total_bytes) > 0.02
    }
    
    labels = filtered_lang.keys()
    sizes = filtered_lang.values()
    
    #  Pie Chart (clean version)
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title(f"{username}'s Tech Stack Analysis (Accurate)")
    plt.tight_layout()
    plt.show()
    
    # ⭐ Top Repository
    if repos:
        top_repo = max(repos, key=lambda x: x["stargazers_count"])
        print("\nTop Repository:")
        print("Name:", top_repo["name"])
        print("Stars:", top_repo["stargazers_count"])


#  Run Program
username = input("Enter GitHub Username: ")
github_analyzer(username)