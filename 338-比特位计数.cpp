class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num + 1);
        for(int i = 1; i <= num; i++){
            int cur_res = 0;
            int bit = 1;
            while(bit <= i){
                if((bit & i) != 0) cur_res++;
                bit <<= 1;
            }
            res[i] = cur_res;
        }

        return res;
    }
};
