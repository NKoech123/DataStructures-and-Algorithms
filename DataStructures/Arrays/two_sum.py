#Leetcode Problem 1
def twoSum(nums, target) :

    hashmap={}
    for i in range(len(nums)):
        complimentary_val=target-nums[i]
        if complimentary_val in hashmap:
            return [i, hashmap[complimentary_val]]
        hashmap[nums[i]]=i
            
