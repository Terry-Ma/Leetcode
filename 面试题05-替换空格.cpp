class Solution {
public:
    string replaceSpace(string s) {
        string result;
        
        for(auto i : s){
            if(i == ' ')
                result += "%20";
            else
                result += i;
        }

        return result;
    }
};
