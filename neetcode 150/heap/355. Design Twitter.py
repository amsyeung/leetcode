"""
355. Design Twitter
Medium
Topics
premium lock icon
Companies
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
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetMap[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        uids = list(self.followMap[userId])
        uids.append(userId)
        for uid in uids:
            if uid in self.tweetMap:
                index = len(self.tweetMap[uid]) - 1
                time, tweetId = self.tweetMap[uid][index]
                heapq.heappush(minHeap, [time, tweetId, uid, index - 1])
        while minHeap and len(res) < 10:
            time, tweetId, uid, next_idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if next_idx >= 0:
                nxt_time, nxt_tweetId = self.tweetMap[uid][next_idx]
                heapq.heappush(minHeap, [nxt_time, nxt_tweetId, uid, next_idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId] = followeeId # follower -> followee
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)

"""
Time Complexity: O(KlogN) for getNewsFeed, where N is the number of followers and K is the number how many most recent to be feed (constant). Other methods have O(1)
Space Complexity: O(N) for getNewsFeed, the maximum size of minHeap equals to the number of followers. 
"""