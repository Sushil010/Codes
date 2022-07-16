class Solution:
    def sumOddLengthSubarrays(self, arr):
        output = sum(arr)
        length = len(arr)+1
        for l in range(3,length , 2):
            for i in range(length-l):
                output += sum(arr[i:l+i])
        return output
        