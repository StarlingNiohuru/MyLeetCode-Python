class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = minutes / 60 * 360
        h = hour % 12 / 12 * 360 + minutes / 60 * 30
        diff = abs(h - m)
        res = diff if diff <= 180 else 360 - diff
        return res
