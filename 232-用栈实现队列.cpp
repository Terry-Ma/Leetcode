class MyQueue {
public:
    stack<int> stack_enqueue;
    stack<int> stack_dequeue;
    int a;

    /** Initialize your data structure here. */
    MyQueue() {

    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        stack_enqueue.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if(stack_dequeue.empty()){
            while(!stack_enqueue.empty()){
                stack_dequeue.push(stack_enqueue.top());
                stack_enqueue.pop();
            }
        }
        a = stack_dequeue.top();
        stack_dequeue.pop();
        return a;
    }
    
    /** Get the front element. */
    int peek() {
        if(stack_dequeue.empty()){
            while(!stack_enqueue.empty()){
                stack_dequeue.push(stack_enqueue.top());
                stack_enqueue.pop();
            }
        }
        return stack_dequeue.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return stack_dequeue.empty() && stack_enqueue.empty();
    }
};