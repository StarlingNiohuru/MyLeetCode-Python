from collections import deque
from typing import List


class HtmlParser(object):
    def getUrls(self, url):
        """
        :type url: str
        :rtype List[str]
        """


# BFS
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = set()
        hostname = startUrl.split('/')[2]
        visited.add(startUrl)
        tasks = deque([startUrl])
        while len(tasks) > 0:
            for url in htmlParser.getUrls(tasks.popleft()):
                if url.split('/')[2] == hostname and url not in visited:
                    tasks.append(url)
                    visited.add(url)
        res = list(visited)
        return res
