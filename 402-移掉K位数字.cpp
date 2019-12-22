class Solution {
public:
    string removeKdigits(string num, int k) {
        if(num.size() == k)
            return "0";
        
        string s = "";
        int i = 0;
        int times = 0;
        int n = num.size();
        int current;

        while(times < n - k && n - i > n - k - times){
            current = INT_MAX;
            for(int j = i; j < k + times + 1; j++){
                if(static_cast<int>(num[j]) < current){
                    i = j;
                    current = static_cast<int>(num[j]);
                }
            }
            s += num[i];
            i += 1;
            times += 1;
        }

        if(times < n - k)
            s += num.substr(i);

        i = 0;
        while(i < s.size() && s[i] == '0')
            i++;
        s = s.substr(i);

        return s.empty() ? "0" : s;
    }
};
