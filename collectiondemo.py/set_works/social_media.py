

users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["sanju","rohit","kohli"]

rahul_followers_suggestion=set(users).difference(set(rahul_followers))

print(rahul_followers_suggestion)

mutual_friends=set(rahul_followers).intersection(set(sanju_followers))

print(mutual_friends)
