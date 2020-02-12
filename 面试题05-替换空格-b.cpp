class Solution {
public:
    string replaceSpace(string s) {
        int n = s.size() - 1;
        
        for(int i = 0; i < n + 1; i++){
            if(s[i] == ' ')
                s += "  ";
        }

        int m = s.size() - 1;
        while(n >= 0){
            if(s[n] == ' '){
                s[m] = '0';
                s[m - 1] = '2';
                s[m - 2] = '%';
                m -= 3;
            }
            else{
                s[m] = s[n];
                m--;
            }
            n--;
        }

        return s;
    }
};
