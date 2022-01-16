import string


class Solution:
    def isIPv4(self, queryIP):
        ips = queryIP.split(".")
        if len(ips) == 4:
            for i in ips:
                if not i.isdigit() or not 0 <= int(i) <= 255 or (len(i) > 1 and i[0] == "0"):
                    return False
        else:
            return False
        return True

    def isIPv6(self, queryIP):
        ips = queryIP.split(":")
        if len(ips) == 8:
            for i in ips:
                if len(i) > 4 or len(i) < 1:
                    return False
                for c in i:
                    if c not in set(string.hexdigits):
                        return False
        else:
            return False
        return True

    def validIPAddress(self, queryIP: str) -> str:
        if self.isIPv4(queryIP):
            return "IPv4"
        elif self.isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
