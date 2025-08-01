import requests
from datetime import datetime
import os

GITHUB_TOKEN = os.getenv('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')
REPO_OWNER = "SumanAgr13"
REPO_NAME = "PyCharmMiscProject"  # or loop over many
TEAM_MEMBERS = [""]  # GitHub usernames

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_pull_requests():
    url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}"
    print(url)
    prs = []
    while url:
        response = requests.get(url, headers=HEADERS)
        print(response.status_code)
        print(response.text)
        data = response.json()
        for pr in data:
            author = pr['user']['login']
            created_at = pr['created_at']
            created_year = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ").year
            if author in TEAM_MEMBERS and created_year == datetime.now().year:
                prs.append({
                    'title': pr['title'],
                    'author': author,
                    'created_at': created_at,
                    'url': pr['html_url']
                })
        url = response.links.get('next', {}).get('url')
    return prs

if __name__ == "__main__":
    pr_list = get_pull_requests()
    for pr in pr_list:
        print(f"{pr['author']} | {pr['created_at']} | {pr['title']} | {pr['url']}")



