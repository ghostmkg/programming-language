import java.util.Stack;

public class MaxHistogramArea {

    // Function to calculate the maximum area in a histogram
    public static int getMaxArea(int[] hist) {
        int n = hist.length;
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0; // To store maximum area
        int top; // To store top of the stack
        int areaWithTop; // To store area with top bar

        int i = 0;
        while (i < n) {
            // Push bar to the stack if it's greater than the top of stack
            if (stack.isEmpty() || hist[stack.peek()] <= hist[i]) {
                stack.push(i++);
            } else {
                // Pop the top and calculate area with top bar as smallest bar
                top = stack.pop();
                areaWithTop = hist[top] * (stack.isEmpty() ? i : i - stack.peek() - 1);
                maxArea = Math.max(maxArea, areaWithTop);
            }
        }

        // Now calculate area for remaining bars in stack
        while (!stack.isEmpty()) {
            top = stack.pop();
            areaWithTop = hist[top] * (stack.isEmpty() ? i : i - stack.peek() - 1);
            maxArea = Math.max(maxArea, areaWithTop);
        }

        return maxArea;
    }

    public static void main(String[] args) {
        int[] histogram = { 6, 2, 5, 4, 5, 1, 6 };
        System.out.println("Maximum area is: " + getMaxArea(histogram));
    }
}
