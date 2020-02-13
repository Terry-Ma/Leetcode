class Solution {
public:
    int numWays(int n) {
        int num1 = 1, num2 = 0, num;
        for(int i = 0; i < n; i++){
            num = num1;
            num1 = (num1 + num2) % 1000000007;
            num2 = num;
        }

        return num1;
    }
};
