// Nested for-loops in js

const twoSum = (nums, target) => {
    for (let i=0; i<nums.length; i++){
        for (let j=i+1; j<nums.length; j++){
            if (nums[i] + nums[j] === target) {
                return [i,j]
             }
        }
    }
    
};

// Hashmap in js
const twoSum_optimized = (nums,target) => {
    hashmap = {}
    for (let i=0; i<nums.length;i++){
        comp = target - nums[i]
        if (nums[i] in hashmap){
            return [i, hashmap[nums[i]]]
        }
        hashmap[comp] = i
    }
}

console.log(twoSum_optimized([2,7,11,15],9))