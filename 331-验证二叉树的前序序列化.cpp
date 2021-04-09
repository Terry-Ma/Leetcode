class Solution {
public:
    bool isValidSerialization(string preorder) {
        vector<int> stack(1, 1);
        int i = 0;

        while(i < preorder.size()){
            if(preorder[i] != ','){
                if(preorder[i] == '#'){
                    if(stack.size() > 0 && stack[stack.size() - 1] > 0){
                        stack[stack.size() - 1]--;
                        i++;
                        if(stack[stack.size() - 1] == 0) stack.pop_back();
                    }
                    else{
                        return false;
                    }
                }
                else{
                    while(i < preorder.size() && preorder[i] != ',') i++;
                    if(stack.size() > 0 && stack[stack.size() - 1] > 0){
                        stack[stack.size() - 1]--;
                        if(stack[stack.size() - 1] == 0) stack.pop_back();
                        stack.push_back(2);
                    }
                    else{
                        return false;
                    }
                }
            }
            else{
                i++;
            }
        }

        return stack.size() == 0;
    }
};
