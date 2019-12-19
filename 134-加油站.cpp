class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total = 0;
        int current = 0;
        int i = 0;
        int j = 0;

        while(i < gas.size()){
            total += gas[i] - cost[i];
            current += gas[i] - cost[i];
            if(current < 0){
                current = 0;
                j = i + 1;
            }
            i += 1;
        }

        return total >= 0 ? j : -1;
    }
};
