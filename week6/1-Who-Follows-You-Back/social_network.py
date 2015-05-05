from directed_graph import DirectedGraph
from exceptions import TooBigLevelException


class Network:

    def __init__(self):
        self.graph = DirectedGraph()
        self.user = None

    def build_social_graph(self, level, user):
        if level >= 4:
            raise TooBigLevelException
        self.user = user
        self.build_followers_part(level, user)
        self.build_following_part(level, user)

    def build_followers_part(self, level, user):
        visited = set()
        queue = []
        current_level = 0

        queue.append((current_level, user))
        visited.add(user)

        while len(queue) != 0:
            current_level = queue[0][0]
            current_user = queue[0][1]
            queue.pop(0)
            if current_level == level:
                break

            if current_user.get_followers() == []:
                current_user.put_followers_to_list()

            followers = current_user.get_followers()
            for follower in followers:
                if follower not in visited:
                    queue.append((current_level + 1, follower))
                    visited.add(follower)
                    self.graph.add_edge(follower, current_user)

    def build_following_part(self, level, user):
        visited = set()
        queue = []
        current_level = 0

        queue.append((current_level, user))
        visited.add(user)

        while len(queue) != 0:
            current_level = queue[0][0]
            current_user = queue[0][1]
            queue.pop(0)

            if current_level == level:
                break

            if current_user.get_following() == []:
                current_user.put_following_to_list()

            followings = current_user.get_following()

            for following in followings:
                if following not in visited:
                    queue.append((current_level + 1, following))
                    visited.add(following)
                    self.graph.add_edge(current_user, following)

    def do_you_follow(self, user):
        return self.graph.edge_between(self.user, user)

    def do_you_follow_indirectly(self, user):
        return self.graph.path_between(self.user, user)

    def does_he_she_follows(self, user):
        return self.graph.edge_between(user, self.user)

    def does_he_she_follows_indirectly(self, user):
        return self.graph.path_between(user, self.user)

    def who_follows_you_back(self):
        followers = self.user.get_followers()
        following = self.user.get_following()

        follow_back = []
        for follower in followers:
            if follower in following:
                follow_back.append(follower)

        return follow_back
