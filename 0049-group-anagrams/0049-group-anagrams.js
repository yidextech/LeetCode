/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const map = new Map()
    let res = []
    for(let i=0; i<strs.length; i++){
        let ana = strs[i].split('').sort().join('')
        if(map.has(ana)){
            map.get(ana).push(strs[i])
        }
        else{
            map.set(ana, []);
            map.get(ana).push(strs[i])
        }
    }
    map.forEach((value, key)=>{
        res.push(value)
    }
    )
    return res
};