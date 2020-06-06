package LeetCode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

/*
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 
most recent tweets in the user's news feed. Your design should support the following methods:

    postTweet(userId, tweetId): Compose a new tweet.

    getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must
     be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.

    follow(followerId, followeeId): Follower follows a followee.
    
    unfollow(followerId, followeeId): Follower unfollows a followee.
*/
public class Twitter {

    private Map<Integer, Set<Integer>> userFollowers;
    private Map<Integer, Queue<Integer>> userTimeline;

    /** Initialize your data structure here. */
    public Twitter() {
        userFollowers = new HashMap<>();
        userTimeline = new HashMap<>();
    }

    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        Set<Integer> followers = userFollowers.get(userId);
        if (followers != null) {
            followers.stream().forEach(follower -> addToQueue(follower, tweetId));
        }
        addToQueue(userId, tweetId);
    }

    private void addToQueue(Integer follower, Integer tweetId) {
        Queue<Integer> timeline = userTimeline.get(follower);
        if (timeline == null) {
            timeline = new LinkedList<>();
            userTimeline.put(follower, timeline);
        }
        if (timeline.size() > 10) {
            timeline.poll();
        }
        timeline.add(tweetId);
    }

    /**
     * Retrieve the 10 most recent tweet ids in the user's news feed. Each item in
     * the news feed must be posted by users who the user followed or by the user
     * herself. Tweets must be ordered from most recent to least recent.
     */
    public List<Integer> getNewsFeed(int userId) {
        if (userTimeline.containsKey(userId)) {
            Queue<Integer> feed = userTimeline.get(userId);
            List<Integer> newsFeed = new ArrayList<>();
            newsFeed.addAll(feed);
            return newsFeed;
        } else {
            return Collections.emptyList();
        }
    }

    /**
     * Follower follows a followee. If the operation is invalid, it should be a
     * no-op.
     */
    public void follow(int followerId, int followeeId) {
        if (userFollowers.containsKey(followerId)) {
            userFollowers.get(followeeId).add(followerId);
        } else {
            Set<Integer> followers = new HashSet<>();
            followers.add(followerId);
            userFollowers.put(followeeId, followers);
        }

    }

    /**
     * Follower unfollows a followee. If the operation is invalid, it should be a
     * no-op.
     */
    public void unfollow(int followerId, int followeeId) {
        if (userFollowers.containsKey(followeeId)) {
            userFollowers.get(followeeId).remove(followerId);
        }

    }

    public static void main(String[] args) {
        Twitter inst = new Twitter();
        inst.postTweet(1, 5);
        inst.getNewsFeed(1);
        inst.follow(1, 2);
        inst.postTweet(2, 6);
        inst.getNewsFeed(1);
        inst.unfollow(1, 2);
        inst.getNewsFeed(1);
    }
}