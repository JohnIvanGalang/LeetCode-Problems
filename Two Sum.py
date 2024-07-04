class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # value(len-target): index
        for index, element in enumerate(nums):
            value = target - element
            if value in hashMap:
                return [hashMap[value] , index]
            hashMap[element] = index # stores in the hashmap