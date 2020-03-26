class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int bit_sum[32] = {0};
        
        for(int i = 0; i < nums.size(); i++){
            unsigned int bit_mask = 1;
            
            for(int j = 31; j >= 0; j--){
                int bit = bit_mask & nums[i];   // 关系运算符高于位运算，要先计算位运算
                if(bit != 0)
                    bit_sum[j] += 1;
                
                bit_mask <<= 1;
            }
        }

        int result = 0;
        for(int j = 0; j < 32; j++){
            result <<= 1;
            result += bit_sum[j] % 3;  
        }

        return result;
    }
};
