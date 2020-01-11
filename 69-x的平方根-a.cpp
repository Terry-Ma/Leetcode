class Solution {
public:
    int mySqrt(int x) {
        int y = -1;
        double bound = pow(2, 15.5);
        while(++y < bound && y * y <= x);
        return y - 1;
    }
};
