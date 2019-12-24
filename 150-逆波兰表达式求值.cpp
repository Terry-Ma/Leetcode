class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int i = 0;
        int n = tokens.size();
        int num, num1, num2;
        vector<string> a = {"+", "-", "*", "/"};
        string s;
        stack <int> mystack;

        while(i < n){  
            s = tokens[i];
            if(find(a.begin(), a.end(), s) != a.end()){
                num1 = mystack.top();
                mystack.pop();
                num2 = mystack.top();
                mystack.pop();
                if(s == "+")
                    num = num2 + num1;
                else if(s == "-")
                    num = num2 - num1;
                else if(s == "*")
                    num = num2 * num1;
                else
                    num = num2 / num1;
                mystack.push(num);
            }

            else
                mystack.push(stoi(s));
            
            i += 1;
        }

        return mystack.top();
    }
};
