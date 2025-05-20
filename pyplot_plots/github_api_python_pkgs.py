import requests

# setting up the url query for the specific data we want
# main part url
url = 'https://api.github.com/search/repositories'
# query protion url
url += '?q=language:python+sort:stars+stars:>10000'

# we set this up to set the version of git and how we want it return (json)
# why do we ask for it using braces notation
headers = {'Accept':'application/vnd.github.v3+json'}

# why do we pass headers here?
# we name the var r to represent response
# we use .get() to obtain the data but with the headers and the query
# we modify it to be able to work with it mnore efficiently
# .get() returns a class(response) obj therefore it has atts we can access
r = requests.get(url, headers=headers)

# proving the statuys code to reaffirm the query
print(f"\nStatus code: {r.status_code}")

# convert the response obj to a dict
# Returns the json-encoded content of a response, if any.
# we requested a json format to return with the "+json" in the headers var
response_dict = r.json()

# process results
# I'm presumming that this is bc the dictionary isn't defined yet because the
# dict gets formed through the request and the reposnsive data obtained throuh
# our query with the header data we have specified
print(response_dict.keys())

print(f"\nTotal repos - {response_dict['total_count']}")
print(f"\nCompleted request - {not response_dict['incomplete_results']}")
print(f"\nTotal repos returned - {len(response_dict['items'])}")

# this is already a list of dictionaries
repo_dicts = response_dict['items']

# thi is redunatn but another way of looks at how to call
print(f"First repo - {response_dict['items'][0]['name']}\n")

# simplier wa yto call since we assigned the repos to a new var
print(f"First repo - {repo_dicts[0]['name']}\n")
# show total key with len. keys() shown as white due to the dict doesn't exist 
# until ran and response recived from the request call
print(f"Total keys - {len(repo_dicts[0].keys())}")
# simple for loop to show the keys of the first repo.
# clearly the 'items' value of the reposnse in a list so we use indexing to see
# we could also assing these to new variable chronologicaly
# something like a for loop decalkring a new var wit the idexing matching?
for key in sorted(repo_dicts[0].keys()):
    print(key)

