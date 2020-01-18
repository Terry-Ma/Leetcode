class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1)
            return s;
        
        string result = "";
        int j1, j2;
        for(int i = 0; i < numRows; i++){
            j1 = i;
            if(i == 0 || i == numRows - 1){
                while(j1 < s.size()){
                    result += s[j1];
                    j1 += 2 * numRows - 2;
                }
            }

            else{
                j2 = 2 * numRows -2 - i;
                while(j2 < s.size()){
                    result += s[j1];
                    result += s[j2];
                    j1 += 2 * numRows - 2;
                    j2 += 2 * numRows - 2;
                }
                if(j1 < s.size())
                    result += s[j1];
            }
        }

        return result;
    }
};
