"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 
"""

from collections import defaultdict
from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.count=0
        self.tweetMap=defaultdict(list)
        self.followMap=defaultdict(set) #hashset has O(1) add/remove but list had O(n)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -=1     #set it negative for maxheap in getNewsFeed to work

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]#final list of tweet IDs for the news feed.
        minHeap=[]

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index-1])
        heapq.heapify(minHeap)
        while minHeap and len(res)<10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >=0 :
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

"""
The approach of initially adding only the last tweet of each user and then subsequently adding older tweets when popping them from the heap is efficient for several reasons:

1. Efficiency and Minimizing Work
Immediate Access to Recent Tweets: By adding only the most recent tweet of each followed user to the min-heap at the start, we minimize the initial workload. This means we only consider the latest tweet of each user, which is a small and manageable set, especially compared to potentially processing all tweets from every user.

Dynamic Management of Tweets: As we pop the most recent tweet from the heap, we immediately check if older tweets are available for that user. This way, we dynamically manage the tweets in a lazy-loading fashion rather than loading everything at once.

2. Maintaining Order
Using the Min-Heap: The min-heap structure allows us to efficiently keep track of the most recent tweets across multiple users. By only adding the latest tweet initially, we ensure that the heap contains the most relevant information (the latest tweets) right away.

Accessing Older Tweets: After popping the most recent tweet, we then check if older tweets exist for that user. By pushing the previous tweet back into the heap, we maintain the order of tweets because the heap will always give us the next most recent tweet available.

3. Controlling the Number of Tweets
Limiting to 10 Most Recent Tweets: This method helps efficiently control the number of tweets in the result. Since the user only needs to see the 10 most recent tweets, starting with the latest ones ensures that we reach that limit quickly without needing to process all tweets for each followed user.
4. Avoiding Unnecessary Processing
Reduce Unused Data: If we were to load all tweets from all followed users at the beginning, we might end up processing a lot of data that won't be included in the final result (only the 10 most recent tweets are needed). This approach ensures we only deal with the data that matters.
Example
Let's say User 1 follows User 2 and User 3:
User 2 has tweets with IDs [1, 2, 3] (3 is the most recent).
User 3 has tweets with IDs [4, 5] (5 is the most recent).
In the first step, we add only [3 (count), 3 (tweetId), User 2, index of 2] and [5 (count), 5 (tweetId), User 3, index of 1] to the min-heap.

After popping the latest tweet (let's say 5 from User 3), we then check if there are older tweets available. We find User 3's tweet with ID 4, and push that into the heap.
Conclusion
This strategy strikes a balance between efficiency and simplicity, allowing the code to focus on just the most relevant information (the latest tweets) while still maintaining the ability to retrieve additional tweets as necessary. By leveraging a min-heap, we ensure that the tweets are processed in the correct order, leading to an efficient and effective implementation of the Twitter-like functionality.

"""