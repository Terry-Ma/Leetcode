class Solution {
public:
    int min(int a, int b, int c){
        if(a < b)
            return a < c ? a : c;
        else
            return b < c ? b : c;
    }

    int nthUglyNumber(int n) {
        if(n == 0)
            return NULL;

        vector<int> ugly_nums({1});
        int p2 = 0, p3 = 0, p5 = 0, cur_ugly_num;
        
        while(n > ugly_nums.size()){
            cur_ugly_num = min(ugly_nums[p2] * 2, ugly_nums[p3] * 3, ugly_nums[p5] * 5);
            ugly_nums.push_back(cur_ugly_num);
            
            while(ugly_nums[p2] * 2 <= cur_ugly_num)
                p2++;
            while(ugly_nums[p3] * 3 <= cur_ugly_num)
                p3++;
            while(ugly_nums[p5] * 5 <= cur_ugly_num)
                p5++;
        }

        return ugly_nums[ugly_nums.size() - 1];
    }
};