# lol we did this we because we thouigh it was clever but we can do a for loop
print(f"allow_forking - {repo_dicts[0]['allow_forking']}")
print(f"archive_url - {repo_dicts[0]['archive_url']}")
print(f"archived - {repo_dicts[0]['archived']}")
print(f"assignees_url - {repo_dicts[0]['assignees_url']}")
print(f"blobs_url - {repo_dicts[0]['blobs_url']}")
print(f"branches_url - {repo_dicts[0]['branches_url']}")
print(f"clone_url - {repo_dicts[0]['clone_url']}")
print(f"collaborators_url - {repo_dicts[0]['collaborators_url']}")
print(f"comments_url - {repo_dicts[0]['comments_url']}")
print(f"commits_url - {repo_dicts[0]['commits_url']}")
print(f"compare_url - {repo_dicts[0]['compare_url']}")
print(f"contents_url - {repo_dicts[0]['contents_url']}")
print(f"contributors_url - {repo_dicts[0]['contributors_url']}")
print(f"created_at - {repo_dicts[0]['created_at']}")
print(f"default_branch - {repo_dicts[0]['default_branch']}")
print(f"deployments_url - {repo_dicts[0]['deployments_url']}")
print(f"description - {repo_dicts[0]['description']}")
print(f"disabled - {repo_dicts[0]['disabled']}")
print(f"downloads_url - {repo_dicts[0]['downloads_url']}")
print(f"events_url - {repo_dicts[0]['events_url']}")
print(f"fork - {repo_dicts[0]['fork']}")
print(f"forks - {repo_dicts[0]['forks']}")
print(f"forks_count - {repo_dicts[0]['forks_count']}")
print(f"forks_url - {repo_dicts[0]['forks_url']}")
print(f"full_name - {repo_dicts[0]['full_name']}")
print(f"git_commits_url - {repo_dicts[0]['git_commits_url']}")
print(f"git_refs_url - {repo_dicts[0]['git_refs_url']}")
print(f"git_tags_url - {repo_dicts[0]['git_tags_url']}")
print(f"git_url - {repo_dicts[0]['git_url']}")
print(f"has_discussions - {repo_dicts[0]['has_discussions']}")
print(f"has_downloads - {repo_dicts[0]['has_downloads']}")
print(f"has_issues - {repo_dicts[0]['has_issues']}")
print(f"has_pages - {repo_dicts[0]['has_pages']}")
print(f"has_projects - {repo_dicts[0]['has_projects']}")
print(f"has_wiki - {repo_dicts[0]['has_wiki']}")
print(f"homepage - {repo_dicts[0]['homepage']}")
print(f"hooks_url - {repo_dicts[0]['hooks_url']}")
print(f"html_url - {repo_dicts[0]['html_url']}")
print(f"id - {repo_dicts[0]['id']}")
print(f"is_template - {repo_dicts[0]['is_template']}")
print(f"issue_comment_url - {repo_dicts[0]['issue_comment_url']}")
print(f"issue_events_url - {repo_dicts[0]['issue_events_url']}")
print(f"issues_url - {repo_dicts[0]['issues_url']}")
print(f"keys_url - {repo_dicts[0]['keys_url']}")
print(f"labels_url - {repo_dicts[0]['labels_url']}")
print(f"language - {repo_dicts[0]['language']}")
print(f"languages_url - {repo_dicts[0]['languages_url']}")
print(f"license - {repo_dicts[0]['license']}")
print(f"merges_url - {repo_dicts[0]['merges_url']}")
print(f"milestones_url - {repo_dicts[0]['milestones_url']}")
print(f"mirror_url - {repo_dicts[0]['mirror_url']}")
print(f"name - {repo_dicts[0]['name']}")
print(f"node_id - {repo_dicts[0]['node_id']}")
print(f"notifications_url - {repo_dicts[0]['notifications_url']}")
print(f"open_issues - {repo_dicts[0]['open_issues']}")
print(f"open_issues_count - {repo_dicts[0]['open_issues_count']}")
print(f"owner - {repo_dicts[0]['owner']}")
print(f"private - {repo_dicts[0]['private']}")
print(f"pulls_url - {repo_dicts[0]['pulls_url']}")
print(f"pushed_at - {repo_dicts[0]['pushed_at']}")
print(f"releases_url - {repo_dicts[0]['releases_url']}")
print(f"score - {repo_dicts[0]['score']}")
print(f"size - {repo_dicts[0]['size']}")
print(f"ssh_url - {repo_dicts[0]['ssh_url']}")
print(f"stargazers_count - {repo_dicts[0]['stargazers_count']}")
print(f"stargazers_url - {repo_dicts[0]['stargazers_url']}")
print(f"statuses_url - {repo_dicts[0]['statuses_url']}")
print(f"subscribers_url - {repo_dicts[0]['subscribers_url']}")
print(f"subscription_url - {repo_dicts[0]['subscription_url']}")
print(f"svn_url - {repo_dicts[0]['svn_url']}")
print(f"tags_url - {repo_dicts[0]['tags_url']}")
print(f"teams_url - {repo_dicts[0]['teams_url']}")
print(f"topics - {repo_dicts[0]['topics']}")
print(f"trees_url - {repo_dicts[0]['trees_url']}")
print(f"updated_at - {repo_dicts[0]['updated_at']}")
print(f"url - {repo_dicts[0]['url']}")
print(f"visibility - {repo_dicts[0]['visibility']}")
print(f"watchers - {repo_dicts[0]['watchers']}")
print(f"watchers_count - {repo_dicts[0]['watchers_count']}")
print(f"web_commit_signoff_required - {repo_dicts[0]['web_commit_signoff_required']}")

print()

for key, value in repo_dicts[0].items():
    print(f"Key - {key}, Value - {value}")