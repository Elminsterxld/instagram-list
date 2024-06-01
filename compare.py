
with open("followers.txt", "r", encoding="utf-8") as file:
    followers = set(file.read().splitlines())

with open("following.txt", "r", encoding="utf-8") as file:
    following = set(file.read().splitlines())

different_followers = followers - following
different_following = following - followers

with open("different.txt", "w", encoding="utf-8") as file:
    for username in different_followers:
        file.write(f"{username} - Follower\n")
    for username in different_following:
        file.write(f"{username} - Followed\n")
