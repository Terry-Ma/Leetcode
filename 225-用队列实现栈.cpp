class MyStack {
public:
    queue<int> myqueue;
    int length;

    /** Initialize your data structure here. */
    MyStack() {
        length = 0;
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        myqueue.push(x);
        length += 1;
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        for(int i = 0; i < length - 1; i++){
            myqueue.push(myqueue.front());
            myqueue.pop();
        }
        int result = myqueue.front();
        myqueue.pop();
        length -= 1;
        return result;
    }
    
    /** Get the top element. */
    int top() {
        for(int i = 0; i < length - 1; i++){
            myqueue.push(myqueue.front());
            myqueue.pop();
        }
        int result = myqueue.front();
        myqueue.push(result);
        myqueue.pop();
        return result;
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return length == 0;
    }
};
