import requests
import json
from datetime import datetime, timedelta

def get_pull_requests(user, repo):
    url = f'https://api.github.com/repos/{user}/{repo}/pulls'
    params = {
        'state': 'all',
        'per_page': 1000
    }
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()

def categorize_pull_requests(pull_requests, weeks):
    now = datetime.utcnow()
    one_week_ago = now - timedelta(weeks=int(weeks))

    categorized_prs = {
        'open': [],
        'closed': [],
        'in_progress': []
    }

    for pr in pull_requests:
        pr_created_at = datetime.strptime(pr['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        if pr_created_at >= one_week_ago:
            pr_data = {
                'id': pr['id'],
                'number': pr['number'],
                'title': pr['title'],
                'state': pr['state'],
                'created_at': pr['created_at'],
                'updated_at': pr['updated_at'],
                'url': pr['html_url']
            }
            if pr['state'] == 'open':
                categorized_prs['open'].append(pr_data)
            elif pr['state'] == 'closed':
                if pr['merged_at'] is not None:
                    categorized_prs['in_progress'].append(pr_data)
                else:
                    categorized_prs['closed'].append(pr_data)

    return categorized_prs

def main(user, repo, weeks):
    pull_requests = get_pull_requests(user, repo)
    categorized_prs = categorize_pull_requests(pull_requests, weeks)

    # Only keep the last 10 PRs from each category
    for state in categorized_prs:
        categorized_prs[state] = categorized_prs[state][:10]

    with open('raw_output.json', 'w') as f:
        json.dump(categorized_prs, f, indent=4)

if __name__ == '__main__':
#    user = input("Enter the GitHub username: ")
#    repo = input("Enter the GitHub repository name: ")
    main(user="tiangolo", repo="fastapi", weeks="3")
