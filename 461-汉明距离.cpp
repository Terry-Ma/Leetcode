class Solution {
public:
    int hammingDistance(int x, int y) {
        int res = 0;
        int bit = 1;
        for(int i = 0; i < 32; i++){
            bool x_bit = ((x & bit) == 0);
            bool y_bit = ((y & bit) == 0);
            if((int)x_bit + (int)y_bit == 1)
                res++;
            if(i < 31)
                bit <<= 1;
        }

        return res;
    }
};
