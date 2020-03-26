class Solution {
public:
    int lastRemaining(int n, int m) {
        int result = 0;

        for(int i = 2; i < n + 1; i++){
            result = (result + (m - 1) % i + 1) % i;
        }

        return result;
    }
};
