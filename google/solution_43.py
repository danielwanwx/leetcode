class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n, m = len(num1), len(num2)
        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum = product + res[i + j + 1]
                res[i + j] += sum // 10
                res[i + j + 1] = sum % 10
        return ''.join(map(str, res)).lstrip('0')