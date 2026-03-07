class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int i = 0;
        int j = numbers.size()-1;

        int two_sum = 0;
        
        while(i<j){
            two_sum = numbers[i] + numbers[j];
            if (two_sum == target){
                return {i+1, j+1};
            }
            else if(two_sum < target){
                i++;
            }
            else{
                j--;
            }
        }
        return {};

    }
};