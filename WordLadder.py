from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}
        l = len(beginWord)
        for word in wordList:
            self.addNodesToGraph(beginWord, graph, l, word)
            for word2 in wordList:
                self.addNodesToGraph(word2, graph, l, word)
        n = len(wordList)
        pathlen = {}
        for word in wordList:
            pathlen[word] = n + 1
        pathlen[beginWord] = 0
        pathlen[endWord] = n + 1
        self.traverse(graph, beginWord, pathlen, 0, n + 1)
        return pathlen[endWord] + 1 if pathlen[endWord] < n + 1 else 0

    def addNodesToGraph(self, beginWord, graph, l, word):
        if word != beginWord and self.compare(word, beginWord, l) == 1:
            self.addToGraph(graph, word, beginWord)
            self.addToGraph(graph, beginWord, word)

    def addToGraph(self, graph, word, word2):
        if word not in graph:
            s = set()
        else:
            s = graph[word]
        s.add(word2)
        graph[word] = s

    def traverse(self, graph, source, pathLength, curr, maxd):
        if source not in graph:
            return
        for word in graph[source]:
            if pathLength[word] == 0 or pathLength[word] > curr + 1:
                pathLength[word] = min(pathLength[word], curr + 1)
                self.traverse(graph, word, pathLength, curr + 1, maxd)

    def compare(self, word, word2, l):
        c = 0
        for i in range(l):
            if word[i] != word2[i]:
                c += 1
        return c


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit", "cog", ["lot", "log", "cog"]))
