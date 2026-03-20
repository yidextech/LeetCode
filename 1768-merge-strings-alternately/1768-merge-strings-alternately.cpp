class Solution {
public:
    string mergeAlternately(string word1, string word2) {

        int n = word1.length();
        int m = word2.length();

        int i = 0;
        int j = 0;
        int turn = 1;

        string res = "";

        while (i<n || j<m){
            turn = turn == 1?0:1;
            if(i<n && turn == 0){
                res += word1[i];
                i += 1;
            }
            else if(j<m){
                res += word2[j];
                j += 1;
            }
        }
        return res;

        
    }
};