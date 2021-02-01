import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Create AIP call and save the result
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Save API response to variable
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Information analysis about repos
repo_dicts = response_dict['items']
names, stars = [], []
print("Repositories returned:", len(repo_dicts))
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Visualization build
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')
