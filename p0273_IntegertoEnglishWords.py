class Solution:
    def numberToWords(self, num: int) -> str:
        word_below_20 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                         "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        word_multiple_of_10 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        word_multiple_of_1000 = ["Thousand", "Million", "Billion"]
        if num == 0:
            return "Zero"
        res = ""
        thousands = 0
        while num > 0:
            num1, num2 = num % 1000, num % 100
            hundreds, tens, ones = num1 // 100, num2 // 10, num2 % 10
            if thousands > 0 and num1 > 0:
                res = word_multiple_of_1000[thousands - 1] + " " + res
            if 0 < num2 < 20:
                res = word_below_20[num2 - 1] + " " + res
            elif num2 >= 20:
                res = word_multiple_of_10[tens - 2] + " " + (word_below_20[ones - 1] + " " if ones > 0 else "") + res
            if hundreds > 0:
                res = word_below_20[hundreds - 1] + " Hundred " + res
            num //= 1000
            thousands += 1
        res = res[0:-1]
        return res
