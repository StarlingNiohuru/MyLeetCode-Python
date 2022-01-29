# hash map of right index of 0-9.traverse the num to check if curr digit has a greater number with a larger right index
class Solution:
    def maximumSwap(self, num: int) -> int:
        digit = str(num)
        right_index = [-1 for _ in range(10)]
        for i, c in enumerate(digit):
            right_index[int(c)] = i
        for j, c in enumerate(digit):
            for d in range(9, int(c), -1):
                i = right_index[d]
                if j < i:
                    new_digit = digit[0:j] + digit[i] + digit[j + 1:i] + digit[j] + digit[i + 1:]
                    return int(new_digit)
        return num
