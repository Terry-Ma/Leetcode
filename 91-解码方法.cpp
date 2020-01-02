class Solution {
public:
    int numDecodings(string s) {
        int n = s.size(), num1 = 1, num2, num;
        num2 = s[n - 1] == '0' ? 0 : 1;
        
        for(int i = n - 2; i > -1; i--){
            if(s[i] == '0')
                num = 0;
            else
                num = (((int)s[i] - '0') * 10 + ((int)s[i + 1] - '0') < 27) ? num2 + num1 : num2;
            num1 = num2;
            num2 = num;
        }

        return n > 1 ? num : num2;
    }
};
