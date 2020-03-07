class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        if(k == 0)
            return vector<int> {};

        priority_queue<int> pq;
        
        for(int i = 0; i < k; i++){
            pq.push(arr[i]);
        }

        for(int i = k; i < arr.size(); i++){
            if(arr[i] < pq.top()){
                pq.pop();
                pq.push(arr[i]);
            }
        }
        
        vector<int> result;
        
        for(int i = 0; i < k; i++){
            result.push_back(pq.top());
            pq.pop();
        }

        return result;
    }
};
