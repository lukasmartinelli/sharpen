class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        numbers = A
        constraint = B
        
        if len(numbers) == 0:
            return 0
            
        if len(numbers) == 1:
            if numbers[0] == constraint:
                return 1
            else:
                return 0
        
        half = len(numbers)/2
        if numbers[half] < constraint:
            return self.findCount(numbers[half:], constraint)
        elif numbers[half] > constraint:
            return self.findCount(numbers[:half], constraint)
        else:
            return 1 + self.findCount(numbers[:half], constraint) + self.findCount(numbers[half+1:], constraint)

print(Solution().findCount([1, 1, 2, 3, 4, 5, 6], 1))
print(Solution().findCount([1, 1, 2, 3, 4, 5, 5, 5, 6], 5))
