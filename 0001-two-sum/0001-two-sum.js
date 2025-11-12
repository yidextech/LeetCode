/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const set = new Set()

    for(let i =0; i<nums.length; i++){
        check = target - nums[i]
        if(set.has(check)){
            return [i, nums.indexOf(check)]
        }
        set.add(nums[i])
    }
};