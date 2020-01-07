class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0 || (x % 10 == 0 && x != 0))
            return false;
        
        int current = 0;
        while(current < x){
            current = 10 * current + x % 10;
            x /= 10;
        }

        return current == x || current / 10 == x;
    }
};
