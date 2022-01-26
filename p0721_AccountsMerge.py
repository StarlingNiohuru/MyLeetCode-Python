from collections import defaultdict
from typing import List


# Build a graph of emails. DFS to find how many islands
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)
        nmap = {}
        for account in accounts:
            main_email = account[1]
            for email in account[1:]:
                adj[main_email].append(email)
                adj[email].append(main_email)
                nmap[email] = account[0]
        visited = set()
        amap = defaultdict(list)

        def dfs(node: str, label: int):
            nonlocal amap, visited
            amap[label].append(node)
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor, label)

        i = 0
        for email in adj:
            if email not in visited:
                dfs(email, i)
                i += 1
        res = []
        for v in amap.values():
            temp = [nmap[v[0]]]
            temp.extend(sorted(v))
            res.append(temp.copy())
        return res
