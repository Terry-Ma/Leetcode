class Solution {
public:
    bool isPrimes(int k){
        for(int i = 2; i < (int)sqrt(k) + 1; i++){
            if(k % i == 0)
                return false;
        }
        return true;
    }

    int countPrimes(int n) {
        int result = 0;
        result += n > 2 ? 1 : 0;
        result += n > 3 ? 1 : 0;

        int i = 0;

        while(6 * (++i) + 1 < n){
            if(isPrimes(6 * i - 1))
                result += 1;
            if(isPrimes(6 * i + 1))
                result += 1;
        }

        if(6 * i - 1 < n & isPrimes(6 * i - 1))
            result += 1;
        
        return result;
    }
};
