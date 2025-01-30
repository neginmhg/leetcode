package linkedList;
/*
 * Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 
 * 
 */

//hashmap - key as key and value as linkedlist node
//doubly linkedlist have dummyleft node for LRU and dummyRight for MRU
//each linkedlist node has key and value and pointers for prev and next 
import java.util.HashMap;
import java.util.Map;
class LRUCache {
    //properties
    int capacity;
    Node dummyLeft;
    Node dummyRight;
    Map<Integer, Node> map ;
    public LRUCache(int capacity) {
        this.capacity=capacity;
        this.dummyLeft = new Node(0,0);
        this.dummyRight=new Node(0,0);
        this.map = new HashMap<>();
        this.dummyLeft.next = this.dummyRight;
        this.dummyRight.prev = this.dummyLeft;
    }
    public void addToRight(Node node){
        Node prev = this.dummyRight.prev;
        prev.next= node;
        node.prev= prev;
        node.next = this.dummyRight;
        //remember
        this.dummyRight.prev= node;
    }
    public void remove(Node node){
        Node prev= node.prev;
        Node next= node.next;
        prev.next= next;
        next.prev = prev;
    }
    
    public int get(int key) {
        if(map.containsKey(key)){
            Node curNode =map.get(key);
            remove(curNode);
            addToRight(curNode);
            return curNode.value;
        }else{
            return -1;
        }
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)){
            Node cur = map.get(key);
            remove(cur);   
        }
        Node newNode = new Node(key, value);
        addToRight(newNode);
        map.put(key, newNode);

        while (map.size()>this.capacity){
            Node cur =dummyLeft.next;
            remove(cur);
            map.remove(cur.key);
            
        }
    }
}


class Node{
    int key;
    int value;
    Node prev;
    Node next;

    public Node(int k, int v){
        this.key = k;
        this.value = v;
        this.prev=null;
        this.next=null;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */