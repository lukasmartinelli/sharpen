class Solution:
    # @param A : integer
    # @return a list of list of integers
    def squareSum(self, A):
        ans = []
        a = 0
        while pow(a, 2) <= A:
            b = a  # Ensures a <= b
            while pow(b, 2) <= A:
                print(a, b)
                if pow(a, 2) + pow(b, 2) == A:
                    newEntry = [a, b]
                    ans.append(newEntry)
                b += 1
            a += 1
        return ans

print(Solution().squareSum(2))
print(Solution().squareSum(3))
print(Solution().squareSum(16))
