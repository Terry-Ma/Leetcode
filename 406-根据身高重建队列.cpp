class Solution {
public:
    static bool compare(const vector<int>& a, const vector<int>& b){
        if(a[0] > b[0] || (a[0] == b[0] && a[1] < b[1]))
            return true;
        return false;
    }

    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        stable_sort(people.begin(), people.end(), compare);

        vector<vector<int>> result;
        
        for(int i = 0; i < people.size(); i++){
            result.insert(result.begin() + people[i][1], people[i]);
        }

        return result;
    }
};
