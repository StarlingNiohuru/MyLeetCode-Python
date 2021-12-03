from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cmap = {}
        for c in cpdomains:
            count, domain = c.split(" ")
            count = int(count)
            strlist = domain.split(".")
            for i in range(len(strlist)):
                subdomain = ".".join(strlist[i:])
                cmap[subdomain] = cmap.get(subdomain, 0) + count
        res = [str(v) + " " + k for k, v in cmap.items()]
        return res
