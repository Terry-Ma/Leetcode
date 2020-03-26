class Solution {
public:
    int strToInt(string str) {
        if(str.empty())
            return 0;

        long result = 0;
        int t = -1;

        int i = 0;
        while(i < str.size() & str[i] == ' '){
            i++;
        }

        if((i == str.size()) | (isdigit(str[i]) == 0 & str[i] != '+' & str[i] != '-'))
            return 0;

        if(str[i] == '+'){
            i++;
        }
        else if(str[i] == '-'){
            t = i;
            i++;
        }
        
        while(i < str.size()){
            if(-1 * result < INT_MIN | isdigit(str[i]) == 0){
                break;
            }
            result = result * 10 + (int)str[i] - (int)'0';
            i++;
        }

        if(t == -1){
            if(result > INT_MAX)
                return INT_MAX;
            else   
                return result;
        }

        else{
            if(-1 * result < INT_MIN)
                return INT_MIN;
            else
                return -1 * result;
        }
    }
};
