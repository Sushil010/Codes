class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        if len(arr) > 1:
            const = arr[1] - arr[0]
        else:
            return True
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != const:
                return False
        return True