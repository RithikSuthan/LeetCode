class Twitter:
    
    tweets={}
    friends={}
    temp=[]
    def __init__(self):
        self.tweets={}
        self.friends={}
        self.temp=[]

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId]=[]
        self.tweets[userId].insert(0,tweetId)
        self.temp.insert(0,[userId,tweetId])
    def getNewsFeed(self, userId: int) -> List[int]:
        result=[]
        user_list=[userId]
        if userId in self.friends:
            user_list.extend(self.friends[userId])
        for i in self.temp:
            if i[0] in user_list:
                result.append(i[1])
        if len(result)>10:
            return result[0:10]
        return result  
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.friends:
            self.friends[followerId]=[]
        self.friends[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.friends:
            self.friends[followerId].remove(followeeId)
            