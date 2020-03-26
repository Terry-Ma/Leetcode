class MedianFinder {
public:
    /** initialize your data structure here. */
    vector<int> myvector;

    MedianFinder() {}
    
    void addNum(int num) {
        int i = 0;
        while(i < myvector.size() && myvector[i] <= num)
            i++;

        myvector.insert(myvector.begin() + i, num);
    }
    
    double findMedian() {
        if(myvector.size() & 1 == 1)
            return myvector[myvector.size() / 2];
        else{
            int i = myvector.size() / 2;
            
            return (myvector[i - 1] + myvector[i]) / 2.0;
        }
    }
};
