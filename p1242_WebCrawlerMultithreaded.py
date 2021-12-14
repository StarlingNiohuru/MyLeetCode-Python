from collections import deque
from concurrent import futures
from typing import List


class HtmlParser(object):
    def getUrls(self, url):
        """
        :type url: str
        :rtype List[str]
        """


# BFS with multi-thread
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = set()
        hostname = startUrl.split('/')[2]
        visited.add(startUrl)
        with futures.ThreadPoolExecutor(max_workers=5) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url.split('/')[2] == hostname and url not in visited:
                        tasks.append(executor.submit(htmlParser.getUrls, url))
                        visited.add(url)
        res = list(visited)
        return res
