class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        int n = s.size();
        for(int i = 0; i < n; i++){
            result += pow(26, n - 1 - i) * (s[i] - 'A' + 1);
        }
        return result;
    }
};
