class Solution {
public:
    int divide(int dividend, int divisor) {
        if(dividend == 0)
            return 0;
        
        bool sign = (dividend > 0) ^ (dividend > 0);    // 异或，是否不同
        dividend = dividend > 0 ? -dividend : dividend;
        divisor = divisor > 0 ? -divisor : divisor;
        int total_num, num, result = 0;

        while(dividend < divisor){

            total_num = divisor;
            num = -1;
            
            while(dividend < (total_num << 1)){
                if(total_num < (INT_MIN >> 1))        // 用INT_MIN >> 1来判断
                    break;
                total_num = total_num << 1;   
                num = num << 1;                    
            }

            dividend -= total_num;
            result += num;              // 负数不用处理越界
        }

        if(!sign){
            if(result == INT_MIN)
                return INT_MAX;
            else
                return -result;
        }

        else  
            return result;
    }
};