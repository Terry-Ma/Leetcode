class Solution {
public:
    string convertToTitle(int n) {
        stack<int> mystack;
        int a;
        while(n != 0){
            a = n % 26;
            if(a == 0){
                mystack.push(26);
                n = n / 26 - 1;
            }
            else{
                mystack.push(a);
                n = n / 26;
            }
        }

        string s;
        while(!mystack.empty()){
            s += char(mystack.top() + 64);
            mystack.pop();
        }

        return s;
    }
};
