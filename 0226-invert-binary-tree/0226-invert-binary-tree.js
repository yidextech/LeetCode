/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if(root == null){
        return root
    }

    let dq = []
    dq.push(root)

    while(dq.length != 0){
        for(let i = 0; i<dq.length; i++){
            cur = dq.shift()
            if(cur.left != null){
                dq.push(cur.left)
            }
            if(cur.right != null){
                dq.push(cur.right)
            }
            [cur.left, cur.right] = [cur.right, cur.left]
        }
    }
    return root
    
};