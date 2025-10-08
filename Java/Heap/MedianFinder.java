import java.util.*;

public class MedianFinder {
    private PriorityQueue<Integer> maxHeap; 
    private PriorityQueue<Integer> minHeap; 

   
    public MedianFinder() {
     
        maxHeap = new PriorityQueue<>(Collections.reverseOrder());
      
        minHeap = new PriorityQueue<>();
    }


    public void addNum(int num) {
        
        maxHeap.offer(num);

        
        minHeap.offer(maxHeap.poll());

        
        if (maxHeap.size() < minHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
    }

    
    public double findMedian() {
        if (maxHeap.size() == minHeap.size()) {
            
            return (maxHeap.peek() + minHeap.peek()) / 2.0;
        } else {
           
            return maxHeap.peek();
        }
    }

   
    public static void main(String[] args) {
        MedianFinder mf = new MedianFinder();
        
        mf.addNum(1);
        System.out.println("After adding 1, Median = " + mf.findMedian());
        
        mf.addNum(2);
        System.out.println("After adding 2, Median = " + mf.findMedian());
        
        mf.addNum(3);
        System.out.println("After adding 3, Median = " + mf.findMedian());
        
        mf.addNum(4);
        System.out.println("After adding 4, Median = " + mf.findMedian());
        
        mf.addNum(5);
        System.out.println("After adding 5, Median = " + mf.findMedian());
    }
}
