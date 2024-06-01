import instaloader

L = instaloader.Instaloader()


L.login("YOUR USERNAME", "YOUR PASSWORD") 


profile = instaloader.Profile.from_username(L.context, "USERNAME UR OR OTHER PPL")



follow_list = []
following_list = []
count = 0


with open("followers.txt", "w", encoding="utf-8") as file:
    for followee in profile.get_followers():
        follow_list.append(followee.username)
        file.write(follow_list[count] + "\n")
        print(follow_list[count])
        count += 1


count = 0
with open("following.txt", "w", encoding="utf-8") as file:
    for following in profile.get_followees():
        following_list.append(following.username)
        file.write(following_list[count] + "\n")
        print(following_list[count])
        count += 1
