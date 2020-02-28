class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> mystack;
        int i = 0;

        for(int j = 0; j < popped.size(); j++){
            if(mystack.empty() || mystack.top() != popped[j]){
                while(i < pushed.size() && pushed[i] != popped[j]){
                    mystack.push(pushed[i]);
                    i++;
                }

                if(i == pushed.size())
                    return false;

                i++;
            }
            
            else
                mystack.pop();
        }

        return true;
    }
};
