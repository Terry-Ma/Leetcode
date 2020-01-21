class Solution {
public:
    void reverse(string& s, int a, int b){
        while(a < b){
            char t = s[a];
            s[a] = s[b];
            s[b] = t;
            a++;
            b--;
        }
    }

    void clear_space(string& s){
        while(s.size() > 0 && s[0] == ' ')
            s.erase(0, 1);
    }

    string reverseWords(string s) {
        clear_space(s);
        reverse(s, 0, s.size() - 1);
        clear_space(s);
        
        int i = 0;
        int n = 0;
        while(i < s.size()){
            if(i > 0 && s[i] == ' ' && s[i - 1] == ' ')
                s.erase(i, 1);
            else if(i > 0 && s[i] == ' ' && s[i - 1] != ' ')
                i++;
            else{
                n = 0;
                while(i < s.size() && s[i] != ' '){
                    i++;
                    n++;
                }
                reverse(s, i - n, i - 1);
            }
        }

        return s;
    }
};
