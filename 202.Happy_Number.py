class Solution:
    def isHappy(self, n: int) -> bool:
        answers = [n]
        while n!=1:
            s = 0
            st = str(n)
            for i in st:
                s = s + int(i)*int(i)
            n = s
            if n in answers:
                return False
            answers.append(n)
        return True