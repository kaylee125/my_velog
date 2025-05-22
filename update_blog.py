import feedparser
import git
import os
import re

rss_url = 'https://api.velog.io/rss/@leesh970930'
repo_path = '.'
posts_dir = os.path.join(repo_path, 'velog-posts')
os.makedirs(posts_dir, exist_ok=True)

repo = git.Repo(repo_path)
feed = feedparser.parse(rss_url)

new_posts = []

for entry in feed.entries:
    safe_title = re.sub(r'[\\/*?:"<>|]', '-', entry.title)
    file_name = f"{safe_title}.md"
    file_path = os.path.join(posts_dir, file_name)

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(entry.description)
        new_posts.append(file_path)

if new_posts:
    repo.index.add(new_posts)
    repo.index.commit(f"Add {len(new_posts)} new Velog post(s)")
    origin = repo.remote(name='origin')
    origin.push()
else:
    print("No new posts to commit.")
