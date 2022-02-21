from collections import defaultdict
from typing import List


# Hash map of island labels. For each loop check how many kinds of labels in neighbours. When need to merge islands,
# update the entire map.
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        label_map = defaultdict(int)
        res = []
        count, label = 0, 0
        for r, c in positions:
            if (r, c) in label_map:
                res.append(count)
                continue
            neighbour_set = set()
            for d in directions:
                nx, ny = r + d[0], c + d[1]
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) in label_map:
                    neighbour_set.add(label_map[(nx, ny)])
            neighbours = len(neighbour_set)
            smallest_label = sorted(neighbour_set)[0] if neighbours else None
            if neighbours == 0:
                count += 1
                label += 1
                label_map[(r, c)] = label
            elif neighbours == 1:
                label_map[(r, c)] = smallest_label
            else:
                label_map[(r, c)] = smallest_label
                for k, v in label_map.items():
                    if v in neighbour_set:
                        label_map[k] = smallest_label
                count -= (neighbours - 1)
            res.append(count)
        return res
