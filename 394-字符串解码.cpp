class Solution {
public:
    string decodeString(string s) {
        string result;
        string subs;
        int subn;
        int j;
        int x;
        
        for(auto i : s){
            if(i != ']')
                result += i;
            else{
                j = result.size();
                subs = "";
                subn = 0;
                x = 0;
                while(isalpha(result[--j]))
                    subs = result[j] + subs;
                while(j > 0 && isdigit(result[--j]))
                    subn += pow(10, x++) * ((int)result[j] - 48);
                result.erase(j > 0 ? j + 1 : 0);
                for(int z = 0; z < subn; z++){
                    result += subs;
                }
            }
        }

        return result;  
    }
};
