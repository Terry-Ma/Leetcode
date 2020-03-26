class Solution {
public:
    bool is_unsigned_int(string& s, int& i){
        int before = i;

        while(i < s.size() && isdigit(s[i]))
            i++;
        
        return i > before;
    }

    bool is_int(string& s, int& i){
        if((i == s.size()) || (!isdigit(s[i]) && s[i] != '+' && s[i] != '-'))
            return false;

        if(!isdigit(s[i]))
            i++;

        return is_unsigned_int(s, i);
    }

    bool isNumber(string s) {
        if(s.empty())
            return false;

        int i = 0;
        while(s[i] == ' ')
            i++;

        bool is_number = is_int(s, i);

        if(i < s.size() && s[i] == '.'){
            i++;
            is_number = is_unsigned_int(s, i) || is_number;
        }

        if(i < s.size() && (s[i] == 'e' || s[i] == 'E')){
            i++;
            is_number = is_number && is_int(s, i);
        }

        while(i < s.size() && s[i] == ' ')
            i++;

        return is_number && i == s.size();
    }
};
