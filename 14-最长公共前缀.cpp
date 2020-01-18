class Solution {
public:
    string helper(vector<string>& strs, int index){  
        string result = "";

        if(!strs.empty() && index < strs[0].size()){
            int j = 1;
            char current = strs[0][index];
            while(j < strs.size() && index < strs[j].size()){
                if(current != strs[j][index])
                    break;
                j++;
            }
            if(j == strs.size()){
                result += current;
                result += helper(strs, index + 1);
            }
        }
        
        return result;
    }

    string longestCommonPrefix(vector<string>& strs) {
        return helper(strs, 0);
    }
};
