class Solution {
public:
    int mySqrt(int x) {
        int left = 0;
        int right = pow(2, 15.5);       // 防止平方溢出
        int middle;

        while(left <= right){
            middle = (left + right) / 2;    // 因为是平方根，所以不用担心溢出
            if(middle * middle > x)
                right = middle - 1;
            else if(middle < x)
                left = middle + 1;
            else
                return middle;
        }

        return right;
    }
};
