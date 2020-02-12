class Solution {
public:
    int fib(int n) {
        int num1 = 1, num2 = 0, num;

        for(int i = 0; i < n - 1; i++){
            num = num1;
            num1 = (num1 + num2) % 1000000007;
            num2 = num;
        }

        return n == 0 ? 0 : num1;
    }
};
