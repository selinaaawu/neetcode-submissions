class Twitter:

    def __init__(self):
        self.time = 0                       # timestamp for ordering post
        self.tweetMap = defaultdict(list)   # {userId : [time, tweetId]}
        self.followMap = defaultdict(set)   # {userId : followee}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # store (time, tweetId) in user's list & increment time
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        ## MIN HEAP | time: O(n log n) | space: O(N*m + N*M + n)
        minHeap = []    # size 10

        # user must follow themselves to retrieve their own tweets
        self.followMap[userId].add(userId)

        # if followees >= 10, keep 10 MOST RECENT tweets from followees
        if len(self.followMap[userId]) >= 10:
            maxHeap = []    

            # for every followee userId follows
            for followeeId in self.followMap[userId]:
                # if followee has tweets posted
                if followeeId in self.tweetMap:
                    # index of most recent tweet
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])

                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            # move into min-heap for final processing
            while maxHeap:
                count, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followeeId, index])
        
        # push newest tweet from each followee into min-heap
        else:
            # for every followee userId follows
            for followeeId in self.followMap[userId]:
                # if followee has tweets posted
                if followeeId in self.tweetMap:
                    # index of most recent tweet
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
            
        # repeatedly pop from heap
        # add tweet to result, push next tweet from followee, stop after 10
        result = []
        while minHeap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            result.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
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
        
