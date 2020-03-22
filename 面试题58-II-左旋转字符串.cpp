class Solution {
public:
    void reverse(string& s, int left, int right){
        while(left < right){
            swap(s[left], s[right]);
            left++;
            right--;
        }
    }

    string reverseLeftWords(string s, int n) {
        reverse(s, 0, s.size() - 1);
        reverse(s, 0, s.size() - 1 - n);
        reverse(s, s.size() - n, s.size() - 1);

        return s;
    }
};
