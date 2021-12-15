from typing import List


# Convert the ip to a number and find the bit of lowest 1 as max block. Then reduce the size of block until <= remain n.
class Solution:
    def bitOfLowestOne(self, x: int):
        for i in range(32):
            if x & (1 << i):
                return 32 - i
        return -1

    def blockWithLowestOne(self, x: int):
        return 1 << (32 - self.bitOfLowestOne(x))

    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        ip_list = [int(s) for s in ip.split('.')]
        number = (ip_list[0] << 24) + (ip_list[1] << 16) + (ip_list[2] << 8) + ip_list[3]
        res = []
        while n > 0:
            b = self.blockWithLowestOne(number)
            while b > n:
                b = b >> 1
            ip = '.'.join([str(number >> 24 & 255), str(number >> 16 & 255), str(number >> 8 & 255), str(number & 255)])
            res.append(ip + "/" + str(self.bitOfLowestOne(b)))
            n -= b
            number += b
        return res
