class Solution {
public:
    string countAndSay(int n) {
        string cur_str = "1";
        string next_str = "";
        int j, num;
        
        for(int i = 1; i < n; i++){
            j = 0;
            while(j < cur_str.size()){
                num = 1;
                while(j < cur_str.size() - 1 && cur_str[j + 1] == cur_str[j]){
                    num++;
                    j++;
                }
                next_str.push_back((char)(num + '0'));
                next_str.push_back(cur_str[j]);
                j++;
            }
            cur_str = next_str;
            next_str = "";
        }

        return cur_str;
    }
};