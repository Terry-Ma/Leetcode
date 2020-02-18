class Solution {
public:
    double myPow(double x, int n) {
        long abs_n = n >= 0 ? n : -(long)n;
        double result = 1;

        while(abs_n > 0){
            if(abs_n & 1)
                result *= x;
            x *= x;
            abs_n >>= 1;
        }

        return n >= 0 ? result : 1 / result;
    }
};
