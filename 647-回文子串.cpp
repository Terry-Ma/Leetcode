class Solution {
public:
    int countSubstrings(string s) {
        int result = 0;
        int n = s.size();
        for(int mid = 0; mid <= 2 * n - 2; mid++){
            int left = mid / 2;
            int right = (mid + 1) / 2;
            while((left >= 0) && (right < n) && (s[left] == s[right])){
                left--;
                right++;
                result++;
            }
        }
        
        return result;
    }
};

