class Twitter:

    def __init__(self):
        self.time = 0                       # timestamp for ordering post
        self.tweetMap = defaultdict(list)   # {userId : [time, tweetId]}
        self.followMap = defaultdict(set)   # {userId : followee}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # store (time, tweetId) in user's list & increment time
        self.tweetMap[userId].append([self.time, tweetId])
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        ## MIN HEAP | time: O(n log n) | space: O(N*m + N*M + n)
        # user must follow themselves to retrieve their own tweets
        self.followMap[userId].add(userId)

        # keep 10 MOST RECENT tweets from followees

        # stores [time, tweetId, followeeId, index of tweet]
        maxHeap = []
        # for every followee userId follows
        for followeeId in self.followMap[userId]:
            # all tweets posted by a followee
            tweets = self.tweetMap[followeeId]

            # if followee has tweets posted
            if tweets:
                index = len(tweets) - 1             # most recent tweet
                time, tweetId = tweets[index]       # time, tweetid of most recent

                # negative time for Max-Heap
                heapq.heappush(maxHeap, (-time, tweetId, followeeId, index - 1))

        # pop least recent tweets from heap
        # add tweet to result, push next tweet from followee, stop after 10
        result = []
        while maxHeap and len(result) < 10:
            count, tweetId, followeeId, nextIndex = heapq.heappop(maxHeap)
            result.append(tweetId)

            # if user has older tweets, push next one
            if nextIndex >= 0:
                time, nextTweetId = self.tweetMap[followeeId][nextIndex]
                heapq.heappush(maxHeap, (-time, nextTweetId, followeeId, nextIndex - 1))
        return result






        # ## SORTING | time: O(# followeeId * max tweets + t log t)
        # # make copy of user's tweet list
        # feed = self.tweetMap[userId][:]
        # # add tweets from all followees
        # for followeeId in self.followMap[userId]:
        #     feed.extend(self.tweetMap[followeeId])
        
        # # sort list by time descending (default is ascending)
        # feed.sort(key=lambda x: x[0], reverse=True)
        
        # # return first 10 tweet IDs
        # return [tweetId for _, tweetId in feed[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        # add followee to follower's follow set
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followee if originally followed
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].discard(followeeId)
        
