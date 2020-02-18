class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0)
            return 1;

        long abs_n = n > 0 ? n : -(long)n;
        if(n > 0)
            return n % 2 == 0 ? myPow(x * x, n / 2) : x * myPow(x * x, (n - 1) / 2);

        else
            return abs_n % 2 == 0 ? 1 / myPow(x * x, abs_n / 2) : 1 / (x * myPow(x * x, (abs_n - 1) / 2));
    }
};
