from typing import List


# hash map [time][name]=list(city)
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tmap = {}
        res = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            time, amount = int(time), int(amount)
            if time not in tmap:
                tmap[time] = {name: [city]}
            elif name not in tmap[time]:
                tmap[time][name] = [city]
            else:
                tmap[time][name].append(city)
        for t in transactions:
            name, time, amount, city = t.split(',')
            time, amount = int(time), int(amount)
            if amount > 1000:
                res.append(t)
                continue
            for x in range(time - 60, time + 61):
                if x in tmap and name in tmap[x]:
                    for c in tmap[x][name]:
                        if c != city:
                            res.append(t)
                            break
                    else:
                        continue
                    break
        return res
