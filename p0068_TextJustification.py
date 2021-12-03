from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        temp_length = -1
        temp_line, res = [], []
        for word in words:
            temp_line.append(word)
            temp_length += (len(word) + 1)
            if temp_length > maxWidth:
                temp_line.pop()
                char_length = temp_length - len(word) - len(temp_line)
                if len(temp_line) > 1:
                    space_length = maxWidth - char_length
                    short_space_width = space_length // (len(temp_line) - 1)
                    long_space_num = space_length % (len(temp_line) - 1)
                    short_space = " " * short_space_width
                    long_space = short_space + " "
                    new_line = short_space.join(temp_line)
                    new_line = new_line.replace(short_space, long_space, long_space_num)
                else:
                    new_line = temp_line[0] + " " * (maxWidth - len(temp_line[0]))
                res.append(new_line)
                temp_line = [word]
                temp_length = len(word)
        else:
            new_line = " ".join(temp_line) + " " * (maxWidth - temp_length)
            res.append(new_line)
        return res
