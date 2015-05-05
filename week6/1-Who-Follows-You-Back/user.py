import requests


class User:

    API = "https://api.github.com/users/"
    CLIENT_ID = "?client_id=c3001a441a35e430854f"
    CLIENT_SECRET = "&client_secret=081e7b71cfc3463987a7af2888b8676ff099c782"

    def __init__(self, username):
        self.username = username
        self.url = self.user_url(username)

        self.followers_url = User.API + "{}/followers".format(self.username)\
            + User.CLIENT_ID + User.CLIENT_SECRET
        self.following_url = User.API + "{}/following".format(self.username)\
            + User.CLIENT_ID + User.CLIENT_SECRET

        self.followers_dict = self.crawl_information(self.followers_url)
        self.following_dict = self.crawl_information(self.following_url)

        self.followers = []
        self.following = []

    def __hash__(self):
        return hash(self.username)

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username

    def __eq__(self, other):
        return self.username == other.username

    def user_url(self, username):
        return User.API + "{}".format(username)

    def crawl_information(self, url):
        information = requests.get(url).json()

        return information

    def put_followers_to_list(self):
        all_followers = []

        for follower in self.followers_dict:
            new_follower = User(follower["login"])
            all_followers.append(new_follower)

        self.followers.extend(all_followers)

    def put_following_to_list(self):
        all_following = []

        for following in self.following_dict:
            new_following = User(following["login"])
            all_following.append(new_following)

        self.following.extend(all_following)

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following
