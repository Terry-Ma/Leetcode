class Solution {
public:
    int add(int a, int b) {
        int t;

        while(b != 0){
            t = a ^ b;
            b = (unsigned int)(a & b) << 1;
            a = t;
        }
        
        return a;
    }
};
