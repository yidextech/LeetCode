/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const map = new Map()

    nums.forEach((num) => {
        if(map.has(num)){
            count = map.get(num)
            map.set(num, count+1)
        }
        else{
            map.set(num,1)
        }
    })
    const sorted_map = new Map([...map.entries()].sort((a,b) => b[1] - a[1]))
    let res = []
    sorted_map.forEach( (value, key) => {
        if(res.length == k){
            return
        }
        res.push(key)
    })
    return res
};