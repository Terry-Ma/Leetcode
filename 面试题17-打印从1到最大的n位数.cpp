class Solution {
public:
    vector<int> printNumbers(int n) {
        vector<int> result;
        
        for(int i = 1; i < pow(10, n); i++){
            result.push_back(i);
        }

        return result;
    }
};
