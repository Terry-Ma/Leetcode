class Solution {
public:
    vector<int> constructArr(vector<int>& a) {
        if(a.empty())
            return vector<int> {};

        vector<int> left, right;
        vector<int> result;
        int l = 1, r = 1;
        
        for(int i = 0; i < a.size(); i++){
            if(i == 0){
                left.push_back(1);
                right.push_back(1);
            }

            else{
                l *= a[i - 1];
                r *= a[a.size() - i];
                left.push_back(l);
                right.push_back(r);
            }
        }

        for(int i = 0; i < a.size(); i++){
            result.push_back(left[i] * right[a.size() - i - 1]);
        }

        return result;
    }
};
