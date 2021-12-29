from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stk = []
        res = [0 for _ in range(n)]
        prev_time = 0
        for log in logs:
            fid, log_type, time = log.split(":")
            fid, time = int(fid), int(time)
            if log_type == "start":
                if len(stk) > 0:
                    prev_fid = stk[-1]
                    res[prev_fid] += time - prev_time
                stk.append(fid)
                prev_time = time
            else:
                stk.pop()
                res[fid] += time - prev_time + 1
                prev_time = time + 1
        return res
