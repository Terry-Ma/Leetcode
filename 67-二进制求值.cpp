class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.size() - 1, j = b.size() - 1, flag = 0;
        int a_val, b_val, total_val;
        string result;

        while(i >= 0 || j >= 0 || flag > 0){
            a_val = i >= 0 ? a[i--] - '0' : 0;
            b_val = j >= 0 ? b[j--] - '0' : 0;
            total_val = a_val + b_val + flag;
            if(total_val >= 2){
                flag = 1;
                result += (char)(total_val - 2 + '0');
            }
            else{
                flag = 0;
                result += (char)(total_val + '0');
            }
        }

        i = -1;
        j = result.size();
        char t;
        while(++i < --j){
            t = result[i];
            result[i] = result[j];
            result[j] = t;
        }

        return result;
    }
};
