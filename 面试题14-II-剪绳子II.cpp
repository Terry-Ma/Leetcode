class Solution {
public:
    int cuttingRope(int n) {
        int num2;
        
        switch(n % 3){
            case 0: num2 = 0; break;
            case 1: num2 = 2; break;
            case 2: num2 = 1; break;
        }

        switch(n){
            case 2: return 1;
            case 3: return 2;
            default:
                long result = pow(2, num2);
                n -= 2 * num2;
                while(n > 0){
                    result *= 3;
                    result = result % 1000000007; 
                    n -= 3;
                }
                return result;
        } 
    }
};
