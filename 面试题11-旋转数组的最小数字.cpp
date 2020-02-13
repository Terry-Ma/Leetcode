class Solution {
public:
    int minArray(vector<int>& numbers) {
        int left = 0, right = numbers.size() - 1, middle;

        while(left < right){
            middle = left + (right - left) / 2;
            if(numbers[middle] < numbers[right])
                right = middle;    // middle小，不能完全排除其为最小值的可能性
            else if(numbers[middle] > numbers[right])
                left = middle + 1;   // middle大，不可能为最小值
            else
                right = right - 1;
        }

        return numbers[right];
    }
};
